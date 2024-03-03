import numpy as np
import matplotlib.pyplot as plt
import math
import sys
np.set_printoptions(threshold=sys.maxsize)
import function_input
import function_propagate
from function_input import function_greylevel
from function_propagate import function_propagate


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
print (Amplitude)
#Select one of the options below for phase of wavefunction
Phase = np.zeros((lx,ly))
#Phase = 2*np.pi*rand(lx,ly)

ComplexField = Amplitude * np.exp(1j*Phase)

#Display Amplitude and Phase at z = 0
#Create a figure and define subplots
fig,ax = plt.subplots(1,3,figsize=(15,5))

#Plot the intensity

# Create a figure with 2 rows and 3 columns
fig = plt.figure(1)

# Plot 1: Intensity at z=0
plt.subplot(2, 3, 1)
plt.imshow(abs(ComplexField)**2, extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
plt.axis('image')
plt.xlabel('X [mm]')
plt.ylabel('Y [mm]')
plt.title('Intensity at z=0')

# Plot 2: Amplitude at z=0
plt.subplot(2, 3, 2)
plt.imshow(abs(ComplexField), extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
plt.axis('image')
plt.xlabel('X [mm]')
plt.ylabel('Y [mm]')
plt.title('Amplitude at z=0')

#Plot 3: Phase at z=0
plt.subplot(2, 3, 3)
plt.imshow(np.angle(ComplexField), extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
plt.axis('image')
plt.xlabel('X [mm]')
plt.ylabel('Y [mm]')
plt.title('Phase at z=0')


fig, ax = plt.subplots(2, 3, figsize=(15, 10))

for j in range(len(prop_dist)):
    # Propagate the field
    NewField = function_propagate(ComplexField, wav, prop_dist[j], ps, ps)

    # Display propagated field
    ax[0, 1].cla()
    ax[0, 1].imshow(np.abs(NewField)**2, extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
    ax[0, 1].axis('image')
    ax[0, 1].set_xlabel('X [mm]')
    ax[0, 1].set_ylabel('Y [mm]')
    ax[0, 1].set_title(f'Propagated Intensity z = {prop_dist[j]} m')

    ax[0, 2].cla()
    ax[0, 2].imshow(np.abs(NewField), extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
    ax[0, 2].axis('image')
    ax[0, 2].set_xlabel('X [mm]')
    ax[0, 2].set_ylabel('Y [mm]')
    ax[0, 2].set_title(f'Amplitude at z = {prop_dist[j]} m')

    ax[1, 0].cla()
    ax[1, 0].imshow(np.angle(NewField), extent=(uy.min(), uy.max(), ux.min(), ux.max()), cmap='gray')
    ax[1, 0].axis('image')
    ax[1, 0].set_xlabel('X [mm]')
    ax[1, 0].set_ylabel('Y [mm]')
    ax[1, 0].set_title(f'Phase at z = {prop_dist[j]} m')

    plt.draw()
    plt.pause(0.1)  # Adjust the pause duration if needed

# Show the plots
plt.show()
