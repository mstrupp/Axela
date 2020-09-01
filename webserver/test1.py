#!/usr/bin/python

# test0.py
# Python Skript zum Anschalten einer LED am 1-Wire Bus
#
# Die Datei mit der entsprechenden Adresse wird geöffnet und eine 1
# hineingeschrieben.
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

file = open('/sys/bus/w1/devices/29-00da24080000/output', 'w')
file.seek(0)
file.write('\x01')
file.close()
print('Angeschaltet.')
