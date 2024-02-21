import numpy as np
import matplotlib.pyplot as plt
import math


#Simulates ability of function_propagate to simulate the propagation of complex wave fields
#Original code by Nicholas Pegard @UNC, this is a re-write in python (for people who don't have access to a MATLAB license)

#######Defining parameters of the simulation#############
#Wavelength
wav = 1.0e-6
print(wav)
#Size of pixel in metres
ps = 10.0e-6
print(ps)
#Number of data points along x-axis and y-axis
lx = 300
ly = 300
#Propoagation distance of wave in meters in 1cm increments
prop_dist = np.linspace(0,0.01,20)
#print(prop_dist)

#Creating co-ordinate grid for plotting wavefunction
ux = np.linspace(0,1,300)
ux = ux*ps
ux = 1000*(ux-np.mean(ux))

print(ux)

uy = np.linspace(0,1,300)
uy = uy*ps
uy = 1000*(uy-np.mean(uy))

print(uy)
