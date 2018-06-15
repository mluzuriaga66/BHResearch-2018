
# coding: utf-8

# In[4]:
import pynbody
import matplotlib.pylab as plt
plt.switch_backend("agg")

#im loading the snapshot
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')   

#loading the halo aka galaxy
h = s.halos()
h2=h[2]

#halo/galaxy we need to look at is no. 2
pynbody.analysis.angmom.faceon(h2)

#converting into useful units
s.physical_units()

#this centers h2
pynbody.analysis.halo.center(h2, mode='hyb')

#function to find the black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

#defining black hole
BH = findBH(s)

#prints the black hole
print BH

#this is the position of black hole
BHposition=BH['pos']

#printing the position of black hole
print BHposition

#putting the x-values into a column
BHx= BHposition[:,0]
print BHx

#putting the y-values into a column
BHy= BHposition[:,1]
print BHy

#putting the z-values into a column
BHz= BHposition[:,2]
print BHz

#distance function
#def distance

#the .5 is the square root , this is the distance formula
distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
print distance
