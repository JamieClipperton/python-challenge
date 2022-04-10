
import os
import csv

#Path to collect date from CSV file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Variables 
month_yrs = []
prpfit_losses = []

month_counts = 0
profit_net_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


#To open CSV file to read information
with open(budget_csv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
print(f"Header: {csv_header}")
     
      



print("Financial Analysis")
print("--------------------------------------------------------------------")













