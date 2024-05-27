import serial
import time
import joblib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

# Initialize Firebase Admin
cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://floodprediction-108b6-default-rtdb.firebaseio.com/"})

# Define the serial port and baud rate
serial_port = 'COM11'  # Change this to the correct port
baud_rate = 9600

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate)
print("Serial connection established.")

# Wait for Arduino to initialize
time.sleep(2)

# Load the model
model = joblib.load('rf_model.joblib')

try:
    while True:
        # Read data from Arduino
        data = ser.readline().decode().strip()
        
        # Split the data into separate values for each sensor
        sensor_data = data.split(',')
        
        # Parse and store data for each sensor
        for sensor_value in sensor_data:
            sensor_id, value = sensor_value.split(':')
            if sensor_id == '1':
                flow1 = float(value)
            elif sensor_id == '2':
                flow2 = float(value)

        # Get the current date and time
        current_datetime = datetime.datetime.now()
        day = current_datetime.strftime('%d')
        month = current_datetime.strftime('%m')
        year = current_datetime.strftime('%Y')

        # Prediction inputs
        rf1 = 1.2
        rf2 = 1.3
        input_data1 = [[day, month, year, flow1, rf1]]
        input_data2 = [[day, month, year, flow2, rf2]]
        
        # Make predictions
        level1 = model.predict(input_data1)
        level2 = model.predict(input_data2)

        # Print sensor data and predictions
        print("Sensor 1 data (m):", flow1, "L/min")
        print("Sensor 2 data (n):", flow2, "L/min")
        print("Predicted Level 1:", level1)
        print("Predicted Level 2:", level2)

        # Update Firebase database
        db_ref = db.reference("")
        db_ref.update({
            'date1': day,
            'month1': month,
            'year1': year,
            'flow1': flow1,
            'rainflow1': rf1,
            'level1': level1[0],
            'date2': day,
            'month2': month,
            'year2': year,
            'flow2': flow2,
            'rainflow2': rf2,
            'level2': level2[0]
        })

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()

