#!/usr/bin/env python
import os,sys
import time
import subprocess

gatt = 'sudo python gatt_sensor.py'
restart = 'sudo systemctl restart bluetooth'
status = 'sudo systemctl status bluetooth'
pow_off = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 power off'
le_on = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 le on'
connect_on = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 connectable on'
bredr_off = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 bredr off'
adv_on = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 advertising on'
pow_on = 'sudo /home/pi/bluez-5.45/tools/btmgmt -i hci0 power on'
run = 'sudo /home/pi/bluez-5.45/tools/btgatt-server -i hci0 -s low -t public -r -v'

os.system(pow_off)
os.system(le_on)
os.system(connect_on)
os.system(bredr_off)
os.system(adv_on)
os.system(pow_on)
#os.system(run)
os.system(gatt)

#print "ready Go"
#while 1:
#os.system('sudo systemctl restart bluetooth')
#value =subprocess.Popen('sudo python gatt_sensor.py',shell=True)
#value = subprocess.call('sudo python gatt_sensor.py',shell=True)
#print value
#    ret=subprocess.call(gatt,shell=True,stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
#    if ret==0:
#        os.system(status)
#        print 'is alive!'
#    elif ret==1:
#        print 'is down...'
#
#    time.sleep(2)
    #sys.exit()
