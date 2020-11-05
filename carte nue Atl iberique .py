#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:25:34 2020

@author: utilisateur
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


mymap=Basemap(projection='merc',llcrnrlat=9,urcrnrlat=61,llcrnrlon=-20,urcrnrlon=13,resolution='h') # dans l'ordre WRNG pas dans n'importe quel ordre 

#X, Y = mymap(lon, lat)
#mymap.scatter(X, Y, s=0.1)   #trace le transect
mymap.drawcoastlines()
myparallels=np.arange(-90,90+1,20)    #  le dernier 10 signifi affiche tout les 10 lon/lat en légende/quadrillage
mymeridians = np.arange(-180,180+1,30) 
mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=10)  
mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=9)
plt.ylabel("Lat", size = 12, position=(0.8, 1))
plt.xlabel("Lon", size = 11, position=(1,1))
mymap.fillcontinents(color='0.83',lake_color='0.83',zorder=100)
