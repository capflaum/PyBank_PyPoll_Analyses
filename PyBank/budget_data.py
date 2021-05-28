import os
import csv

month_count = 0
total_profit=0
last_profit=0
current_profit = 0 
max_profit_change =0

budget_csv = os.path.join("..", "resources", "budget_data.csv")
with open (budget_csv) as budgetData:
    csvreader = csv.reader(budgetData, delimiter=",")
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
     
    Average = round(total_profit / month_count)
     
    text = (    
    f"Total Months: {month_count}\n"

    f"Total: $ {total_profit}\n"
    f"Max Profit Change: {month_of_max_profit_change} ${max_profit_change}\n"
    f"Greatest Decrease in Profits: {month_of_greatest_decrease} ${greatest_decrease}\n"
   
    f"Average Change: ${Average}\n")

    print(text)

analysis_file = os.path.join("..", "analysis", "Analysis.txt")
with open(analysis_file, "w") as txt_file:
    txt_file.write(text)

    #writer.writerow([month_count, total_profit, month_of_max_profit_change, max_profit_change, month_of_greatest_decrease, greatest_decrease, Average])