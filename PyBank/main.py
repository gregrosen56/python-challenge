#done using pandas for convenience
import pandas as pd
import csv

with open ("budget_data_1.csv") as file1:
    csv1 = pd.read_csv(file1)
    row_count1 = len(csv1.index)           #total number of months
    total1 = csv1['Revenue'].sum()         #sum of total revenue
    csv1['Diffs'] = csv1['Revenue'].diff() #calculate month-over-month change
    avg1 = round(csv1["Diffs"].mean())     #average of month-over-month change
    max1 = csv1["Diffs"].max()             #maximum month-over-month increase
    min1 = csv1["Diffs"].min()             #largest month-over-month DECREASE

#sort data to retrieve month of largest revenue decrease
csv1_sorted = csv1.sort_values("Diffs")
csv1_sorted = csv1_sorted.reset_index(drop=True)
mindate1 = csv1_sorted["Date"].loc[0]

#flip sorting to get the month of maximum revenue increase
csv1_sorted = csv1.sort_values("Diffs", ascending=False)
csv1_sorted = csv1_sorted.reset_index(drop=True)
maxdate1 = csv1_sorted["Date"].loc[0]

#print findings
print("Financial Analysis (1)")
print("--------------------------------------------------------------")
print("Total Months: " + str(row_count1))
print("Total Revenue: $" + str(total1))
print("Average Revenue Change: $" + str(avg1))
print("Greatest Increase in Revenue: " + str(maxdate1) + " ($" + str(max1) + ")")
print("Greatest Decrease in Revenue: " + str(mindate1) + " ($" + str(min1) + ")")

#export print to text file
f = open('Results_1.txt','w')
f.write("Financial Analysis (1)" + '\n' +
        "--------------------------------------------------------------" + '\n' +
        "Total Months: " + str(row_count1) + '\n' +
        "Total Revenue: $" + str(total1) + '\n' +
        "Average Revenue Change: $" + str(avg1) + '\n' +
        "Greatest Increase in Revenue: " + str(maxdate1) + " ($" + str(max1) + ")" + '\n' +
        "Greatest Decrease in Revenue: " + str(mindate1) + " ($" + str(min1) + ")" + '\n'
       )
f.close()

#begin analysis of SECOND spreadsheet
with open ("budget_data_2.csv") as file2:
    csv2 = pd.read_csv(file2)
    row_count2 = len(csv2.index)           #total number of months
    total2 = csv2['Revenue'].sum()         #sum of total revenue
    csv2['Diffs'] = csv2['Revenue'].diff() #calculate month-over-month change
    avg2 = round(csv2["Diffs"].mean())     #average of month-over-month change
    max2 = csv2["Diffs"].max()             #maximum month-over-month increase
    min2 = csv2["Diffs"].min()             #largest month-over-month DECREASE

#sort data to retrieve month of largest revenue decrease
csv2_sorted = csv2.sort_values("Diffs")
csv2_sorted = csv2_sorted.reset_index(drop=True)
mindate2 = csv2_sorted["Date"].loc[0]

#flip sorting to get the month of maximum revenue increase
csv2_sorted = csv2.sort_values("Diffs", ascending=False)
csv2_sorted = csv2_sorted.reset_index(drop=True)
maxdate2 = csv2_sorted["Date"].loc[0]

#print findings
print("")
print("Financial Analysis (2)")
print("--------------------------------------------------------------")
print("Total Months: " + str(row_count2))
print("Total Revenue: $" + str(total2))
print("Average Revenue Change: $" + str(avg2))
print("Greatest Increase in Revenue: " + str(maxdate2) + " ($" + str(max2) + ")")
print("Greatest Decrease in Revenue: " + str(mindate2) + " ($" + str(min2) + ")")

#export print to text file
f = open('Results_2.txt','w')
f.write("Financial Analysis (2)" + '\n' +
        "--------------------------------------------------------------" + '\n' +
        "Total Months: " + str(row_count2) + '\n' +
        "Total Revenue: $" + str(total2) + '\n' +
        "Average Revenue Change: $" + str(avg2) + '\n' +
        "Greatest Increase in Revenue: " + str(maxdate2) + " ($" + str(max2) + ")" + '\n' +
        "Greatest Decrease in Revenue: " + str(mindate2) + " ($" + str(min2) + ")" + '\n'
       )
f.close()