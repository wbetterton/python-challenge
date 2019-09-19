import os
import csv
import pandas as pd

csvpath = os.path.join("..","3 - Python","election_data.csv")

csv_pandas_path = "election_data.csv"

poll_df = pd.read_csv(csv_pandas_path, encoding="utf-8")
#poll_df.head()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    vote_count = len(list(csv.reader(open(csvpath))))   

candidate_list = poll_df["Candidate"].value_counts().reset_index()

first_place = candidate_list["index"].iloc[0:1]
first_place_candidate = first_place.to_string(header=None, index=None)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count -1))
print("-------------------------")
print(candidate_list.to_string(header=None, index=None))
print("-------------------------")
print("Winner: " + first_place_candidate)
print("-------------------------")

file = open("resultsfilepoll.txt","w")

file.write("Election Results")
file.write("-------------------------")
file.write("Total Votes: " + str(vote_count -1))
file.write("-------------------------")
file.write(candidate_list.to_string(header=None, index=None))
file.write("-------------------------")
file.write("Winner: " + first_place_candidate)
file.write("-------------------------")

file.close()
