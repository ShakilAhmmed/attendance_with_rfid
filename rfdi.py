import serial 
import mysql.connector
import time

#establish connection to MySQL. You'll have to change this for your database.
db =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rfid_read"

)
#open a cursor to the database
connect = db.cursor()

device = '/dev/ttyACM0' #this will have to be changed to the serial port you are using
try:
  print("Trying...",device)
  arduino = serial.Serial(device, 9600)
  print("Connected")
except: 
  print("Failed to connect on",device)
while True:
    time.sleep(1)
    try:
        data=arduino.readline()
        pieces=data.decode("utf-8").split()
        print(pieces)
        try:
            insert_sql = "INSERT INTO attendances(Member_ID,allowed_members) VALUES(%s,%s)"
            value = (pieces[0], pieces[1])
            connect.execute(insert_sql, value)
            db.commit()
        except:
            print("failed to insert data")
        finally:
            cursor.close()
    except:
        print("Processing")
    