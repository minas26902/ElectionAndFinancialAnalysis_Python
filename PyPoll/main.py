#Import dependencies
import os
import csv
from collections import Counter

#User will be prompted to add a file to be analyzed - example: election_data_1.csv or election_data_2.csv
file_input = input("Which file would you like to analyze? ") 

#Create file path
csvpath = os.path.join('raw_data',file_input)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')  
    #print (csvreader)
    
    #Checked first line for headers; added "break" so that the entire file is not printed
    #If the for statement below is added, the header is skipped and there is no need to add the next statement. Why?
    #for row in csvreader:
        #print (row)
        #break

    #Next function skips the header row so that it is not counted 
    next(csvreader, None) 
    
    #Set variables
    total_votes =[] 
    candidates = [] 

    #Calculate total number of votes cast and create list of candidates
    for row in csvreader:
        total_votes.append(row[0])    
        candidates.append(row[2])

    #print (len(total_votes))
    #print (len(candidates))

    #The total number of votes each candidate won 
    tallied_votes= Counter()
    for votes in candidates:
        tallied_votes[votes] += 1    
        new_tallied_votes = dict(tallied_votes) #not sure how to handle data in counter so I converted it into a dictionary
    #print (new_tallied_votes)

    #The percentage of votes each candidate won - (number of votes/ total_votes)*100
        percent_votes_won = {}
        for i,j in new_tallied_votes.items():
            percent_votes_won[i] = (j/int(len(total_votes))*100)
            
    #The winner of the election based on popular vote - use max dictionary function
        winner = max(percent_votes_won, key=percent_votes_won.get)
    #print (percent_votes_won)   
    #print (winner)
    
    #Convert dictionary keys and values into lists to call these to print
    keys1=list(new_tallied_votes.keys())
    values1=list(new_tallied_votes.values())
    values2=list(percent_votes_won.values())

    #print (keys1)
    #print (values1)
    #print (values2)
    
    #Print analysis to terminal
    print (" ")
    print ('Election Results')
    print ("------------------------------------")
    print ("Total Votes: " + str(len(total_votes)))
    print ("------------------------------------")
    for index in range(len(keys1)):
            print (keys1[index] +":" + " " + str(round(values2[index],1)) + "%" + " " + str(values1[index]))
    print ("------------------------------------")
    print ("Winner: " + winner)
    print ("------------------------------------")              

#Export results into a text file - MAKE SURE TO GIVE A DIFFERENT FILE NAME FOR EACH SUMMARY OUTPUT
import sys
sys.stdout = open('election_results.txt','wt')
print (" ")
print ('Election Results')
print ("------------------------------------")
print ("Total Votes: " + str(len(total_votes)))
print ("------------------------------------")
for index in range(len(keys1)):
    print (keys1[index] +":" + " " + str(round(values2[index],1)) + "%" + " " + str(values1[index]))
print ("------------------------------------")
print ("Winner: " + winner)
print ("------------------------------------")  