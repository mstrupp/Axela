#!/usr/bin/python

# test0.py
# Python Skript zum Ausschalten einer LED am 1-Wire Bus
#
# Die Datei mit der entsprechenden Adresse wird geöffnet und eine 0
# hineingeschrieben.
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

file = open('/sys/bus/w1/devices/29-00da24080000/output', 'w')
file.seek(0)
file.write('\x00')
file.close()
print('Ausgeschaltet.')
