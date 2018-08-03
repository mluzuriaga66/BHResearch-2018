import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('elektra.dat',fsep=',')
BHID= files[:,1]
Time= files[:,2]
BHDistance= files[:,5]

ID=[227839049]
i1= np.where(BHID== 227839049)
#i2= np.where(BHID== 243778457)
#i3= np.where(BHID== 243771992)


plt.plot(Time[i1], BHDistance[i1], label= "Elektra Black Hole")
#plt.plot(Time[i2], BHDistance[i2], label= "Galaxy2a")
#plt.plot(Time[i3], BHDistance[i3], label= "Galaxy2b")



plt.legend()

#(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)

plt.ylabel("BH Distance 'Kpc'")
plt.xlabel("Time 'Gyr'")
plt.show()
