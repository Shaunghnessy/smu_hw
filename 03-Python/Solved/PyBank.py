import csv

# set path for the cvs file

budget_datacsv = "/Users/shaunghnessyrobertson/Desktop/SMU/GitLab/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

row = 0
total = 0
total_months = []
total_profit = []
profit_change = []
 
# Open the budget_datacsv 

with open(budget_datacsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # print(row)
    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Calculate changes
    for x in range(len(total_profit)-1):
        profit_change.append(total_profit[x+1]-total_profit[x])
        
    # Find min/max of changes 
    max_increase_val = max(profit_change)
    max_increase_month = profit_change.index(max(profit_change)) + 1

    max_decrease_val = min(profit_change)
    max_month = profit_change.index(min(profit_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: $ {sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} $ {(str(max_increase_val))}")
print(f"Greatest Decrease in Profits: {total_months[max_month]} $ {(str(max_decrease_val))}")

with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {len(total_months)}" + "\n")
    text.write(f"Total: $ {sum(total_profit)}" + "\n")
    text.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}" + "\n")
    text.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} $ {(str(max_increase_val))}" + "\n")
    text.write(f"Greatest Decrease in Profits: {total_months[max_month]} $ {(str(max_decrease_val))}" + "\n") 