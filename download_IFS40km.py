#!/usr/bin/env python3

# ============================================================================================================
#                  Script that downloads daily ECMWF data in grib2 format transforming to netcdf.
#                      This will generate the accumulated rainfall of the IFS/ECMWF 40km
#
#                                   Mateus Dias Nunes @WorldSE - March 2022
#
# ============================================================================================================


from ecmwf.opendata import Client         # pip install ecmwf-api-client
from datetime import datetime
import time as t                         
import os
from cdo import Cdo
cdo = Cdo()


print('------------------------------------------------------------------------------------------------------')
print('----------------------------https://github.com/ecmwf/ecmwf-opendata-----------------------------------')
print('------------------------------------------------------------------------------------------------------')
print('----------------------------https://pypi.org/project/ecmwf-opendata-----------------------------------')
print('------------------------------------------------------------------------------------------------------')
print('                     ECMWF Download (ECMWF Data Store (ECPDS)) - Script started.                      ')
print('                                                                                                      ')
print('                                                                                                      ')
print('---------------------------------------- Data from: --------------------------------------------------')
print('------------------------------https://data.ecmwf.int/forecasts/---------------------------------------')
print('------------------------------------------------------------------------------------------------------')

#----------------------------------------------------------------------------------------------------------------------------------------
#                                     DEFINE  TIMESTEP PARAMETERS
#----------------------------------------------------------------------------------------------------------------------------------------
# Start the time counter
start_time  = t.time()

today       = datetime.today().strftime('%Y%m%d')    # date='20220125',

presentTime = datetime.now().strftime('%H')          # hour=10

dataformat  = datetime.today().strftime('%Y-%m-%d')  # date='2022-01-25' - To configure "settaxis" in CDO

#----------------------------------------------------------------------------------------------------------------------------------------
# Define forecast time
if presentTime <= '10':
   
   hour_run  = '00' 

else: 
   hour_run  = '12'

# Desired forecast hours
step_hour   = 6       
init_hour   = 0     # Init time
last_hour   = 240 + step_hour   #   End time 0 - 240 - 10 days forecast 10 dias

# ----------------------------------------------------------------------------------------------------------------------------------------
# Download temporary directory
RECENT = '/home/mateusdiasnunes/IFS/' + today + '/' + hour_run + '/'
os.makedirs(RECENT, exist_ok=True)

#----------------------------------------------------------------------------------------------------------------------------------------
#Create final directory 
USER_path  = '/home/mateusdiasnunes/models/IFS_40/'
MODEL_path = USER_path + today + '/' + hour_run + '/'
os.makedirs(MODEL_path, exist_ok=True)

#----------------------------------------------------------------------------------------------------------------------------------------
#create name to downloads
filename    = RECENT + 'IFS_oper_fc_'  + today + '_f' +  str(init_hour).zfill(3) + '_' + str(last_hour).zfill(3) + '_' + hour_run + 'Z.grib2'

filenameout = RECENT + 'ec_oper40_fc_' + today + '_f' +  str(init_hour).zfill(3) + '_' + str(last_hour).zfill(3) + '_' + hour_run + 'Z.grib2'     
#----------------------------------------------------------------------------------------------------------------------------------------


#====================================================================================================================================
#                                                DOWNLOADING DATA FILE ECMWF
#====================================================================================================================================

#('----------------------------------------------------------------------------------------------------------------------------')
#('------------------------------------------Defining parameters do ecmwf.opendata---------------------------------------------')
#('                                                                                                                            ')
#('-------------------------------Information about https://github.com/ecmwf/ecmwf-opendata------------------------------------')
#('----------------------------------------------------------------------------------------------------------------------------')

# Downloading data type: forecast (fc), of strem: operational (oper), to parameter: total precipitation (tp)
# In https://github.com/ecmwf/ecmwf-opendata has explanation about the variables 

client = Client(source="ecmwf")
client.retrieve(
    
    {
        'date'  : today,
        'time'  : hour_run,
        'step'  : [i for i in range(init_hour, last_hour, step_hour)],
        'stream': 'oper',
        'type'  : 'fc',
        'param' : 'tp',
    },
        filename)


#Cutting South America
cdo.mulc('1000', input='-sellonlatbox,-75,-30.2,-35,5 %s' % (filename), output=(filenameout)) # cdo mulc,1000 to pass data file units from kg.kg.m-2 to mm.dia-1

os.remove(filename) # remove data file 

