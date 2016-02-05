import obd
import time
import numpy as np
import sys
from matplotlib import pyplot as plt

obd.debug.console = False

rpmdat = np.array([[0,0]])
spddat = np.array([[0,0]])
enldat = np.array([[0,0]])

connection = obd.Async()

#still not very fast only going at about 2 fps maybe a bit slower...
#maybe take the debug/print statements out???
# a callback that prints every new value to the console
def new_rpm(r):
    if not r.is_null():
#        sys.stdout.flush()
#        sys.stdout.write('\rrpm: %f %s at time: %s' % (r.value, r.unit, r.time()))
        print('\rrpm: %f %s at time: %s' % (r.value, r.unit, r.time))
        global rpmdat
        rpmdat = np.append(rpmdat, [[r.time, r.value]],axis=0)
#        rpmval = np.append(rpmval, r.value)
#        rpmtim = np.append(rpmtim, r.time)

def new_speed(r):
    if not r.is_null():
        print('\rspeed: %f %s at time: %s'% (r.value, r.unit, r.time))
        global spddat
        spddat = np.append(spddat, [[r.time,r.value]],axis=0)
#        spdval = np.append(spdval, r.value)
#        spdtim = np.append(spdtim, r.time)

def new_engine_load(r)


connection.watch(obd.commands.RPM, callback=new_rpm)
connection.watch(obd.commands.SPEED, callback=new_speed)
connection.start()



#mechanical things used to be so cool. Now everything is computerized and the
#fun of designing mechanical components is gone. Distributer have been 
#replaced with ECUs

# the callback will now be fired upon receipt of new values
# the same people who make corn chex built the Alvin????
time.sleep(60)
connection.stop()

#
#ipython > matlab
#learn how to configure ipython startup to have the following packages
#-plotting
#-dsp related things
#-numpy
#-scipy
#-time

#TODO FOR REAL, learn more about how computers work. Someday they'll probably
#be putting pentiums in car engines
