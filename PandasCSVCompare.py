import csv
import pandas as pd
import sys

with open('/Users/apeterson/Downloads/CommonNameIssuedCerts.csv', 'r') as csv1, open('/Users/apeterson/Downloads/CNsSplunkCHHQ1.csv', 'r') as csv2:  # Import CSV files
    import1 = csv1.readlines()
    import2 = csv2.readlines()

# Create CSV file with differences
with open('/Users/apeterson/Downloads/data_diff.csv', 'w') as outFile:
    for row in import2:
        if row not in import1:
            outFile.write(row)





# csvoutfile = open("filelocation.csv", 'wt', encoding='utf8',newline='')
# outFile = csv.writer(csvoutfile, delimiter=",")



# f = open("outputfile.csv", 'rt')

# reader = csv.reader(f,delimiter=',')

# for row in reader:
#                 if 'year' in row[1]:
#                                 print (row[0])
#                                 outFile.writerow(row)
#                 else:
#                                 print ("No 'Year' listed in line.")