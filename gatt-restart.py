#!/usr/bin/env python
import os,sys
import time
import subprocess

print "ready Go"
while 1:
#os.system('sudo systemctl restart bluetooth')
#value =subprocess.Popen('sudo python gatt_sensor.py',shell=True)
#value = subprocess.call('sudo python demo.py',shell=True)
#print value
    ret=subprocess.call('sudo python gatt_sensor.py',shell=True,stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
    if ret==0:
        os.system('sudo systemctl status bluetooth')
        os.system('sudo systemctl restart bluetooth')
        print 'is alive!'
        os.system('sudo systemctl status bluetooth')
    elif ret==1:
        print 'is down...'
    time.sleep(2)
    #sys.exit()
