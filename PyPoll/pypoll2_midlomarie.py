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
#   Voter ID (represents an individual vote)
#   unique candidate name (for producing slate of candidates, finding total number, percentages, and winner)
unique_candidate_name = []
candidate_votes = {}
each_percentage = {}

# Include the operating system
#  module which allows creation of file paths across systems
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
    # Use DictReader method to read past header and store remaining rows 
    # directly into an ordered dictionary
    csvreader = csv.DictReader(csvfile, delimiter=',')
    # print(csvreader)


    for row in csvreader:
     #  print(row["Candidate"])
        namerow = row["Candidate"]

        # Increment total votes as each row is read
        total_votes += 1

        # Keep track of unique names as we loop through rows
        # and initialize the candidate's vote count on first
        # occurence
        if namerow not in unique_candidate_name:
            unique_candidate_name.append(namerow)
            candidate_votes[namerow] = 0

        candidate_votes[namerow] += 1

    # print(unique_candidate_name)
    # print(candidate_votes)
    # print(total_votes)

    # Find the candidate with the most votes, compute overall percentages and print out the results
    maxpercent = 0
    keep_percent =[]
    keep_vote = []

    for name in candidate_votes:
        # retrieve the individual vote total
        each_vote = candidate_votes.get(name)

        # compute the vote percentage for each candidate
        
        each_percentage = float(each_vote / total_votes)

        keep_percent.append(each_percentage)
        keep_vote.append(each_vote)

        if(each_percentage > maxpercent):
            maxpercent = each_percentage
            winner = name

     
    # Print to screen to check values in real time
    title = "\n\t\tElection Results\n"
    print(title.upper())
    #print(f"\n {title}".upper()")
    print("##################################################################")
    print(f"\nTotal votes: \t\t{total_votes}\n")
    print("##################################################################")
    ilist = 0
    for name in candidate_votes:
        print(f" {name}:\t\t {keep_percent[ilist]:.2%} \t {keep_vote[ilist]}")
        ilist += 1
    print("##################################################################") 
    print(f"\nWinner is:  {winner}\n")
    print("##################################################################") 
    # Write to text file to store ouput for later use

    output_path_file = os.path.join("..","Python_me_up_HW3","election_results.txt")

    # # Open a new file in "write" mode and variable name
    with open(output_path_file, 'w') as newtext:
        title = "Election Results\n"
        newtext.write(title)
        newtext.write("#######################################################")
        newtext.write(f"\nTotal votes: \t\t{total_votes}\n")
        newtext.write("##################################################################") 
        ilist = 0
        iout = f"{name}:\t\t {keep_percent[ilist]:.2%} \t {keep_vote[ilist]}"
        for name in candidate_votes:
            newtext.write(iout)
            ilist += 1

        newtext.write("##################################################################") 
        newtext.write(f"\nWinner is:  {winner}\n")
        newtext.write("##################################################################") 