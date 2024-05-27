import serial
import time

# Define the serial port and baud rate
serial_port = 'COM11'  # Change this to the correct port
baud_rate = 9600

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate)
print("Serial connection established.")

# Wait for Arduino to initialize
time.sleep(2)

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
                m = float(value)
            elif sensor_id == '2':
                n = float(value)

        # Print or use the stored data as needed
        print("Sensor 1 data (m):", m, "L/min")
        print("Sensor 2 data (n):", n, "L/min")

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()