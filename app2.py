import joblib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import serial
import time




cred=credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL': "https://staffattendance-89417-default-rtdb.firebaseio.com/ "})

category=""
db_ref=db.reference(category)
current_datetime=datetime.datetime.now()
#date=current_datatime,strftime('%Y-%m-%d')
#print("formatted date:",date)
year = current_datetime.strftime('%Y')
month =current_datetime.strftime('%m')
day = current_datetime.strftime('%d')
print("Year:", year)
print("Month:", month)
print("Day:", day)
flow1=m
flow2=n
rf1=1.2
rf2=1.3

model = joblib.load('rf_model.joblib')
input_data1 = [[day, month, year,flow1,rf1]]
input_data2 = [[day, month, year,flow2,rf2]]
level1 = model.predict(input_data1)
level2= model.predict(input_data2)
print("level1=",level1)
print("level1=",level2)
db_ref.update({
    'date1':f'"{day}"',
    'month1':f'"{month}"',
    'year1':f'"{year}"',
    'flow1':f'"{flow1}"',
    'rainflow1':f'"{rf1}"',
    'date2':f'"{day}"',
    'month2':f'"{month}"',
    'year2':f'"{year}"',
    'flow2':f'"{flow2}"',
    'rainflow2':f'"{rf2}"',
    'level1':f'"{level1}"',
    'level2':f'"{level2}"',

    

    })


