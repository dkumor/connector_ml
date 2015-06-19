

history_path = "E:\\Backup\\rdkumor@gmail.com-20140711T145038Z-takeout\\rdkumor@gmail.com-20140711T145038Z-takeout\\Location History\\LocationHistory.json"
from pylab import *
from pandas import DataFrame
import json
import locationgrid

with open(history_path,"r") as f:
    data = json.loads(f.read())
print "done reading"

df = DataFrame(data["locations"])

df['latitude'] = df['latitudeE7']/1e7
df['longitude'] = df['longitudeE7']/1e7
df["timestamp"] = df["timestampMs"].astype(float64)/1000.

del df['latitudeE7']
del df['longitudeE7']
del df['timestampMs']


del df['accuracy']
del df['activitys']
del df['altitude']
del df['heading']
del df['velocity']


#Get the timestamps into neural format
#import timestamp
#ts = timestamp.Timestamper()
#print "timestamping"
#timestamps = ts(df["timestamp"])

print "Locating"
g = locationgrid.GridLocator()

g(df["latitude"],df["longitude"])


nz = g.nonzero()

with open("coormap.txt","w") as f:
    for i in xrange(len(nz[0])):
        v = g.coorToGPS(nz[0][i],nz[1][i])
        f.write(str(v[0])+","+str(v[1])+"\n")



