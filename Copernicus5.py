#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:28:40 2020

@author: utilisateur
"""


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


Sit = xr.open_dataset("dataset-ibi-analysis-forecast-phys-005-001-2daily_1604575757062.nc")


lon=Sit['longitude'][:]
lat=Sit['latitude'][:]
time=Sit['time'][:]
temp=Sit['thetao'] [0,0,:,:] 
xL=[]

xL.append(time[:])


plt.figure(figsize=(25,40))
            
            
mymap=Basemap(projection='merc',llcrnrlat=26,urcrnrlat=56,llcrnrlon=-19,urcrnrlon=5,resolution='h') # dans l'ordre WRNG pas dans n'importe quel ordre 
    
#X, Y = mymap(lon, lat)
lon, lat = np.meshgrid(lon,lat)
#mymap.scatter(X, Y, s=0.1)   #trace le transect
mymap.drawcoastlines()
myparallels=np.arange(-90,90+1,20)    #  le dernier 10 signifi affiche tout les 10 lon/lat en légende/quadrillage
mymeridians = np.arange(-180,180+1,30) 
mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=25)  
mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=25)
plt.ylabel("Lat", size = 25, position=(0.8, 1))
plt.xlabel("Lon", size = 25, position=(1,1))
mymap.fillcontinents(color='0.83',lake_color='0.83',zorder=100)
mymap.pcolormesh(lon, lat, temp, latlon=True, cmap='nipy_spectral')
plt.colorbar( shrink=0.5, label='Sea surface temperature by model [$\mathregular{^oC}$]' )



plt.figtext(0.5,0.2, "27-10-2018", fontsize = 70),#bbox=dict(facecolor='darkblue'))
plt.savefig("Copernicus5-1.png")