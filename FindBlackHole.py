
# coding: utf-8

# In[4]:


import pynbody
import matplotlib.pylab as plt
plt.switch_backend("agg")

#im loading the snapshot
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')   


#loading the halo aka galaxy
h = s.halos()

#halo/galaxy we need to look at is no.2
pynbody.analysis.angmom.faceon(h[2])

#turns the numbers into useful units
s.physical_units()

#finding the black hole using function
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
#defining that Black Hole is the function above
BH = findBH(s)

#prints the black hole
print ('BH')

#finding what is the radius of the Black Hole at that time
pynbody.analysis.halo.center(h[2],mode='hyb')

#this centers h2
with pynbody.analysis.halo.center(h[2], mode='hyb'):
    print(h[2]['pos'][0])
    print(h[2]['pos'][1])
    print(h[2]['pos'][2])


cen_hyb = pynbody.analysis.halo.center(h[2],mode='hyb',retcen=True)
print(cen_hyb)
