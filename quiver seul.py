#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:40:02 2020

@author: utilisateur
"""


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

#from mpl_toolkits.basemap import Basemap

Mod = xr.open_dataset("reanalysis model sst.nc", decode_times=True)
u = Mod['uo']
v = Mod['vo']
lon=Mod['longitude']
lat=Mod['latitude']
time= Mod['time']



print(time[3])  # le 4e donc le 11juillet 2018

plt.figure(figsize=(10,10))

for time in range(3) :

    #x=np.linspace(9, 61,300)
   # y=np.linspace(-20, 13,300)
    
    
   # X, Y = np.meshgrid(x,y)
    
    
    #X, Y = mymap(lon, lat) 
    X4, Y4 =np.meshgrid (lon, lat)
    # X4, Y4 = mymap(lons, lats) 
    u,v =np.meshgrid(u, v)
    

    plt.ylabel("Lat", size = 12, position=(0.8, 1))
    plt.xlabel("Lon", size = 11, position=(1,1))
    #plt.text(x, y, 'Barcelona',fontsize=12,fontweight='bold', ha='left',va='center',color='k', bbox=dict(facecolor='b', alpha=0.2))
    #plt.savefig('balabala')
    #mymap.quiver([lon, lat], u, v)
    
    for i in range (0, len(lat)) : 
   # for j in range (0, len(lon)): 
            plt.quiver(X4,Y4,u[i],v[i]) #,speed[i]) #,cmap=cmap‌​,latlon=True)


            #mymap.quiver(X4, Y4, u[i] + v[i])#, speed[i],latlon=True)
            
            #plt.streamplot(X4, Y4, u[i], v[i])
            #plt.streamplot(X, Y, u, v, color=np.sqrt(u**2+v**2), linewidth = 2, cmap =plt.cm.viridis)
            #plt.colorbar(plt.lines)
