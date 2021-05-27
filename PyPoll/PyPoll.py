import os
import csv

print ("-----")
print (os.getcwd())
os.chdir("C:\\Users\\capfl\\Python-Challenge\\PyPoll")
print (os.getcwd())
print ("-----")

vote_count = 0

def remove_duplicates(candidatelist):
    uniquelist = []
    for candidate in candidatelist:
        if candidate not in uniquelist:
            uniquelist.append(candidate)
    return uniquelist

#vote_percentages = (votes / vote_count) *100

full_list= []

election_csv = os.path.join("..", "Resources", "election_data.csv")
with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        vote_count = vote_count+1
        full_list.append(row[2])
                  
candidate_list = remove_duplicates(full_list)

#not needed after creating dictionary
#for name in candidate_list:
 #   print (name)

votes = dict()
for name in full_list:
    if (name in votes.keys()):
        votes[name] = votes[name]+1
    else:
        votes[name] = 1
for key in votes:
    print (f"{key}: {votes[key]} votes, {round((votes[key]/vote_count)*100)}%")
    
print(f"Total Votes: {vote_count}")

print(f"Winner: ")


pypoll_analysis = os.path.join("..","analysis", "Analysis.txt")
with open(pypoll_analysis, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow