#!/usr/bin/python


import os
import csv
import codecs
import sys
import pandas as pd


csv.field_size_limit(sys.maxsize)

# Change date to Salesforce required format
def format_date(d):
    if d != "":
        return d[6:10]+'-'+d[3:5]+'-'+d[0:2]+'T'+d[12:20]+'.000Z'

# Field string limitation, used mainly for "Email body" cloumn
def cs(string):
    newstring = string[0:2000000]
    return newstring


# Read Email and Salesforce ID export from Salesforce
t = 0
with codecs.open("contact_id.csv", mode="r") as infile0:
    reader0 = csv.reader(infile0)
    mydict = {rows[0]: rows[1] for rows in reader0}

    # File to be chacked for email is "file.csv"; new column with ID matches email from "contact_id" file
    with open("file.csv", mode="r") as infile, open("newfile0.csv", mode="w") as outfile0, open("newfile1.csv", mode="w") as outfile1: 
        writer0 = csv.writer(outfile0, lineterminator=os.linesep, delimiter=',')
        writer1 = csv.writer(outfile1, lineterminator=os.linesep, delimiter=',')
        filereader = csv.reader(x.replace('\0','') for x in infile)

        print('Based on size of csv file it can take up to few minutes to finish, please be patient :) ')


        i = 0
        for row in filereader:
            if i == 0:
                row.append("Person__c")
                row.append("Incoming")
                row.append("Length")
                header = row

                writer0.writerow(header)
                i = i + 1
            else:
                if i < 10000:
                    from_email = row[2]
                    to_email = row[4]
                    
                    if from_email in mydict:
                        #print(mydict[from_email])
                        row.append(mydict[from_email])
                        row.append('true')
                        row[0] = format_date(row[0])
                        for x in range(1,11):
                            row[x] = cs(row[x])
                        row.append(len(row[8]))
                        if len(row[8]) > 120000:
                            t = t + 1
                        writer0.writerow(row)
                        i = i + 1  
                    else:
                        if to_email in mydict:
                            row.append(mydict[to_email])
                            row.append('false')
                            row[0] = format_date(row[0])
                            for x in range(1,11):
                                row[x] = cs(row[x])
                            row.append(len(row[8]))
                            if len(row[8]) > 120000:
                                t = t + 1
                            writer0.writerow(row)
                            i = i + 1

                # Devide new created file into two files if too many records
                else:
                    if i == 10000:
                        writer1.writerow(header)
                        i = i + 1
                    else:
                        from_email = row[2]
                        to_email = row[4]
                        
                        if from_email in mydict:
                            #print(mydict[from_email])
                            row.append(mydict[from_email])
                            row.append('true')
                            row[0] = format_date(row[0])
                            for x in range(1,11):
                                row[x] = cs(row[x])
                            row.append(len(row[5]))
                            writer1.writerow(row)
                            i = i + 1  
                        else:
                            if to_email in mydict:
                                row.append(mydict[to_email])
                                row.append('false')
                                row[0] = format_date(row[0])
                                for x in range(1,11):
                                    row[x] = cs(row[x])
                                row.append(len(cs(row[8])))
                                writer1.writerow(row)
                                i = i + 1




# VERIFICATION
df = pd.read_csv('newfile0.csv')
print(df.sort_values(['Length']))

print(header)

#print(pd.read_csv('newfile0.csv'))
#print(header)
