
import os
import csv


# Read data from the CSV file
dates = []
profits_losses = []

with open('Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate total number of months
total_months = len(dates)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# Calculate changes in "Profit/Losses" and the average of those changes
changes = [profits_losses[i] - profits_losses[i - 1] for i in range(1, len(profits_losses))]
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits (date and amount)
greatest_increase_amount = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase_amount) + 1]

# Find the greatest decrease in profits (date and amount)
greatest_decrease_amount = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease_amount) + 1]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Export the results to a text file
with open('financial_analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${average_change:.2f}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")