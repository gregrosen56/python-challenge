#done using pandas for convenience
import pandas as pd
import csv

with open ("election_data_1.csv") as file1:
    csv1 = pd.read_csv(file1)
    votes1 = len(csv1.index)     #total votes cast
    candidate_votes_1 = csv1["Candidate"].value_counts()        #votes cast for each candidate
    candidate_percent_1 = round((candidate_votes_1/candidate_votes_1.sum()) * 100)         #percentage of votes cast for each candidate
    candidates1 = csv1["Candidate"].value_counts().index.tolist()         #list of candidates
    winner1 = candidates1[0]       #candidate with greatest number of votes

#print findings
print("Election Results (1)")
print("----------------------------------")
print("Total Votes: " + str(votes1))
print("----------------------------------")
for n in range(len(candidates1)):
    print(candidates1[n] + ": " + str(candidate_percent_1[n]) + "% (" + str(candidate_votes_1[n]) + ")")
print("----------------------------------")
print("Winner: " + winner1)
print("----------------------------------")

#export print to text file
f = open('Results_1.txt','w')
f.write("Election Results (1)" + '\n' +
        "----------------------------------" + '\n' +
        "Total Votes: " + str(votes1) + '\n' +
        "----------------------------------" + '\n'
        )
for n in range(len(candidates1)):
    f.write(candidates1[n] + ": " + str(candidate_percent_1[n]) + "% (" + str(candidate_votes_1[n]) + ")" + '\n'
           )
f.write("----------------------------------" + '\n'
        "Winner: " + winner1 + '\n' +
        "----------------------------------" + '\n'
        )
f.close()

#REPEAT PROCESS FOR SECOND DATA FILE
#REPEAT PROCESS FOR SECOND DATA FILE
#REPEAT PROCESS FOR SECOND DATA FILE
#REPEAT PROCESS FOR SECOND DATA FILE

with open ("election_data_2.csv") as file2:
    csv2 = pd.read_csv(file2)
    votes2 = len(csv2.index)     #total votes cast
    candidate_votes_2 = csv2["Candidate"].value_counts()        #votes cast for each candidate
    candidate_percent_2 = round((candidate_votes_2/candidate_votes_2.sum()) * 100)         #percentage of votes cast for each candidate
    candidates2 = csv2["Candidate"].value_counts().index.tolist()         #list of candidates
    winner2 = candidates2[0]       #candidate with greatest number of votes

#print findings
print("")
print("Election Results (2)")
print("----------------------------------")
print("Total Votes: " + str(votes2))
print("----------------------------------")
for n in range(len(candidates2)):
    print(candidates2[n] + ": " + str(candidate_percent_2[n]) + "% (" + str(candidate_votes_2[n]) + ")")
print("----------------------------------")
print("Winner: " + winner2)
print("----------------------------------")

#export print to text file
f = open('Results_2.txt','w')
f.write("Election Results (2)" + '\n' +
        "----------------------------------" + '\n' +
        "Total Votes: " + str(votes2) + '\n' +
        "----------------------------------" + '\n'
        )
for n in range(len(candidates2)):
    f.write(candidates2[n] + ": " + str(candidate_percent_2[n]) + "% (" + str(candidate_votes_2[n]) + ")" + '\n'
           )
f.write("----------------------------------" + '\n'
        "Winner: " + winner2 + '\n' +
        "----------------------------------" + '\n'
        )
f.close()