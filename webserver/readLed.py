#!/usr/bin/python

# readLED.py
# Auslesen des aktuellen LED-Schaltzustandes
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

file = open('/sys/bus/w1/devices/29-00da24080000/output', 'r')
file.seek(0)
status = file.read()
file.close()

if status == '\x00':
    print('off')
elif status == '\x01':
    print('on')
