#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:55:41 2020

@author: utilisateur
"""


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

Sit = xr.open_dataset("dataset-ibi-analysis-forecast-phys-005-001-2daily_1604575757062.nc")
v = Sit['vo']#[:,0,:,:]  
u = Sit['uo']#[:,0,:,:]  
s = Sit['so'] 
temp=Sit['thetao'] 

lon=Sit['longitude']#[:]
lat=Sit['latitude']#[:]
time=Sit['time']#[:]


plt.figure(figsize=(25,40))
    
plt.title("Température, salinité et courant horizontaux, d'après modèle à la station de coordonées [-16.527779° E ; 28.472221° N] entre le 27 octobre et le 3 novembre 2018") 
plt.gcf().subplots_adjust(hspace=0.4,  right= 0.9, top = 1)

       
Lon=np.where(lon==-16.527779)
Lat=np.where(lat==28.472221)
coordo=np.ravel(Lon)
coorda=np.ravel(Lat)



T= plt.subplot(3, 1, 1)

temp2=np.ravel(temp[:, 0, coordo, coorda])
plt.plot(time, temp2,'ro-',linewidth=1.5, color = "maroon")
plt.ylabel("SST [$\mathregular{^oC}$]", size=24)
plt.xticks()
plt.yticks(size=16)
for tickLabel in plt.gca().get_xticklabels(): 
    
         tickLabel.set_fontsize(20)
         
         


S=plt.subplot(3, 1, 2)

sal2=np.ravel(s[:, 0, coorda, coordo])
plt.plot(time, sal2,'ro-',linewidth=1.5, color = "salmon")
plt.ylabel("salinity [PSS-78]", size=24)
plt.xticks()
plt.yticks(size=16)
for tickLabel in plt.gca().get_xticklabels(): 
    
         tickLabel.set_fontsize(20)
  
  
V= plt.subplot(3, 1, 3)

u2=np.ravel(u[:, 0, coorda, coordo])
v2=np.ravel(v[:, 0, coorda, coordo])
r= np.linspace(1,len(time), len(time))
c=np.hypot(u2,v2)


plt.quiver(r, c, u2, v2, color = "navy", width=0.005)

plt.plot(r, c,'x', linewidth=0.0040)


plt.ylabel("surface current speed[m/s]", size=24, position = ( 0 , 0.5))
plt.xlabel("Time [days]", position = (1.07, -0.7), size=25)
plt.xticks()
plt.yticks(size=16)
for tickLabel in plt.gca().get_xticklabels(): 
    
         tickLabel.set_fontsize(23)
  

#plt.text( 'blabla', horizontalalignment='left', verticalalignment='bottom' )


plt.savefig("Copernicus4.png")
