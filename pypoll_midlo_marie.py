# This is the main routine for the PyPoll exercise
#
# Requirements

# Our task is to create a Python script that analyzes the election records to calculate each of the following:

#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.
#

# Initialize variables used for sums or percentages
total_votes = 0
# 
# Initialize empty lists for keeping 
#   Voter ID (represents and individual vote)
#   County_name (not used in this exercise, but stored for completeness here)
#   Candidate name (for producing slate of candidates, finding total number, percentages, and winner)
voter_id = []
county_name = []
candidate_list = []

# Include the operating system module which allows creation of file paths across systems
import os

# Also include the module for reading and operating on CSV files
import csv
import operator

# Identify the path location of the data file, currently in local directory
csvpath = os.path.join("..","Python_me_up_HW3","election_data.csv")
# print(f"{csvpath}")

# Open the file and read header
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    # Read all of the voter ids and candidate names into their corresponding list

    #*************** Start for each row *************************
    for row in csvreader:
        # Append to the voter_id list
        voter_id.append(row[0])
        candidate_list.append(row[2])

    # Total number of votes is simply the length of the voter_id list

    total_votes = len(voter_id)

    # print(f"total votes are  {total_votes}")

    # Use SET function from Python to find unique names in candidate_list
    # (from Python Crash Course book, p. 104)

    candidate_name = set(candidate_list)
    candidate_number = int(len(candidate_name))

    #print(f"Candidates are {candidate_name}")
    #print(f"length of list is  {candidate_number}")

    # sum total votes for each candidate name
    candidate_vote_total = []
    candidate_percentage =[]
    candidate_unique_name = []
    count_votes = 0
    count_names = 1

    for iname in candidate_name:
    
        # print(f"count_names is {count_names}")
        # print(f"candidate name is {candidate_name}")

        compare_name = iname
         
        for i in range(1, int(total_votes)):
            if (compare_name == candidate_list[i] ):
                count_votes += 1

        candidate_vote_total.append(count_votes)
        candidate_percentage.append(count_votes/total_votes)
        candidate_unique_name.append(compare_name)
        count_votes = 0
        count_names += 1

       # Make a dictionary to hold information
    election_dict = {
            "names": candidate_unique_name,
            "percentage": candidate_percentage,
            "vote_total": candidate_vote_total
    }
    print(election_dict)
    print(candidate_percentage)

     # Make a sort index on greatest percentage
    sortbypercent = sorted(candidate_percentage, reverse = True)
    
    print(sortbypercent)
    # print(f"sortbypercent {sortbypercent}  max is {percentmax}")
    test = 1
    for key, value in election_dict.items():
        print(f"test is {test}\n")
        print(f"key and value are {key}  {value}")

        # find the winner
        if ( value  == sortbypercent[0]):
            print(f"in the if check  value is {value} percentmax is {sortbypercent[0]}\n")
            winner = key

        test += 1

        #election_output = f"{names}:  {percentage:.2f} {vote_total}\n"
    #print(election_output)



   
    # Print to screen to check values in real time
    title = "\n\t\tElection Results\n"
    print(title.upper())
    #print(f"\n {title}".upper()")
    print("##################################################################")
    print(f"\nTotal votes: \t\t{total_votes}\n")
    print("##################################################################") 
    for i in range(0,candidate_number):
        print(f"{candidate_unique_name[i]} \t{candidate_percentage[i]:.2%} \t{candidate_vote_total[i]}\n\n")
    print("##################################################################") 
    print(f"\nWinner is:  {winner}\n")
    print("##################################################################") 
    # Write to text file to store ouput for later use

    output_path_file = os.path.join("..","Python_me_up_HW3","election_results.txt")

    # Open a new file in "write" mode and variable name
    with open(output_path_file, 'w') as newtext:
        title = "Election Results\n"
        newtext.write(title)
        newtext.write("#######################################################")
        newtext.write(f"\nTotal votes: \t\t{total_votes}\n")
        newtext.write("##################################################################")    
     
