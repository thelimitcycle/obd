import obd
import time
import numpy as np
import sys

# add verbose toggle at command line interface
verbose = False

#set up the connection with the car
print('Starting vehicle monitor')
connection = obd.OBD()

load = obd.commands.ENGINE_LOAD #from the python_obd library
rpm = obd.commands.RPM
speed = obd.commands.SPEED


k = 0
try:
    while True:
        #get the time
        t = time.time()
        #check quantities of interest
        rpmres = connection.query(rpm)
        loadres = connection.query(load)
        spdres =  connection.query(speed)
        
        if verbose:
        #display them
            loadstr = 'Engine load: {0} {1}'.format(loadres.value, loadres.unit) 
            rpmstr = 'RPM: {0} {1}'.format(rpmres.value, rpmres.unit)
            spdstr = 'Speed: {0} {1}'.format(spdres.value, spdres.unit)
         

            idstr = 'time:{0}, frame{1}'.format(t, k)
            print(idstr)
            print(loadstr)
            print(rpmstr)
            print(spdstr)
            print(flevstr)
            print(fratestr)
            print('\n')
        else:
            if k ==0:
                print('Frame\tTime\t\Engine Load\tRPM\tSpeed')
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}'.format(k, t, loadres.value, rpmres.value, spdres.value))

        #add this set of measurements to the counter
        k = k+1
            
except KeyboardInterrupt:
    obd.OBD.close(connection)
    if(obd.OBD.is_connected == False):
        print('OBD connection sucessfully closed')
        print('Thank you for flying Lufthansa')
    exit()
