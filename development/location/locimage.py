from pylab import *
import theano

class LocationImageMaker(object):
    def __init__(self,timedecay=1./(60.*60.*10)):
        self.timedecay = timedecay
        self.currentnodes = 0
        self.currentvector = zeros(1000, dtype=theano.config.floatX)
        self.curtime = 0.0
    def __call__(self,t,i):
        if i >= len(self.currentvector):
            raise AssertionError("Assumed that less than 1000 nodes!")
        #We have a new timestamp at t with index i
        if i >= self.currentnodes:
            self.currentnodes = i +1
        self.currentvector *= 1./exp(self.timedecay*(t-self.curtime))
        val = (t-self.curtime)/(60.*60.)
        if val > 1:
            val = 1
        self.currentvector[i] += val
        self.curtime = t
        return self.currentvector[:self.currentnodes]