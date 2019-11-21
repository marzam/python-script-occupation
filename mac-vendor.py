#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
import pandas as pd

url = "https://macvendors.co/api/00:00:00:00:00:00/csv"
#url = "https://macvendors.co/api/00:B2:E8:00:00:00/csv"
df = pd.read_csv(url)
txt = str(len(df.columns))
print(txt)


#Fix: json object must be str, not 'bytes'
"""ret = "unknown"
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))
if (len(obj['result']) > 1):
    ret = obj['result']['company']
print (ret)

#print(ret)
#Print company name
#print (+"<br/>");

#print company address
#print (obj['result']['address']);

"""