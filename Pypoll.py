#The data that we need to retreive
#1. the total number of votes cast
#2. A complete list of the candidates that received votes.
#3. The percentage of votes each candidate won.
#4. the total number of votes each candidate won.
#5. the winner of the election based on popular vote.

import csv
import os

#Assign a variable for the file to load and the path

file_to_load = os.path.join("resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file

with open(file_to_load) as election_data:

    # to do: read and analyze the data here

    # Read the file object with the reader function
    file_reader=csv.reader(election_data)

    #print header row in the CSV file.

    headers=next(file_reader)
    print(headers)


