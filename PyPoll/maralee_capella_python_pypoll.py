
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('election_data.csv')

numberofvotes = 0
totalprofit = 0
totalchange=0
candidates_votes={}

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        numberofvotes = numberofvotes + 1
        candidate = row[2]
        
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1
              
most_votes=0
for candidate in candidates_votes.keys():
    
    if candidates_votes[candidate]> most_votes:
        winner= candidate
        most_votes=candidates_votes[candidate]

print("total votes:" , numberofvotes)
for candidate in candidates_votes.keys():
    print(candidate, candidates_votes[candidate],str((candidates_votes[candidate]/numberofvotes)*100)+"%")
print("Winner:", winner)

with open("Output.txt", "w") as text_file:
    text_file.write("total votes:"+ str(numberofvotes))
    text_file.write("\n")
    for candidate in candidates_votes.keys():
        text_file.write(candidate+" "+str(candidates_votes[candidate])+" "+str((candidates_votes[candidate]/numberofvotes)*100)+"%")
        text_file.write("\n")
    text_file.write("Winner:"+" "+ winner)
    text_file.write("\n")
    