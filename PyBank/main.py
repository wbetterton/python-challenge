import os
import csv
import pandas as pd

csvpath = os.path.join("..","3 - Python","budget_data.csv")

csv_pandas_path = pd.read_csv("budget_data.csv")
df = pd.DataFrame(csv_pandas_path)
df["Difference"] = df["Profit/Losses"].diff(1)

decrease = csv_pandas_path["Difference"].min()
increase = csv_pandas_path["Difference"].max()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvtotal = csv.DictReader(csvfile)
    
    month_count = len(list(csv.reader(open(csvpath))))
    
    total = sum(float(row["Profit/Losses"]) for row in csvtotal)
    
    average = str(round(total / (month_count - 1)))
    
  print("Financial Analysis")
print("------------------")
print("Total Months: " + str(month_count - 1))
print("Total: $" + str(total))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(increase))
print("Greatest Decrease in Profits: " + str(decrease))