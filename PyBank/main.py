
import os
import csv

#Path to collect date from CSV file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Variables 
mth_yrs = []
prpfit_losses = []
mth_yrs_count = 0
total_profit = 0
prolo_change = []
grt_inc = 0
wrt_inc = 0
print("Financial Analysis")
print("--------------------------------------------------------------------")


#To open CSV file to read information
with open(budget_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#To count how many months in row 1
    for row in csv_reader:
        mth_yrs_count += 1
        mth_yrs.append(row[0])
        prpfit_losses.append(row[1])
#To print(f"Header: {csv_header}")
#print(f"Total Months: {mth_yrs_count}")    

#To get net total for the profit losses over the entire period 
    for number in prpfit_losses:
        total_profit = total_profit + int(number)

    #print(total_profit)

#To calculate the changes in "Profit/Losses over the entire period"    
    for number in range(len(prpfit_losses)-1):
        prolo_change.append(int(prpfit_losses[number+1])-int(prpfit_losses[number]))

    total_mths = len(mth_yrs)
    sum_prolo = 0
    for number in prolo_change:
        sum_prolo = sum_prolo + number

    avg_chg = round(sum_prolo / (total_mths-1), 2)

    #print(avg_chg)

#To get greatest increase in profits including date

    grt_inc = prolo_change[0]

    for number in prolo_change:
        if number > grt_inc:
            grt_inc = number

    hgt_inc = grt_inc
    hgt_inc_mth = mth_yrs[prolo_change.index(grt_inc)+1]

    #print(mth_yrs[prolo_change.index(grt_inc)+1])

#To get greatest decrease in profits including date 

    wrt_inc = prolo_change[0]

    for number in prolo_change:
        if number<wrt_inc:
            wrt_inc=number

    lwt_inc = wrt_inc
    lwt_inc_mth = mth_yrs[prolo_change.index(wrt_inc)+1]

    #print(mth_yrs[prolo_change.index(wrt_inc)+1])

    print(f"Total Months: {mth_yrs_count}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${avg_chg}")
    print(f"Greatest Increase in Profits: {hgt_inc_mth} (${hgt_inc})")
    print(f"Greatest Decrease in Losses: {lwt_inc_mth} (${lwt_inc})")












