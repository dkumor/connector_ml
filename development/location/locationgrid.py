import scipy.sparse
import numpy
from numpy.random import randn

def rand_gen(gen):
    return randn(gen)

class GridLocator(object):
    def __init__(self,lat_step = 0.003, long_step = 0.003,numexist=10,weightnum = 1,randgen=rand_gen):
        self.longsize = int(360./long_step)
        self.latsize = int(180./lat_step)
        self.weightnum=weightnum
        self.numexists = numexist
        self.randgen = randgen
        self.numgrid = scipy.sparse.lil_matrix((self.latsize,self.longsize),dtype=int)
        self.grid = scipy.sparse.lil_matrix((self.latsize,self.longsize),dtype=int)
        self.curint = 1
    def getGridCoordinate(self,lat,long):
        newlat = int(self.latsize * (lat + 90.)/180.)
        newlong = int(self.longsize * (long + 180)/360.)
        return (newlat,newlong)
    def coorToGPS(self,xcoor,ycoor):
        return (xcoor/float(self.latsize)*180.-90.,ycoor/float(self.longsize)*360.-180.)
    def __len__(self):
        return self.grid.getnnz()
    def nonzero(self):
        return self.grid.nonzero()

    def __call__(self,lat_array,long_array):
        for i in xrange(len(lat_array)):
            lat,long = self.getGridCoordinate(lat_array[i],long_array[i])
            self.numgrid[lat,long]+=1
            if self.numgrid[lat,long]==self.numexists:
                self.grid[lat,long] = self.curint
                self.curint +=1

    def getNode(self,lat,long):
        x,y = self.getGridCoordinate(lat,long)
        return self.grid[x,y]-1


if __name__=="__main__":
    g = GridLocator()
    a,b=g.getGridCoordinate(37.449664,-122.149896)
    print g.coorToGPS(a,b)