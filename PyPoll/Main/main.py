import os
import csv

# Initialize variables
total_votes = 0
candidates = {}
candidates_votes = {}

# Read data from the CSV file
with open('Resources/election_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate the percentage of votes each candidate won and the total votes each candidate won
for candidate in candidates:
    candidates_votes[candidate] = {
        "percentage": (candidates[candidate] / total_votes) * 100,
        "total_votes": candidates[candidate]
    }

# Determine the winner of the election based on popular vote
winner = max(candidates, key=candidates.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates_votes.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['total_votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
file_path = os.path.join('analysis', 'financial_analysis.txt')
with open(file_path, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, data in candidates_votes.items():
        f.write(f"{candidate}: {data['percentage']:.3f}% ({data['total_votes']})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")