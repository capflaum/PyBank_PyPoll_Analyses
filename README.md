import os
import csv

    # Having trouble running from the right directory
print ("-----")
print (os.getcwd())
os.chdir("C:\\Users\\capfl\\Python-Challenge\\PyBank")
print (os.getcwd())
print ("-----")

month_count = 0
total_profit=0
last_profit=0
current_profit = 0 
max_profit_change =0

Budget_csv = os.path.join("..","Resources", "budget_data.csv")
with open (Budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader: 
        total_profit = total_profit + int(row[1])
        month_count = month_count+1

        current_profit = int(row[1])
        change_in_profit = current_profit - last_profit
        if month_count == 2:
            max_profit_change = change_in_profit
        elif month_count > 2:
            if change_in_profit >= max_profit_change:
                max_profit_change = change_in_profit
                month_of_max_profit_change = row[0]
            elif change_in_profit <= max_profit_change:
                greatest_decrease = change_in_profit
                month_of_greatest_decrease = row[0]
        
     
        
    print(f"Total Months: {month_count}")

    print(f"Total: $ {total_profit}")
    print (f"Max Profit Change: {month_of_max_profit_change} ${max_profit_change}")
    print(f"Greatest Decrease in Profits: {month_of_greatest_decrease} ${greatest_decrease}")
    Average = round(total_profit / month_count)
    print(f"Average Change: ${Average}")

        
Analysis_file = os.path.join("..","analysis", "Analysis.txt")
with open(Analysis_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([month_count, total_profit, Average])
