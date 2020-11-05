#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:33:46 2020

@author: utilisateur
"""

import xarray as xr
import matplotlib.pyplot as plt


Sat = xr.open_dataset("obs sat sst.nc", decode_times=True)
Mod = xr.open_dataset("reanalysis model sst.nc", decode_times=True)
Situ = xr.open_dataset("CORIOLIS-GLOBAL-NRTOA-OBS_IN SITU_TIME_SERIE_1603882301942.nc", decode_times=True)





lat=Situ['latitude']
lon=Situ['longitude']


plt.gcf().subplots_adjust(hspace=1, wspace=0.15, top = 1.7)

situ = plt.subplot(3, 1, 1)

for lat in [9 , 61] :
    
    for lon in  [-20 , 13] :
        
            Situ.TEMP.values = Situ.TEMP                
            Situ.TEMP.plot(facecolor ='peru')
situ.set_title('')
situ.set_xlabel('IBI sea surface temperature based on in situ measurement [degree celsius] ')
plt.text(15 , 370000, 'daily, 08-07-2018 to 08-09-2018', horizontalalignment='left', verticalalignment='top' )
sat= plt.subplot(3, 1, 2)

Sat.analysed_sst.values = Sat.analysed_sst -273.15
Sat.analysed_sst.plot()
sat.set_title('')
sat.set_xlabel('IBI analysed sea surface temperature measured by satelite [degree celsius]')

mod= plt.subplot(3, 1, 3)

Mod.thetao.plot(facecolor = 'blue')
mod.set_title('')
mod.set_xlabel('IBI sea surface temperature by model [degree celsius]')

#plt.legend()

# date / encadré légendes

#Temperature in situ de la zone Atlantique IBI en degrés
#Temperature mesurée par satellite de la zone Atlantique IBI en degrés