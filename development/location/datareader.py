import connectordb
import booltool
from pylab import *
import getpass

p =getpass.getpass()

cdb = connectordb.ConnectorDB("daniel",p)

print "Got ratings:", len(cdb["rating_productivity"])
prodratings = cdb["rating_productivity"][:]

#print prodratings

print "Have locations:",len(cdb.user["SM-N910V"]["location"])

locstream = cdb.user["SM-N910V"]["location"]

locvalues = locstream(prodratings[0]["t"],prodratings[-1]["t"])

print "Loaded locations:",len(locvalues)

vals = booltool.restamp(prodratings,locvalues)

print "Restamped:",len(vals)

from locationgrid import GridLocator

g = GridLocator(lat_step=0.0005,long_step=0.0005,numexist=1)

lat = []
long = []
for v in vals:
    lat.append(v["d2"]["latitude"])
    long.append(v["d2"]["longitude"])

g(lat,long)

#Now create the magic necessary for a linear fit
y = zeros(len(vals))
x = zeros((len(vals),len(g)))
for i in xrange(len(vals)):
    x[i,g.getNode(vals[i]["d2"]["latitude"],vals[i]["d2"]["longitude"])] = 1
    y[i] = vals[i]["d"]

print x
print y

from sklearn.linear_model import LinearRegression

reg = LinearRegression(fit_intercept=False)

reg.fit(x,y)

print "Fit complete"

for i in xrange(len(reg.coef_)):
    print reg.coef_[i]," ",g.getCoor(i)
