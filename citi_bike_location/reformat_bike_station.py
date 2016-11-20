import csv
#read the csv file skipping header
csvrows=[]
with open('citibike-tripdata-201504.csv',newline='') as usage1504:
    citi_readerobj=csv.reader(usage1504)
    for row in citi_readerobj:
        if citi_readerobj.line_num==1:
            continue
        csvrows.append(row)
#create a csv on arrival/departure info
reform1504=open('citibike_reform_201504.csv','w',newline='')
citi_writerobj=csv.DictWriter(reform1504,fieldnames=['Datetime',
    'interval','weekday','station id',
      'arrival','departure'])
citi_writerobj.writeheader()
#create a csv pair station id with lat/lon
reform_loc=open('citibike_station.csv','w',newline='')
loc_writeobj=csv.DictWriter(reform_loc,fieldnames=['station id','lat','lon'])
loc_writeobj.writeheader()
stations=set([])
for i in range(0,len(csvrows)-1):
    if csvrows[i][3] not in stations:
        stations.add(csvrows[i][3])
        loc_writeobj.writerow({'station id':csvrows[i][3],
                                'lat':csvrows[i][5],'lon':csvrows[i][6] })
stations.clear()








