#!/home/mzamith/Apps/anaconda3/bin/python

import sys
import mysql.connector
import matplotlib.pyplot as plt

#./graficos 2019-11-19 07:00:00 23:00:00
#retorna a quatidade de vezes que cada mac apareceu
#no intervalo de tempo definido

setMACs = []
setX = []
setY = []


mydate = sys.argv[1]
myITime = sys.argv[2]
myFTime = sys.argv[3]

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd="",
  database="dbNetwork"
)
mycursor = mydb.cursor()
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