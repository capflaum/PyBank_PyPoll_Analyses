import os
import csv

#Having trouble running from the right directory
print ("-----")
print (os.getcwd())
os.chdir("C:\\Users\\capfl\\Python-Challenge\\PyBank")
print (os.getcwd())
print ("-----")

Total_Months = 0
total_profit=0

Budget_csv = os.path.join("..","Resources", "budget_data.csv")
with open (Budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

   for row in csvreader:   
        total_profit = total_profit + int(row[1])
        Total_Months = Total_Months+1
        
   print(f"Total Months: {Total_Months}")
   print(f"Total: $ {total_profit}")

    
Average = round(total_profit / Total_Months)
print(f"Average Change: $ {Average}")

Analysis_file = os.path.join("..","analysis", "Analysis.txt")
with open(Analysis_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([Total_Months, total_profit, Average])

#Total Months: 86
#Total: $ 38382578
#Average Change: $ 446309
