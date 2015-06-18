import numpy
import datetime
import theano

class Timestamper(object):
    def __init__(self, nodes_per_day = 24, dayspread=0.3, nodes_per_week=7, week_spread=0.1, nodes_per_month=4,month_spread=0.05, nodes_per_year=12, year_spread = 0.1):
        #Set up the timestamper with the given data - weeks and months are defined by their spread.
        #The default is 47 nodes per timestamp. That is reasonable, I think
        self.nodes_per_day = nodes_per_day
        self.day_spread = dayspread
        self.nodes_per_week = nodes_per_week
        self.week_spread = week_spread
        self.nodes_per_month = nodes_per_month
        self.month_spread = month_spread
        self.nodes_per_year = nodes_per_year
        self.year_spread = year_spread


        self.total_length = nodes_per_day + nodes_per_week + nodes_per_month + nodes_per_year

        pass

    def writeDay(self,arr,dt):
        #Writes the time
        nodetime = len(arr)*(dt.hour + (dt.minute+(dt.second+1e-6*dt.microsecond)/60.)/60.)/24.

        return self.writeDist(arr,nodetime,self.day_spread)

    def writeWeek(self,arr,dt):
        weektime = len(arr)*(dt.weekday()+(dt.hour + (dt.minute+(dt.second+1e-6*dt.microsecond)/60.)/60.)/24.)/7.
        return self.writeDist(arr,weektime,self.week_spread)

    def writeMonth(self,arr,dt):
        dist = len(arr)*dt.day/31.
        return self.writeDist(arr,dist,self.month_spread)
    def writeYear(self,arr,dt):
        yeartime = len(arr)*(dt.month-1+dt.day/31.)/12.
        return self.writeDist(arr,yeartime,self.year_spread)

    def writeDist(self,arr,nodetime,spread=0.2):

        for i in xrange(len(arr)):
            dist = min(abs(nodetime-i),len(arr)-nodetime + i)
            arr[i] = spread**dist
        return arr


    def __call__(self,timestamp_array):
        result = zeros((len(timestamp_array),self.total_length),dtype=theano.config.floatX)
        for i in xrange(len(timestamp_array)):
            dt = datetime.datetime.utcfromtimestamp(timestamp_array[i])

if __name__=="__main__":
    from pylab import *
    ts = Timestamper()
    print ts.total_length
    
    figure()
    title("Day")
    plot(ts.writeDay(zeros(24),datetime.datetime.now()))
    show()
    figure()
    title("Week")
    plot(ts.writeWeek(zeros(7),datetime.datetime.now()))
    show()
    title("Month")
    plot(ts.writeMonth(zeros(4),datetime.datetime.now()))
    show()
    
    figure()
    title("Year")
    plot(ts.writeYear(zeros(12),datetime.datetime.now()))
    show()

