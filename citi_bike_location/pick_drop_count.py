import csv
import math
from datetime import datetime
#from reformat_datatime import starows,citi_writerobj
#len(starows)=278; with three cols
#from reformat_bike_station import csvrows
csvrows=[]
with open('citibike-tripdata-201504.csv',newline='') as usage1504:
    citi_readerobj=csv.reader(usage1504)
    for row in citi_readerobj:
        if citi_readerobj.line_num==1:
            continue
        csvrows.append(row)
starows=[]
with open('citibike_station.csv',newline='') as station:
    station_reader=csv.reader(station)
    for row in station_reader:
        if station_reader.line_num==1:
            continue
        starows.append(row)

row_num=30*12*len(starows)
#list of stations
sta_list=[]
for row in starows:
    sta_list.append(row[0])
#count picks and drops
picklist=[0]*row_num
droplist=[0]*row_num
for i in range(len(csvrows)):
    pick_sta=csvrows[i][3]
    if pick_sta in sta_list: #avoid error when a station is not in starows
        pick_ind=sta_list.index(pick_sta)
        dt=datetime.strptime(csvrows[i][1],"%m/%d/%Y %H:%M:%S")
        tt=dt.timetuple()
        pick_day=tt.tm_mday
        pick_hour=tt.tm_hour
        pick_int=math.floor(pick_hour/2)#transform hour to time interval
        ind1=(pick_day-1)*12*len(starows)+pick_int*len(starows)+pick_ind
        picklist[ind1]=picklist[ind1]+1
    else:
        continue
    #do the same for drop-off data
    drop_sta=csvrows[i][7]
    if drop_sta in sta_list: #avoid error when a station is not in starows
        drop_ind=sta_list.index(drop_sta)
        dt=datetime.strptime(csvrows[i][2],"%m/%d/%Y %H:%M:%S")
        tt=dt.timetuple()
        drop_day=tt.tm_mday
        drop_hour=tt.tm_hour
        drop_int=math.floor(drop_hour/2)#transform hour to time interval
        ind2=(drop_day-1)*12*len(starows)+drop_int*len(starows)+drop_ind
        droplist[ind2]=droplist[ind2]+1
    else:
        continue
#write pick/drop in the csv
#reform1504=open('citibike_reform_201504.csv','w',newline='')
#citi_writerobj.writeheader()
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
                                   'pick': picklist[i*12*len(starows)+k*len(starows)+j], 'drop': droplist[i*12*len(starows)+k*len(starows)+j]})





