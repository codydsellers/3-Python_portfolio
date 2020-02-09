import os
import csv

# Map the csv file
csv_1 = '03-PyBank_Resources_budget_data.csv'

# Create import lists for the CSV data
month_list = []
profit_loss_list = []

# Import the csv file
with open(csv_1,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        month_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

# The total number of months included in the dataset.
total_months = len(month_list)

# The net profit/loss
net_profit_loss = 0

for x in profit_loss_list:
    net_profit_loss = net_profit_loss + x

# The average profit/loss
average_monthly_change_list = []
previous_month_amount = 0

for x in range(len(profit_loss_list)):
    if x == 0:
        previous_month_amount = profit_loss_list[x]
    else:
        monthly_change = profit_loss_list[x] - previous_month_amount
        average_monthly_change_list.append(monthly_change)
        previous_month_amount = profit_loss_list[x]

# Print(average_monthly_change_list)

length = len(average_monthly_change_list)
total = sum(average_monthly_change_list)
profit_loss_average = total / length
print(profit_loss_average)

# The min and max profit/loss and corresponding month
month_greatest_increase = ''
amount_greatest_increase = 0
month_greatest_decrease = ''
amount_greatest_decrease = 0

for x in range(len(average_monthly_change_list)):
    if average_monthly_change_list[x] > amount_greatest_increase:
        amount_greatest_increase = average_monthly_change_list[x]
        month_greatest_increase = month_list[x+1]
    elif average_monthly_change_list[x] < amount_greatest_decrease:
        amount_greatest_decrease = average_monthly_change_list[x]
        month_greatest_decrease = month_list[x+1]

# The total number of months included in the dataset
print(f'There are {total_months} months included in the dataset.')

# The net total amount of "Profit/Losses" over the entire period
print(f'The total Profit/Loss over the entire period was ${net_profit_loss}.')

# The average of the changes in "Profit/Losses" over the entire period
print(f'The average of the changes in Profit/Loss over the entire period was {profit_loss_average}.')

# The greatest increase in profits (date and amount) over the entire period
print(f'The greatest increase in profits over the entire period was in {month_greatest_increase} for ${amount_greatest_increase}.')

# The greatest decrease in losses (date and amount) over the entire period
print(f' The greatest decrease in losses over the entire period was in {month_greatest_decrease} for ${amount_greatest_decrease}.')