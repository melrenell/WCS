#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:14:22 2020

@author: melaniee
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

filename = '/afs/cas.unc.edu/users/m/e/melaniee/GITHUB/WCS/0278.Ne.fits'

hdu = fits.open(filename)
spec = hdu[0].data[0] #needs extra index for arc file
x = np.arange(len(spec[500])) #create array of x values the length of the image

peaks1=np.array([])
for j in range(350,650):
    peak = np.argmax(spec[j])
    peaks1=np.append(peaks1,peak)
    

peaks0=np.array([])
for j in range(715,950):
    peak = np.argmax(spec[j])
    peaks0=np.append(peaks0,peak)
   

peaks2=np.array([])
for j in range(55,300):
    peak = np.argmax(spec[j])
    peaks2=np.append(peaks2,peak)
   
    
# Plot spectrum
#plt.figure()
#plt.scatter(x,spec[500])
#plt.plot(x,spec[500])
#plt.show()

x2= np.arange(len(spec))
peaksall=np.array([])
for j in range(0,1048):
    peak = np.argmax(spec[j])
    peaksall=np.append(peaksall,peak)
plt.figure()
plt.plot(peaksall,x2,'bo',markersize=1)
plt.title('Arc File')
plt.show()

filename2 = '/afs/cas.unc.edu/users/m/e/melaniee/GITHUB/WCS/0271.rs0010si.fits'

hdu2 = fits.open(filename2)
spec2 = hdu2[0].data[0] #needs extra index for arc file
x = np.arange(len(spec2[:,500])) #create array of x values the length of the image


x2= np.arange(len(spec))
peaksall2=np.array([])
for j in range(len(spec)):
    peak2 = np.argmax(spec2[j])
    peaksall2=np.append(peaksall2,peak2)  

plt.figure()
plt.plot(peaksall2,x2,'bo',markersize=1)
plt.title('Slit File')
plt.show()

"""
peaks2=np.zeros(200)
for k in range(len(peaks2)):
    for j in range(350,650):
        peaks2[k] = np.argmax(spec2[j])
slitx = np.int(np.sum(peaks2)/len(peaks2))
   
y = spec2[:,slitx]   
 
#Plot spectrum
plt.figure()
plt.scatter(x,y)
plt.plot(x,y)
plt.show()
"""

