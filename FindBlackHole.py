
# coding: utf-8

# In[4]:
import pynbody
import matplotlib.pylab as plt
plt.switch_backend("agg")

#im loading the snapshot
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')   

<<<<<<< HEAD
=======
#turns the numbers into useful units
s.physical_units()

>>>>>>> 150158bb83fa86d3388a4b396c35fa8a08861c6f
#loading the halo aka galaxy
h = s.halos()
h2=h[2]

#halo/galaxy we need to look at is no. 2
pynbody.analysis.angmom.faceon(h2)

<<<<<<< HEAD
#converting into useful units
s.physical_units()
=======
#this centers h2
with pynbody.analysis.halo.center(h[2], mode='hyb'):
    print(h[2]['pos'][0])
    print(h[2]['pos'][1])
    print(h[2]['pos'][2])
    
print ('pos')    
>>>>>>> 150158bb83fa86d3388a4b396c35fa8a08861c6f

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

<<<<<<< HEAD
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
=======
#forgot what this is for
#cen_hyb = pynbody.analysis.halo.center(h[2],mode='hyb',retcen=True)
#print(cen_hyb)
>>>>>>> 150158bb83fa86d3388a4b396c35fa8a08861c6f
