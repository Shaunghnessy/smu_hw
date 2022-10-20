import csv

#Set the path for the CSV file

election_datacsv = "/Users/shaunghnessyrobertson/Desktop/SMU/GitLab/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

row = 0
count = 0
vote_count = []
vote_percent = []
total_candidates_list = []
candidatelist = []
unique_candidate = []
summary_total_candidate = 0


 # Open the CSV using the set path election_datacsv
with open(election_datacsv, newline="") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_header = next(csvreader)

      # print(row)
     for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
        
     for x in set(candidatelist):
        unique_candidate.append(x)
        
        y = candidatelist.count(x)
        vote_count.append(y)
        
        z = round(100*y/count, 3)
        vote_percent.append(z)
        
        winning_vote_count = max(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]



print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")