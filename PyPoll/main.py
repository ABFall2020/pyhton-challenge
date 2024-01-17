import os

import pandas as pd

# Load the dataset
import csv
file_path = "./Resources/election_data.csv"
df = pd.read_csv(file_path)

# Calculate the total number of votes cast
total_votes = len(df)

# Create a list of unique candidates
candidates = df["Candidate"].unique()

# Calculate the percentage of votes and total votes for each candidate
candidate_votes = df["Candidate"].value_counts()
percentage_votes = (candidate_votes / total_votes) * 100

# Find the winner based on popular vote
winner = candidate_votes.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Candidates who received votes:")
for candidate in candidates:
    print(f"{candidate}: {percentage_votes.get(candidate, 0):.3f}% ({candidate_votes.get(candidate, 0)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create a directory for the analysis if it doesn't exist
output_folder = "analysis"
os.makedirs(output_folder, exist_ok=True)

# Specify the file path for the output file
output_file_path = os.path.join(output_folder, "election_results.txt")

# Open a file for writing
with open(output_file_path, "w") as file:
    # Write the results to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write("Candidates who received votes:\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentage_votes.get(candidate, 0):.3f}% ({candidate_votes.get(candidate, 0)})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print a message indicating successful export
print(f"Results have been exported to '{output_file_path}'")