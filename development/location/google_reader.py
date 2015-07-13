

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

#Load the grid - this can be done piecewise, but f it, let's do it all at once
#g(df["latitude"],df["longitude"])


print "Generating image..."
from locimage import LocationImageMaker

l = LocationImageMaker()
for i in reversed(xrange(400000)):
    g([df["latitude"][i],],[df["longitude"][i],])
    n = g.getNode(df["latitude"][i],df["longitude"][i])
    if n>=0:
        l(df["timestamp"][i],n)
print "Done generating"
def sigm(s):
    return 1/(1+exp(-s))
plot(sigm(l.currentvector[:l.currentnodes]))
show()