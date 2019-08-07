# This is the main routine for the PyBank exercise
#
# Requirements

# Our task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
#

# Initialize variables used for sums
total_months = 0
net_total = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
# 
# Initialize empty lists for keeping months and monthly changes
month_count = []
month_change = []

# Include the operating system module which allows creation of file paths across systems
import os

# Also include the module for reading and operating on CSV files
import csv

# Identify the path location of the data file, currently in local directory
csvpath = os.path.join("..","Pybank","Payroll.csv")
# print(f"{csvpath}")

# Open the file and read header
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read next row of data and store first values for comparison checks
    row = next(csvreader)
    start_value = int(row[1])

    # Add to total month count using += assignment operator, e.g. b = b + a
    total_months += 1
    # Add to net total the same way
    net_total += int(row[1])
    # Initialize sum of average monthly changes
    average_change = 0
    # Store greatest increase value and month
    greatest_increase = start_value
    greatest_increase_month = row[0]

    # Read each row of data after the header
    #*************** Start for each row *************************
    for row in csvreader:

        # Add to total month count using += assignment operator, e.g. b = b + a
        total_months += 1
        # Add to net total the same way
        net_total += int(row[1])

        # Calculate month to month changes and store amount and month
        amount_change = int(row[1]) - start_value
        average_change = average_change + amount_change
        month_change.append(amount_change)
        month_count.append(row[0])
        start_value = int(row[1])

        # Calculate greatest increase and decrease
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Calculate greatest increase and decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #***************** End of for loop *****************************
    #
    # Compute overall statistics 
    # Average is sum of monthly changes divided by number of changes in the month change list
    
    average_change = average_change / len(month_change)
    
    # Largest positive/negative change
    best =  max(month_change)
    worst = min(month_change)
    
    # Print to screen to check values in real time
    title = "\n\t\tFinancial Analysis of Monthly Changes\n"
    print(title.upper())
    #print(f"\n {title}".upper()")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"\nTotal months: \t\t{total_months}")
    print(f"Net change: \t$ {net_total}")
    print(f"Average change: $ {average_change:.2f}\n\n")
    print(f"Greatest increase in profits: \t{greatest_increase_month} \t$  {best}")
    print(f"Greatest decrease in profits: \t{greatest_decrease_month} \t$ {worst}")
    print(f"\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    # Write to text file to store ouput for later use

    output_path_file = os.path.join("..","Pybank","monthly_data_stats.txt")

    # Open a new file in "write" mode and variable name
    with open(output_path_file, 'w') as newtext:
        title = "Financial Analysis of Monthly Changes\n"
        newtext.write(title)
        newtext.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        newtext.write(f"\nTotal months: \t\t{total_months}")
        newtext.write(f"\nNet change: \t$ {net_total}")
        newtext.write(f"\nAverage change: $ {average_change:.2f}")
        newtext.write(f"\nGreatest increase in profits: \t{greatest_increase_month} \t$  {best}")
        newtext.write(f"\nGreatest decrease in profits: \t{greatest_decrease_month} \t$ {worst}")
        newtext.write(f"\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

