from operator import itemgetter
import os
import csv



poll_csv = os.path.join("Resources", "election_data.csv")


#Variables
Vo_iD = []
cny = []
cons = []
khan_con = []
correy_con = []
li_con = []
otool_con = []


print("Election Results")
print("-----------------------------------------")

with open(poll_csv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
#To determine total number of votes cast
    for row in reader:
        Vo_iD.append(int(row[0]))
        cny.append(row[1])
        cons.append(row[2])

        tot_vot = (len(Vo_iD))
            
    print("Total Votes:" + str(tot_vot))
    print("---------------------------------------")

#To determine votes for each candidate
    for con in cons: 
        if con == "Khan":
            khan_con.append(cons)
            kh_vo = len(khan_con)
        elif con == "Correy":
            correy_con.append(cons)
            co_vo = len(correy_con)
        elif con == "Li":
            li_con.append(cons)
            li_vo = len(li_con)
        else:
            otool_con.append(cons)
            otool_vo = len(otool_con)
    #print(kh_vo)
    #print(co_vo)
    #print(li_vo)

#To determine each candidates percentage
    khan_per = round(kh_vo / (tot_vot-1)*100, 3)
    #print(khan_per)
    cor_per = round(co_vo / (tot_vot-1)*100, 3)
    #print(cor_per)
    li_per = round(li_vo / (tot_vot-1)*100, 3)
    #print(li_per)
    otool_per = round(otool_vo / (tot_vot-1)*100, 3)
    #print(otool_per)
    winner = ""
    win_tot = 0
    if len(khan_con)>win_tot:
        win_tot=len(khan_con)
        winner = "Khan"
    if len(correy_con)>win_tot:
        win_tot=len(correy_con)
        winner = "Correy"
    if len(li_con)>win_tot:
        win_tot=len(li_con)
        winner = "Li"
    if len(otool_con)>win_tot:
        win_tot=len(otool_con)
        winner = "O'Tooley"

    print(f"Khan: {khan_per}({kh_vo})")
    print(f"Correy: {cor_per}({co_vo})")
    print(f"Li: {li_per}({li_vo})")
    print(f"O'Tooley: {otool_per}({otool_vo})")

    print("---------------------------------------")

    print(f"Winner: {winner}")

    print("---------------------------------------")

poll_file = 'Analysis/Pypoll Analysis.txt'
with open(poll_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------------------- \n")
    outfile.write(f"Total Votes: {str(tot_vot)})\n")
    outfile.write("----------------------------------------- \n")
    outfile.write(f"Khan: {khan_per}({kh_vo})\n")
    outfile.write(f"Correy: {cor_per}({co_vo})\n")
    outfile.write(f"Li: {li_per}({li_vo})\n")
    outfile.write(f"O'Tooley: {otool_per}({otool_vo})\n")
    outfile.write("----------------------------------------- \n")
    outfile.write(f"Winner:  {winner}\n")
    outfile.write("------------------------------------------\n")










