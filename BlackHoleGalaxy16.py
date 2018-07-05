#Find All The Black Holes 

import pynbody
import numpy as np
import matplotlib.pylab as plt

#im loading the snapshot of the simulation
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

#turns the numbers into useful units
s.physical_units()

#loading the halo aka galaxy
h = s.halos()

#function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print BH

#function to find the halos that the galaxy is in
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

#using the function the halos
BHhalos = findBHhalos(s)

#printing the halos
print BHhalos

#sorting the halos, indexes/indecis are like an exact address
currenthalo = np.argsort(halos)
print halos[currenthalo]

for i in currenthalo:

    #which halo are we on?
    currenthalo = halos[i]
    print 'current halo: ', currenthalo

    #put the galaxy you care about in the center of the simulation
    pnbody.analysus.angmom.faceon(h[currenthalo])
    with pynbody.analysis.halo.center(h[currenthalo], mode='hyb'):

#for halo in BHhalos:
#    halo/galaxy we need to look at is no. 2
#    pynbody.analysis.angmom.faceon(h[halo])
#    prints the black hole
#    print BH

    #this is the position of black hole
    BHposition=BH['pos']

    #printing the position of black hole
    print BHposition

    #putting the x-values into a column
    BHx= BHposition[i,0]
    print BHx

    #putting the y-values into a column
    BHy= BHposition[i,1]
    print BHy

    #putting the z-values into a column
    BHz= BHposition[i,2]
    print BHz

    #the .5 is the square root , this is the distance formula
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    #print 'this is the distance :'
    print distance
##
