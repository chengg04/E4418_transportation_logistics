import csv

bikeinfo_rows=[]
with open ('citibike_reform_201504.csv',newline='') as bike_reform:
    bikereform_obj=csv.reader(bike_reform)
    for row in bikereform_obj:
        if bikereform_obj.line_num==1:
            continue
        bikeinfo_rows.append(row)
starows=[]
with open('citibike_station.csv',newline='') as station:
    station_reader=csv.reader(station)
    for row in station_reader:
        if station_reader.line_num==1:
            continue
        starows.append(row)

reformclu=open('reform_cluster.csv','w',newline='')
clu_obj=csv.DictWriter(reformclu,fieldnames=['lat','lon',
      'pick','drop'])
clu_obj.writeheader()

#the pickup/dropoff for 8-10am(4th interval) of April 15th 2015
for i in range(len(starows)):
    clu_obj.writerow({'lat':starows[i][1],'lon':starows[i][2],
                      'pick':bikeinfo_rows[14*12*327+3*327+i][4],
                      'drop':bikeinfo_rows[14*12*327+3*327+i][5]})


