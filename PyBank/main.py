#module import
#retreive budget_data.csv

import os
import csv
budgetdata = csv.reader(open('budget_data.csv'), delimiter=",")

#The total number of months included in the dataset

month_count = sum(1 for row in budgetdata) - 1

#The net total amount of "Profit/Losses" over the entire period

nettotal = sum(int(row["Profit/Losses"]) for row in budgetdata)

#The average of the changes in "Profit/Losses" over the entire period

    #average=nettotal/pl_count

#divide by number of rows
pl_count = sum(1 for row in budgetdata) - 1

#The greatest increase in profits (date and amount) over the entire period

minProfit = []
maxProfit = []

for row in budgetdata:
    print(row[1],row[2])
    minProfit.append(row[1])
    maxProfit.append(row[2])
print ("min value element : ", min(minProfit))
print ("max value element : ", min(maxProfit))

#The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("------------------")

#Total Months: 86
print(f"Total Months: {month_count}")

#Total: $38382578
print(f"${nettotal}")

#Average  Change: $-2315.12
    #print(f"{average}")

#Greatest Increase in Profits: Feb-2012 ($1926159)
    #print(f"Greatest Increase in Profits:{max}")
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
     #print(f"Greatest Decrease in Profits:{min}")
