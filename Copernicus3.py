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

Mod = xr.open_dataset("dataset-ibi-analysis-forecast-phys-005-001-daily_1604511631098.nc")#, decode_times=True)
u = Mod['uo'][0,0,:,:]
v = Mod['vo'][0,0,:,:]  
lon=Mod['longitude'][:]
lat=Mod['latitude'][:]




plt.figure(figsize=(10,10))

Resolution=np.hypot(u, v)

plt.quiver(lon,lat,u,v, Resolution, cmap='Blues' , width=0.0040) #,speed[i]) #,cmap=cmap‌​,latlon=True)

plt.ylabel("Lat", size = 12, position=(0.8, 1))
plt.xlabel("Lon", size = 11, position=(1,1))
          
            #plt.streamplot(X4, Y4, u[i], v[i])
            #plt.streamplot(X, Y, u, v, color=np.sqrt(u**2+v**2), linewidth = 2, cmap =plt.cm.viridis)
plt.colorbar(aspect=18)
plt.title("Champs de courant de surface (vitesse en m/s) simulé pour le 4 juillet 2020 dans la zone IBI", position = (0.7, 1.1 ), size = 12)


#plt.savefig("Blues3.png")