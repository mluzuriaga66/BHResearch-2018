import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import readcol
import csv

#this is defining files to be the readcol 
files = readcol.readcol('testdata.txt')

#defining time and choosing to read the first column because that's where time is
time = files[:,0]
BHdistance = files[:,3]

#number of files
#nfiles = len(files)

#print 'this is time:', time
#print 'this is the distance:', BHdistance

plt.plot(time, BHdistance)
plt.ylabel('Time')
plt.xlabel('BH Distance')
plt.show()

#with open("testdata.txt") as f:
#    lines = f.readlines()

#    x = [line.split()[0] for line in lines]
#    y = [line.split()[1] for line in lines]

    #plt.show()

#plt.show()

#x = [time]
#y = [BHdistance]

#with open('testdata.txt','r') as csvfile:
#        plots = csv.reader(csvfile, delimiter=',')
#        for row in plots:
#            x.append(int(time[0]))
#            y.append(int(BHdistance[1]))
#plt.plot(x,y, label='Loaded from file!')

#x, y = np.loadtxt('testdata.txt', delimiter=',', unpack=True)
#plt.plot(x,y, label='Loaded from file!')

#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Interesting Graph\nCheck it out')
#plt.legend()
#plt.show()

#X, Y = [], []
#for line in open('testdata.txt', 'r'):
#      values = [float(s) for s in line.split()]
#      X.append(values[0])
#      Y.append(values[1])

#plt.plot(X, Y)
#plt.show()

#data = np.loadtxt('testdata.txt')

#plt.plot(data[:,0], data[:,1])
#plt.show()
