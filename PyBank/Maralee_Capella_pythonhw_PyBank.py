
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

numberofmonths = 0
totalprofit = 0
totalchange=0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        numberofmonths = numberofmonths + 1
        totalprofit = totalprofit + int(row[1])
      
        if numberofmonths>1: 
            change= int(row[1])- int(lastrow[1])
            totalchange= totalchange + change
            
        if numberofmonths==2:
            greatest_change= change
            month_great= row[0]
            lowest_change = change
            month_low= row[0]
        if numberofmonths>2:
            if change> greatest_change:
                greatest_change=change
                month_great=row[0]
            if change < lowest_change:
                lowest_change=change
                month_low=row[0]

 
        lastrow=row


print("total months:" , numberofmonths)
print("total profit:", "$" + str(totalprofit))
print("average change:" , "$" + str(totalchange/ (numberofmonths -1)))  
print("greatest increase in profits:", month_great, "$"+str(greatest_change))
print("greatest decrease in profits:",month_low, "$"+ str(lowest_change))

with open("Output.txt", "w") as text_file:
    
    text_file.write("total months:" +str(numberofmonths))
    text_file.write("\n")
    text_file.write("total profit:"+ "$" + str(totalprofit))
    text_file.write("\n")
    text_file.write("average change:" + "$" + str(totalchange/ (numberofmonths -1)))  
    text_file.write("\n")
    text_file.write("greatest increase in profits:"+ month_great+" "+ "$"+str(greatest_change))
    text_file.write("\n")
    text_file.write("greatest decrease in profits:"+month_low+" "+ "$"+ str(lowest_change))
    text_file.write("\n")


