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

#1. Initialize a total vote counter
total_votes = 0

#declare a list of candidate options
candidate_options=[]

# declare an empty dictionary

candidate_votes={}

# winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # to do: read and analyze the data here

    # Read the file object with the reader function
    file_reader=csv.reader(election_data)

    #read the header row in the CSV file.

    headers=next(file_reader)
    
    # print each rown in CSV file

    for row in file_reader:

        #Add to the total vote counter

        total_votes += 1
        
        #get candidate name from each row

        candidate_name = row[2]

        # if the candidate does not match any existing candidates...
        if candidate_name not in candidate_options:
            # add it to the list of candidates
            candidate_options.append(candidate_name)
        
            # begin tracking that candidate's vote count by creating each candidate as a key using the format * dictionary_name[key] *
            candidate_votes[candidate_name]=0

        # add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

#Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # determine the percentage of votes for each candidate by looping through the counts
    # iterate through the candidate list

    for candidate_name in candidate_options:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of the votes
        vote_percentage = float(votes) / float(total_votes) * 100
       
        # 4. Print the candidate name, percentage of votes, and vote count.
        
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # save the candidate results to our text file
        txt_file.write(candidate_results)

        # determine winning vote count and candidate

        if (votes>winning_count) and (vote_percentage > winning_percentage):

            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage

            # and set the winning candidate equal to the candidate's name
            winning_candidate=candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)

    # save the winning candidate's results to the text file.

    txt_file.write(winning_candidate_summary)




