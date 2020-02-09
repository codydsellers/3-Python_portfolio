import os
import csv

# Map the csv file
csv_1 = '03-PyPoll_Resources_election_data.csv'

# Create import dictionaries for the CSV data
candidate_dictionary = {}

# Import the csv data
with open(csv_1,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

# Check to see if candidate is in the dictionary - if so "Add + 1" - if not "set it equal to 1" the first time
    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_dictionary:
            candidate_dictionary[candidate] = candidate_dictionary[candidate] + 1
        else:
            candidate_dictionary[candidate] = 1

print(candidate_dictionary)
print(candidate_dictionary['Khan'])

# calculate the total number of votes cast
total_votes = sum(candidate_dictionary.values())

# the percentage of votes each candidate won
khan_percentage_votes = (candidate_dictionary['Khan']) / (total_votes) * 100
correy_percentage_votes = candidate_dictionary['Correy'] / total_votes * 100
li_percentage_votes = candidate_dictionary['Li'] / total_votes * 100
otooley_percentage_votes = candidate_dictionary["O'Tooley"] / total_votes * 100

# the total number of votes each candidate won
khan_total_votes = candidate_dictionary['Khan']
correy_total_votes = candidate_dictionary['Correy']
li_total_votes = candidate_dictionary['Li']
otooley_total_votes = candidate_dictionary["O'Tooley"]

# the winner of the election based on popular vote.
winner = ""

if khan_total_votes > correy_total_votes and khan_total_votes > li_total_votes and khan_total_votes > otooley_total_votes:
    winner = "Khan"
elif correy_total_votes > khan_total_votes and correy_total_votes > li_total_votes and correy_total_votes > otooley_total_votes:
        winner = "Correy"
elif li_total_votes > correy_total_votes and li_total_votes > khan_total_votes and li_total_votes > otooley_total_votes:
        winner = "Li"
else:
    winner = "O'Tooley"

print("Election Results")
print("---------------------")
print(f'Total Votes: {total_votes}')
print("---------------------")
print(f'Khan: {khan_percentage_votes}% ({khan_total_votes})')
print(f'Correy: {correy_percentage_votes}% ({correy_total_votes})')
print(f'Li: {li_percentage_votes}% ({li_total_votes})')
print(f"O'Tooley: {otooley_percentage_votes}% ({otooley_total_votes})")
print("---------------------")
print(f'Winner: {winner}')
print("---------------------")