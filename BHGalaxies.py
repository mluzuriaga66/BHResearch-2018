#saving file
import pynbody
import matplotlib.pylab as plt
plt.switch_backend("agg")

#im loading the snapshot
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

#turns the numbers into useful units
s.physical_units()

#loading the halo aka galaxy
h = s.halos()

#function to find black hole
def findBH(snap):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = snap.stars[BHfilter]
    return BH

#function to find the halos that the galaxy is in
def findBHhalos(snap):
    BH = findBH(snap)
    BHhalos = BH['amiga.grp']
    return BHhalos

#using the function the halos
BHhalos = findBHhalos(s)

#printing the halos
print BHhalos

for halo in BHhalos:
    #halo/galaxy we need to look at is no. 2
    pynbody.analysis.angmom.faceon(h[halo])
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
    #the .5 is the square root , this is the distance formula
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    print 'this is the distance :'
    print distance
