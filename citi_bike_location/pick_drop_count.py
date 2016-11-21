import csv
#import re
import pandas as pd
from reformat_datatime import starows

csvrows=[]
with open('citibike-tripdata-201504.csv',newline='') as usage1504:
    citi_readerobj=csv.reader(usage1504)
    for row in citi_readerobj:
        if citi_readerobj.line_num==1:
            continue
        csvrows.append(row)
row_num=30*12*len(starows)
picklist=[0]*row_num
droplist=[0]*row_num
#create a list of strings representing hours
hourlist=[]
for i in range(10):
    hourlist.append('0%d'% i)
for i in range(10,24):
    hourlist.append('%d'% i)
#count picks and drops
for i in range(csvrows):
    rawday=csvrows[i][1][2]
    rawhour=csvrows[i][1][9]+csvrows[i][1][10]
    for j in range(30):
        if '4/%d/2015'% (j+1) in csvrows[i][1]:
            for k in range(24):
            for t in range(starows):

                    if '%s:'% hourlist[k] in csvrows[i][1]:
                        if
                            picklist[]