# Download loop
for hour in range(init_hour, last_hour + 1, step_hour):
    print('Downloading... IFS (ECMWF): HRES High Resolution Forecast')
    print('---------------------------------------------------------')
    print('Horizontal resolution: 0.4 (40km)')
    print('Date: ' + today)
    print('Initialization hour: ' + hour_run)
    print('Forecast time: f ' + str(hour).zfill(3))

    print('------------------------------------------------------------------------------')
    print('\n   Time Process: ', round((t.time() - start_time), 2), 'seconds.            ')
    print('------------------------------------------------------------------------------')
    print('--------ECMWF Download (ECMWF Data Store (ECPDS)) - Script finished.----------')
    print('------------------------------------------------------------------------------')

print('----------------------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------------------')

#====================================================================================================================================


# # # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # #                                                 - Loop to calculate cumulative precipitation from 12Z to 12Z
# # #                                                       NOTE: IFS forecast precipitation data is cumulative
# # #                                                     As there are 41 times for each forecast time (6h at 6h),
# # #                                               will be calculated on forecast time (41 times) and NOT synoptic times
# # #                                   Ex: 12Z to 12Z of the first day is equivalent to subtracting COUNT 06(36Z) minus COUNT 03(12Z)
# # #                                               the second day will be COUNT 10 (60Z) minus COUNT (42Z) and so on.
# # # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#################################################################################################################################################################################
# DAYS       |    1     |       2     |       3     |      4     |       5        |      6          |        7        |        8        |         9       |         10      |
# HOUR_UTC   00 06 12 18| 00 06 12 18 | 00 06 12 18 |00 06 12 18 | 00  06  12  18 |  00  06  12  18 |  00  06  12  18 |  00  06  12  18 |  00  06  12  18 |  00  06  12  18 |  00 
# COUNT      00 01 02 03| 04 05 06 07 | 08 09 10 11 |12 13 14 15 | 16  17  18  19 |  20  21  22  23 |  24  25  26  27 |  28  29  30  31 |  32  33  34  35 |  36  37  38  39 |  40
# FORECAST(Z)00 06 12 18| 24 30 36 42 | 48 54 60 66 |72 78 84 90 | 96 102 108 114 | 120 126 132 138 | 144 150 156 162 | 168 174 180 186 | 192 198 204 210 | 216 222 228 234 | 240       
#################################################################################################################################################################################


# #Define forecast time

data_file = filenameout

if hour_run == '00':

   for analysis in range(3, 40, 4):
     print(f'O valor de analysis: {analysis} ')
     forecast = analysis + 3
     if forecast < 40:
      print(f'O valor de forecast: {forecast} ')
      cdo.sub(input  =  cdo.seltimestep( str(forecast), input  =  data_file) + ' ' + cdo.seltimestep( str(analysis), input  =  data_file), output  =  RECENT+'temp_ifs_oper_fc_'+today+'_'+str(forecast)+'_'+str(analysis)+'.grib2')  #python
     elif forecast >= 41:
      forecast=forecast-1
      print(f'O valor extra: {forecast} ')
      cdo.sub(input  =  cdo.seltimestep( str(forecast), input  =  data_file) + ' ' + cdo.seltimestep( str(analysis), input  =  data_file), output  =  RECENT+'temp_ifs_oper_fc_'+today+'_'+str(forecast)+'_'+str(analysis)+'.grib2')  #python

elif hour_run == '12':

    for analysis in range(1, 40, 4):
      print(f'O valor de analysis: {analysis} ')
      forecast = analysis + 3
      if forecast < 41:
       print(f'O valor de forecast: {forecast} ')
       cdo.sub(input  =  cdo.seltimestep( str(forecast), input  =  data_file) + ' ' + cdo.seltimestep( str(analysis), input  =  data_file), output  =  RECENT+'temp_ifs_oper_fc_'+today+'_'+str(forecast)+'_'+str(analysis)+'.grib2')  #python

#CDO in python 
#cdo.OPERATOR3("PARAM3",input="-OPERATOR2,PARAM2 -OPERATOR1,PARAM1 INPUT.grib2", output="OUTPUT.grib2")

final_infile  = RECENT+'temp_ifs_oper_fc_'+today+'_*.grib2 ' #join data files 

final_outfile = RECENT+'ecmwf_SA_oper_fc_'+today+'_f'+str(init_hour).zfill(3)+'_'+str(last_hour).zfill(3)+'_'+hour_run+'Z.nc'


# Change variable name from "tp" to "prec_acum_12Z" 
# This was a standardization option so that all weather models have the same nomenclature on the precipitation variable between 12Z-12Z.
# To pass format from grib2 to netcdf

cdo.settaxis(str(dataformat)+',12:00:00,1day -chname,tp,prec_acum_12Z -mergetime', input=final_infile,  output=final_outfile, options='-f nc', returnCdf=True)

os.system('mv ' +final_outfile+ ' ' + MODEL_path) #move data to final directory
os.system('rm -R ' + RECENT )                     #remove all temporary datafiles

#############################################################################################################################################################################################################################################################
#############################################################################################################################################################################################################################################################


