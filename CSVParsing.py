import csv
import sys
 
csvoutfile = open("filelocation.csv", 'wt', encoding='utf8',newline='')
outFile = csv.writer(csvoutfile, delimiter=",")
 
f = open("outputfile.csv", 'rt')
 
reader = csv.reader(f,delimiter=',')
 
for row in reader:
                if 'year' in row[1]:
                                print (row[0])
                                outFile.writerow(row)
                else:
                                print ("No 'Year' listed in line.")
