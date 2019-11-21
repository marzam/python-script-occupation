#!/home/mzamith/Apps/anaconda3/bin/python

# pip install requests
import pandas as pd
import requests
import io
import sys
import mysql.connector

print("1")
df = pd.read_csv(r'export_dataframe.csv', encoding='utf-8-sig')

myaddr = df.iloc[0,0]
mydate = df.iloc[0,1]
mysignal = df.iloc[0,2]
mylocation = df.iloc[0,3]
mytype =  df.iloc[0,4]

print( mydate)
#print(list(df))
#print the response text (the content of the requested file):
#addr, date_time, device_signal, device_id, pack_type
#print(len(df))
#print(df['addr'][0])
#print(df['vendor'][0])
