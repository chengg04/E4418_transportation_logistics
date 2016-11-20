#write date/time interval/weekday to csv
import csv
#create a csv on arrival/departure info
reform1504=open('citibike_reform_201504.csv','w',newline='')
citi_writerobj=csv.DictWriter(reform1504,fieldnames=['Datetime',
    'interval','weekday','station id',
      'arrival','departure'])
citi_writerobj.writerow('Datetime':)
