Sub WallstreetAnalysis()

' For interest, measure run time of program
Dim dtOpentime As Date, dtClosetime As Date
Dim strElapsedtime As String
dtOpentime = Time


' Do tasks for each worksheet in the given workbook using "Worksheets" object
' (Challenge task)
' ==================  START For Each Worksheet loop =======================================

For Each ws In Worksheets
    
    ' Label the new column headers for summary table
    ' (static locations in each worksheet determined by developer)
    
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Annual Change"
    ws.Range("K1").Value = "Percentage Change"
    ws.Range("L1").Value = "Total Volume"
    
    ' Lable new columns for greatest change summary table
    ws.Range("O1").Value = "Ticker"
    ws.Range("P1").Value = "Value"
    ws.Range("N2").Value = "Greatest % Increase"
    ws.Range("N3").Value = "Greatest % Decrease"
    ws.Range("N4").Value = "Greatest Total Volume"
    
    ' Declare variable types, initialize counters, set start locations for "Easy" task
    Dim strTicker As String
    Dim lngLastrow As Long
    
    Dim dblTotalvolume As Double
    dblTotalvolume = 0
    
    ' Add these variables for Moderate code to compute annual changes
    Dim dblOpening As Double, dblClosing As Double
    Dim dblAnnualchange As Double, dblPercentchange As Double
    
    ' Add these variables for Hard code to compute greatest changes
    Dim dblGreatestup As Double, dblGreatestdown As Double, dblGreatestvolume As Double
    dblGreatestup = 0
    dblGreatestdown = 0
    dblGreatestvolume = 0
    '
    
    Dim irow As Long
    Dim lngPrevrow As Long
    lngPrevrow = 2
    
    ' Set row location for summary table
    Dim lngSumrow As Long
    lngSumrow = 2
    
    ' Find last row of each worksheet to set stopping point of "for" loop
    lngLastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
'************************ START For Row loop for EASY and MODERATE**************************************
    
    For irow = 2 To lngLastrow
    
    ' Add to total volume until ticker symbol changes
    dblTotalvolume = dblTotalvolume + ws.Cells(irow, 7)
    
'+++++++++++++++++++++++ START line by line checks and computations +++++++++++++++

    ' Check for ticker symbol change in next row
        If (ws.Cells(irow + 1, 1) <> ws.Cells(irow, 1).Value) Then
    
    ' The outer If/Endif clause constitutes the "Easy" task: output ticker and total volume
    
    'Put current ticker name in summary table and its total volume
            strTicker = ws.Cells(irow, 1).Value
            ws.Range("I" & lngSumrow).Value = strTicker
            ws.Range("L" & lngSumrow).Value = dblTotalvolume
        
    'Reset volume tally.  Add to summary table row and store location of end row
            dblTotalvolume = 0
            
    'For Moderate task, now compute the changes for each symbol and
    ' color as red for negative and green for positive
            dblOpening = ws.Range("C" & lngPrevrow)
            dblClosing = ws.Range("F" & irow)
            dblAnnualchange = dblClosing - dblOpening
            ws.Range("J" & lngSumrow) = dblAnnualchange
            If (dblAnnualchange >= 0) Then
                ws.Range("J" & lngSumrow).Interior.ColorIndex = 4
            Else
                ws.Range("J" & lngSumrow).Interior.ColorIndex = 3
            End If
            
    'Compute percentage change, error trap for divide by zero first
           If (dblOpening <> 0) Then
               dblPercentchange = dblAnnualchange / dblOpening
            Else
               dblPercentchange = 0
            End If
    'Write percentage in table
            ws.Range("K" & lngSumrow).NumberFormat = "0.00%"
            ws.Range("K" & lngSumrow).Value = dblPercentchange
                
        lngSumrow = lngSumrow + 1
        lngPrevrow = irow + 1
            
        End If
   
'+++++++++++++++++++++++  END line by line checks and computations ++++++++++++++++
    Next irow
' *********************** END For Row loop for EASY and MODERATE ****************************************
'
' *********************** START of Row Loop for HARD ****************************************************

' Find last row in summary table columns
    lngLastrow = ws.Cells(Rows.Count, 11).End(xlUp).Row
    
    For i = 2 To lngLastrow
    ' Look for largest % increase
    If ws.Range("K" & i) > ws.Range("P2") Then
        ws.Range("P2").Value = ws.Range("K" & i).Value
        ws.Range("P2").NumberFormat = "0.00%"
        ws.Range("O2").Value = ws.Range("I" & i).Value
    End If
    
    ' Look for largest % decrease
    If ws.Range("K" & i) < ws.Range("P3") Then
        ws.Range("P3").NumberFormat = "0.00%"
        ws.Range("P3").Value = ws.Range("K" & i).Value
        ws.Range("O3").Value = ws.Range("I" & i).Value
    End If
    
    ' Look for largest total volume
    If ws.Range("L" & i) > ws.Range("P4") Then
        ws.Range("P4").Value = ws.Range("L" & i).Value
        ws.Range("O4").Value = ws.Range("I" & i).Value
    End If
    
    Next i
 '*********************** END of Row Loop for HARD *************************************************************
    
    
' Size the columns for flexible fit

ws.Columns("I:Q").AutoFit

' Show elapsed time per sheet

dtClosetime = Time
t = Format(dtClosetime - dtOpentime, "hh:mm:ss")

strElapsedtime = "Worksheet " & ws.Name & "  Opened at " & Format(dtOpentime, "hh:mm:ss") _
& "    Closed at " & Format(dtClosetime, "hh:mm:ss")


ws.Range("N9").Value = strElapsedtime

' ======================= END Worksheet loop ========================================

Next ws

End Sub
