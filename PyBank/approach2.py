#import pandas module
import pandas as pd
import os

#make a reference to file path
budgetdata = "budget_data.csv"

#import .csv as data frame
budgetcsv = pd.read(budgetdata)
print(budgetcsv)

