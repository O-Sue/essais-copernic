#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:06:00 2020

@author: utilisateur
"""


import xarray as xr
import matplotlib.pyplot as plt


Situ2 = xr.open_dataset("CORIOLIS-GLOBAL_salinity.nc", decode_times=True)
Mod2 = xr.open_dataset("dataset-ibi-analysis-forecast-phys-005-001-monthly_1604148880512.nc", decode_times=True)



lat=Situ2['latitude']
lon=Situ2['longitude']
time=Situ2['time']

plt.gcf().subplots_adjust(hspace=0.5, wspace=0.15, top = 1.7, bottom = 0.1)

situ = plt.subplot(2, 1, 1)

for time in range(len(time)) : # attention ! parenthese ou crochet ? idema desouss
    
    for lat in [9 , 61] :
        
        for lon in  [-20 , 13] :
            
                Situ2.PSAL.values = Situ2.PSAL                
                Situ2.PSAL.plot(facecolor ='peru')
               # plt.hist(bins=10) ATTENTIO & ATTENTIO DATES ! 2020 ?? 
situ.set_title('IBI sea surface salinity based on in situ measurement (monthly, 15 june 2018 - 15 september 2020) [PSS-78]', position = (0.5, -0.3), size=10)
situ.set_xlabel('')#IBI sea surface salinity based on in situ measurement (monthly, 15 june 2018 - 15 september 2018) [PSS-78]', position = (0.5, -0.5))


mod= plt.subplot(2, 1, 2)

Mod2.so.plot(facecolor = 'blue')
mod.set_title('IBI sea surface salinity by model (monthly, 16 june 2018 - 16 september 2020) [PSS-78]', position = (0.5, -0.3), size=10)
mod.set_xlabel("")                                                                                                                              ##centre le titre dessous la figure
