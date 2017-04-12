import csv
import sys
 
csvoutfile = open("C:/Users/apeterson/Desktop/uptime output.csv", 'wt', encoding='utf8',newline='')
outFile = csv.writer(csvoutfile, delimiter=",")
 
f = open("C:/Users/apeterson/Desktop/uptimeUpdated1.csv", 'rt')
 
reader = csv.reader(f,delimiter=',')
 
for row in reader:
                if 'year' in row[1]:
                                print (row[0])
                                outFile.writerow(row)
                else:
                                print ("No 'Year' listed in line.")
