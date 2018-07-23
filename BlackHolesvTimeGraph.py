import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import readcol

#this is defining files to be the readcol 
files = readcol.readcol('testdata.txt')

#defining time and choosing to read the first column because that's where time is
time = files[:,0]
BHdistance = files[:,3]

#number of files
#nfiles = len(files)

#print 'this is time:', time
#print 'this is the distance:', BHdistance

#making a graph of Time v. BHDistance
plt.plot(time, BHdistance)
plt.ylabel('BH Distance')
plt.xlabel('Time')
plt.show()
