import numpy as np
import matplotlib.pyplot as plt
import math
import sys
np.set_printoptions(threshold=sys.maxsize)
import function_input
from function_input import function_greylevel
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
#Create 2D grid of above vectors
xx,yy = np.meshgrid(ux,uy)
print(xx,yy)

#Import a test image
Image = function_greylevel("Image1.jpg")
Image = np.resize(Image,(lx,ly))
Image = -Image

print(Image)


#Creating complex field by setting amplitude and phase
Amplitude = np.sqrt(Image)
#Select one of the options below for phase of wavefunction
Phase = np.zeros(lx,ly)
#Phase = 2*np.pi*rand(lx,ly)

ComplexField = Amplitude * np.exp(1j*Phase)

#Display Amplitude and Phase at z = 0
#Create a figure and define subplots
fig,ax = plt.subplots(1,3,figsize=(15,5))

#Plot the intensity
