import os
import csv

# set path
budgetpath = os.path.join('budget_data.csv')

# find total rows
total_months = 0

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    if csv.Sniffer().has_header: #skip the header
        next(budgetreader)
    for row in budgetreader:
        total_months += 1

# sum column 2 values
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    if csv.Sniffer().has_header:
        next(budgetreader)
    total_profits = 0
    for row in budgetreader:
        total_profits += int(row[1])

# seperate profit column to list for calculation
profit_list = []

# create a list of monthly profits
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    next(budgetreader)
    for row in budgetreader:
        profit_list.append(row[1])

# convert monthly value list to integers
monthly_values = list(map(int, profit_list))

# calculate change per month
monthly_change = [monthly_values[i + 1] - monthly_values[i] for i in range(len(monthly_values)-1)]

# calculate net change
total_change = sum(monthly_change)

# calculate average change
average_change = total_change / len(monthly_values)

# find max and min values
max_value = max(monthly_values)
min_value = min(monthly_values)

# create a function to identify rows with max and mins
def find_row(input): 
    csvfile = open(budgetpath) 
    budgetreader = csv.reader(csvfile) 
    for row in budgetreader:
      if row[1] == input: 
        return budgetreader.line_num

# find the row indecies to print with max values 
max_val_index = find_row(str(max_value))
min_val_index = find_row(str(min_value))

# create an empty list to collect all rows
all_rows = []

# collect_all_rows of csv
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    for row in budgetreader:
        all_rows.append(row)

# collect string for max and min rows by index. (-1 accounts for index 0)
max_string = all_rows[max_val_index-1]
min_string = all_rows[min_val_index-1]

# print to terminal
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profits}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_string}')
print(f'Greatest Decrease in Profits: {min_string}')

# print to text file
write_path = open('PyBank Output.txt', 'w')
write_path.write(f'Financial Analysis\n')
write_path.write(f'-------------------------\n')
write_path.write(f'Total Months: {total_months}\n')
write_path.write(f'Total: ${total_profits}\n')
write_path.write(f'Average Change: ${average_change}\n')
write_path.write(f'Greatest Increase in Profits: {max_string}\n')
write_path.write(f'Greatest Decrease in Profits: {min_string}\n')
