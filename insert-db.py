#!/home/mzamith/Apps/anaconda3/bin/python

# pip install requests
import pandas as pd
import io
import sys
import mysql.connector


#---------------------------------------------------------------------------------------------------------------
file = "/home/mzamith/matrix/occupation/" + sys.argv[1]
print("Load csv file: ", file)

df = pd.read_csv(file)
print("Number of records: ", str(len(df)))
print("Connect to DB")
mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd="",
  database="dbNetwork"
)
mycursor = mydb.cursor()
sql = "INSERT INTO tbNetworkRecord_v2 (MAC, date_time, device_signal, location, pack_type) VALUES (%s, %s, %s, %s, %s)"
print("Inserting....")
for i in range(0, len(df)-1):
    mymac = df.iloc[i, 0]
    mydate = df.iloc[i, 1]
    mysignal = df.iloc[i, 2]
    mylocation = df.iloc[i, 3]
    mytype = df.iloc[i, 4]
    val = (str(mymac), str(mydate), str(mysignal), str(mylocation), str(mytype))
    mycursor.execute(sql, val)

mydb.commit()
print("Record inserted.")

"""

print("Insert to DB")
mycursor = mydb.cursor()
sql = "INSERT INTO tbNetworkRecord_v2 (addr, date_time, device_signal, location, pack_type) VALUES (%s, %s, %s, %s, %s)"
for i in range(0, len(df)-1):
    myaddr = df.iloc[i, 0]
    mydate = df.iloc[i, 1]
    mysignal = df.iloc[i, 2]
    mylocation = df.iloc[i, 3]
    mytype = df.iloc[i, 4]

    val = (str(myaddr), str(mydate), str(mysignal), str(mylocation), str(mytype))
    mycursor.execute(sql, val)

mydb.commit()
print("Record inserted.")

#print the response text (the content of the requested file):
#addr, date_time, device_signal, device_id, pack_type
#print(len(df))
#print(df['addr'][0])
#print(df['vendor'][0])
"""