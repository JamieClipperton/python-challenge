
import os
import csv

#Path to collect date from CSV file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Variables 
count = 0
total_profit = 0
total_profits_change = 0
original_profit = 0
current_profit_change = 0

#Lists
profit_loss_change = []
date = []

#To open CSV file to read information
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        count += 1

        current_profit_change = int(row[1])
        total_profit += current_profit_change

        if (count == 1):
            original_profit = current_profit_change
            continue
        else :
            total_profits_change = current_profit_change - original_profit
            date.append(row[0])
            total_profits_change.append(total_profits_change)
            original_profit = current_profit_change


    

print("Total Months: " + str(count))









