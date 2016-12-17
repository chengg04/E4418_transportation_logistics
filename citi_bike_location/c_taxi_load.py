'''
A file that loads yellow cab data to sql
'''

import sqlite3
import csv
from datetime import datetime

start_time=datetime.now()
# with open('green_tripdata_201504.csv') as g, sqlite3.connect('green_taxi.sqlite') as gsql:
#     reader_g=csv.reader(g)
#     next(reader_g)
#     c_g=gsql.cursor()
#     c_g.execute('drop table green')
#     c_g.execute('''create table if not exists green (VendorID,lpep_pickup_datetime,Lpep_dropoff_datetime,Store_and_fwd_flag,
# RateCodeID,Pickup_longitude,Pickup_latitude,Dropoff_longitude,Dropoff_latitude,Passenger_count,
# Trip_distance,Fare_amount,Extra,MTA_tax,Tip_amount,Tolls_amount,Ehail_fee,improvement_surcharge,Total_amount,Payment_type,Trip_type,none1,none2
# )''')
#     c_g.executemany('insert into green values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',reader_g)
#     gsql.commit()
#     gsql.close
with open('yellow_tripdata_201504.csv') as y, sqlite3.connect('green_taxi.sqlite') as gsql:
    reader=csv.reader(y)
    next(reader)
    c_g=gsql.cursor()
    c_g.execute('''create table if not exists yellow (VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,
passenger_count,trip_distance,pickup_longitude,pickup_latitude,RateCodeID,store_and_fwd_flag,dropoff_longitude,
dropoff_latitude,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount
)''')
    c_g.executemany('insert into yellow values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',reader)
    gsql.commit()
    gsql.close
print(datetime.now()-start_time)