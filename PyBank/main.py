#Import dependencies
import os
import csv

#Create file path
#To get this path to be recognized I need to start inside of the raw_data directory

#User will be prompted to add a file to be analyzed - example: budget_data_1.csv or budget_data_2.csv
file_input = input("Which file would you like to analyze? ")
csvpath = os.path.join('raw_data',file_input)


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')  
    print (csvreader)

    #Skips the header row
    next(csvreader, None) 
    
    total_months =[]
    total_revenue = []
    rev_dif = []
    max_dif= []
    min_dif= []

    #Calculate total months and total revenue in for loop:
    for row in csvreader:
        total_months.append(row[0])
        total_revenue.append(float(row[1]))

    new_total_months = len(total_months)
    new_total_revenue = sum(total_revenue)
       
    print ("")
    print ('Financial Analysis')
    print ("------------------------------------")
    print ("Total Months: " + str(new_total_months))
    print ("Total Revenue: " + "$ " + str(new_total_revenue))

    
    #Begin iteration through csv file, and skip header using next function again? NOT NECESSARY
    #csvfile.seek(0)
    #next(csvreader, None) 
        
    #Create another for loop to calculate avg change, max and min change
    
    for i in range (1,len(total_revenue)):
        
        #Calculate the change in revenue between months and the average change in revenue over the entire period
        rev_dif.append(total_revenue[i] - total_revenue[i-1])
        avg_change = sum(rev_dif)/new_total_months
    #print (rev_dif)
    #print (new_total_months)
    #print (avg_change)


        #Find the greatest increase in revenue (date and amount) over the entire period
        max_dif = max (rev_dif)
        
        #Find the greatest decrease in revenue (date and amount) over the entire period
        min_dif = min (rev_dif)
    #print (max_dif)
    #print (min_dif)
       
       #Find index for max_dif and apply to total_months list to find corresponding month. Do the same for min_dif. DOUBLE CHECK THESE AS MONTHS
       #APPEAR TO BE OFF BY ONE? CHANGE STARTING i value?
        max_month= total_months[rev_dif.index(max_dif)]
   
        min_month= total_months[rev_dif.index(min_dif)]
    #print (max_month)
    #print (min_month)
    
    print ("Average Revenue Change: " + "$ " + str (round (avg_change, 1)))
    print ("Greatest Increase in Revenue: " + "$ " + str(max_month) + " " + (str(max_dif)))
    print ("Greatest Decrease in Revenue: " + "$ " + str(min_month) + " " + (str(min_dif)))
    print ("------------------------------------")

#Export a txt file with a summary output
import sys
sys.stdout = open('summary_output.txt','wt')
print ("")
print ('Financial Analysis')
print ("------------------------------------")
print ("Total Months: " + str(new_total_months))
print ("Total Revenue: " + "$ " + str(new_total_revenue))
print ("Average Revenue Change: " + "$ " + str(round (avg_change, 1)))
print ("Greatest Increase in Revenue: " + "$ " + str(max_month) + " " + (str(max_dif)))
print ("Greatest Decrease in Revenue: " + "$ " + str(min_month) + " " + (str(min_dif)))
print ("------------------------------------")

#Started out creating own functions, but then switched to using Python's built-in functions