#!/usr/bin/python

# readRGB.py
# Auslesen des aktuell eingestellten RGB-Farbwertes
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

file = open('/sys/bus/w1/devices/29-00da24080001/output', 'r')
file.seek(0)
red = file.read()
file.close()

file = open('/sys/bus/w1/devices/29-00da24080002/output', 'r')
file.seek(0)
green = file.read()
file.close()

file = open('/sys/bus/w1/devices/29-00da24080003/output', 'r')
file.seek(0)
blue = file.read()
file.close()

print('#{:02x}{:02x}{:02x}'.format(ord(red), ord(green), ord(blue)))

