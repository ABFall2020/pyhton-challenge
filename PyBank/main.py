import os

import pandas as pd

import csv
file_path = "./Resources/budget_data.csv"
df = pd.read_csv(file_path)

# Calculate total number of months
total_months = len(df)

# Calculate net total amount of "Profit/Losses"
net_total = df["Profit/Losses"].sum()

# Calculate changes in "Profit/Losses" and the average of those changes
df["Profit/Losses Change"] = df["Profit/Losses"].diff()
average_change = df["Profit/Losses Change"].mean()

# Find the greatest increase and decrease in profits
greatest_increase = df[df["Profit/Losses Change"] == df["Profit/Losses Change"].max()]
greatest_decrease = df[df["Profit/Losses Change"] == df["Profit/Losses Change"].min()]

# Extract date and amount for greatest increase and decrease
greatest_increase_date = greatest_increase.iloc[0]["Date"]
greatest_increase_amount = greatest_increase.iloc[0]["Profit/Losses Change"]

greatest_decrease_date = greatest_decrease.iloc[0]["Date"]
greatest_decrease_amount = greatest_decrease.iloc[0]["Profit/Losses Change"]

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Create a directory for the analysis if it doesn't exist
output_folder = "analysis"
os.makedirs(output_folder, exist_ok=True)

# Specify the file path for the output file
output_file_path = os.path.join(output_folder, "financial_analysis.txt")

# Open a file for writing
with open(output_file_path, "w") as file:
    # Write the results to the file
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${net_total}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

# Print a message indicating successful export
print(f"Financial analysis results have been exported to '{output_file_path}'")