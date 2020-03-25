#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:55:31 2020

@author: melaniee
Plots RA and Dec of all original images from one night to explore variations
"""

from astropy.io import fits
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord as sky
from astropy import units as u

galname=['rs0001','rs0010','rs0314','rs0361','rs0536','rs0546']
for j in galname:
    files=[]
    bspecfiles=[]
    gspecfiles=[]
    RAarray=np.array([])
    Decarray=np.array([])
    filepath='/afs/cas.unc.edu/users/m/e/melaniee/GITHUB/WCS'
    
    os.chdir(filepath)
    for file in glob.glob('*'+j+'*'):
        files.append(file)
        
    for k in glob.glob('*bspec*'):
        bspecfiles.append(k)
        
    for l in glob.glob('*gspec*'):
        gspecfiles.append(l)
        
    for i in range(len(files)):
        image = fits.open('/afs/cas.unc.edu/users/m/e/melaniee/GITHUB/WCS/'+files[i])
        RA0 = image[0].header['RA']
        Dec0 = image[0].header['DEC']
        c = sky(RA0,Dec0, unit=(u.hourangle,u.deg))
        RA=c.ra.degree
        Dec=c.dec.degree
        RAarray= np.append(RAarray,RA)
        Decarray=np.append(Decarray,Dec)
    
    plt.figure()
    for i in range(len(files)):
        plt.plot(RAarray[i],Decarray[i],'bo')
        plt.annotate(files[i],(RAarray[i],Decarray[i]))
    plt.title(j+' files')
    plt.xlabel('RA')
    plt.ylabel('Dec')
    plt.show()