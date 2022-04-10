import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

print(f"Header: {csv_header}")
