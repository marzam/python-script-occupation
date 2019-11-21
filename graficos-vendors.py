#!/home/mzamith/Apps/anaconda3/bin/python

import sys
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

#./graficos 2019-11-19 07:00:00 23:00:00
#retorna a quatidade de vezes que cada mac apareceu
#no intervalo de tempo definido

def getVendorFromMAC(mac_address):
    url = "https://macvendors.co/api/"+mac_address+":00:00:00/csv"
    df = pd.read_csv(url)
    ret = "unknown"
    if len(df.columns) > 1:
        ret = str(df.columns[0])

    return ret;
#---------------------------------------------------------------------------------------------------------------


setMACs = []
setX = []
setY = []


mydate = "2019-11-19"
myITime = "18:00:00"
myFTime = "19:00:00"
table = "tbNetworkRecord_v2"
location = "multimidia"
mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd="",
  database="dbNetwork"
)
mycursor = mydb.cursor()
sql  = "SELECT a.MAC as MAC, COUNT(a.MAC) as MACs FROM ( SELECT SUBSTR(MAC,1,8) AS MAC FROM tbNetworkRecord_v2 WHERE DATE(date_time)='";
sql += mydate + "' AND TIME(date_time) >= '";
sql += myITime + "' AND TIME(date_time) < '";
sql += myFTime + "' AND location='";
sql += location + "' AND pack_type <> '0008') AS a GROUP BY a.MAC ORDER BY MACs;";

mycursor.execute(sql)
table = mycursor.fetchall()
index = 1
total = 0
df = pd.DataFrame()
for i in range(0, len(table)):
    currMAC = table[i][0]
    freq = table[i][1]
    total += freq
    df = df.append({'prefix': currMAC, 'vendor': getVendorFromMAC(currMAC), 'freq': freq}, ignore_index=True)
    #data.append(currMAC, getVendorFromMAC(currMAC), freq)
    print("%s %64s %8d" % (currMAC, getVendorFromMAC(currMAC), freq))

df.to_csv("dados.csv")
""""

mycursor.execute("select MAC  from tbNetworkRecord_v2 group by MAC;")
MACs = mycursor.fetchall()
index = 1
for i in range(0, len(MACs)-1):
    currMAC = MACs[i][0]
    sql = " SELECT count(*) FROM tbNetworkRecord_v2 WHERE MAC='" + currMAC + "' AND DATE(date_time) = '" + mydate + "' AND TIME(date_time) >= '" + myITime + "' AND  TIME(date_time) < '" + myFTime + "';"
    mycursor.execute(sql)
    mycount = mycursor.fetchall()
    freq = mycount[0][0]
    print("%s %8d" %(currMAC,freq))
    if freq > 0:
        setMACs.append(currMAC)
        setX.append(index)
        setY.append(freq)
        index = index + 1
plt.bar(setX, setY, tick_label = setMACs,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()

"""