#write date/time interval/weekday to csv
import csv
#creat a list about station information
starows=[]
with open('citibike_station.csv',newline='') as station:
    station_reader=csv.reader(station)
    for row in station_reader:
        if station_reader.line_num==1:
            continue
        starows.append(row)
#create a csv on arrival/departure info
reform1504=open('citibike_reform_201504.csv','w',newline='')
citi_writerobj=csv.DictWriter(reform1504,fieldnames=['date',
    'interval','weekday','station id',
      'pick','drop'])
citi_writerobj.writeheader() #to be removed
#creat a list on weekday info of april 2015
wday=[]
for i in range(30):
    if (i+1)%7==4 or (i+1)%7==5:
        wday.append(0) #if weekend, then 0
    else:
        wday.append(1)
#write down date, time interval, weekday, station id
for i in range(30):
    #12 time intervals a day, each contains 2 hours
    for k in range(12):
        #iterate through stations
        for j in range(len(starows)):
            citi_writerobj.writerow({'date':i+1,'interval':k+1,
                                     'weekday':wday[i], 'station id': starows[j][0],
                                   'pick': 0.0, 'drop': 0.0})





