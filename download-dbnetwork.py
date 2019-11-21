#!/home/mzamith/Apps/anaconda3/bin/python

# pip install requests
import pandas as pd
import requests
import io
import sys
import mysql.connector


url = 'https://www.dcc.ufrrj.br/ocupationdb/exportMAC.php'
myobj = {'day': '2019-11-20'}

myrequest = requests.post(url, data = myobj)
if myrequest.ok:
    data = myrequest.content.decode('utf8')
    df = pd.read_csv(io.StringIO(data))
else:
    print("Error on web server - file not loaded", file=sys.stderr)
    exit(0)

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd="",
  database="dbNetwork"
)

mycursor = mydb.cursor()
sql = "INSERT INTO tbDeviceAddr (addr, vendor) VALUES (%s, %s)"
for i in range(0, len(df)-1):
    myaddr = df['addr'][i]
    myvendor = df['vendor'][i]
    val = (str(myaddr), str(myvendor))
    mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

#print the response text (the content of the requested file):
#addr, date_time, device_signal, device_id, pack_type
#print(len(df))
#print(df['addr'][0])
#print(df['vendor'][0])
