#!/usr/bin/python
import sys

#ROT

file = open('/sys/bus/w1/devices/29-00da24080001/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][1:3],16)))
file.close()


#GRUEN

file = open('/sys/bus/w1/devices/29-00da24080002/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][3:5],16)))
file.close()

#BLAU

file = open('/sys/bus/w1/devices/29-00da24080003/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][5:7],16)))
file.close()

#Wiederholung da der Arduino nicht alles an Code richtig geladen hat

file = open('/sys/bus/w1/devices/29-00da24080001/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][1:3],16)))
file.close()
file = open('/sys/bus/w1/devices/29-00da24080002/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][3:5],16)))
file.close()
file = open('/sys/bus/w1/devices/29-00da24080003/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][5:7],16)))
file.close()
file = open('/sys/bus/w1/devices/29-00da24080001/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][1:3],16)))
file.close()
file = open('/sys/bus/w1/devices/29-00da24080002/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][3:5],16)))
file.close()
file = open('/sys/bus/w1/devices/29-00da24080003/output', 'w')
file.seek(0)
file.write(chr(int('0x'+sys.argv[1][5:7],16)))
file.close()
