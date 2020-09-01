#!/usr/bin/python

# rgb.py
# Python Skript zum Ansteuern der RGB LED am 1-Wire Bus.
#
# Als Parameter der Funktion wird der RGB Wert im Format #rrggbb übergeben.
# Dabei entsprechen rr, gg, bb den als als Hex-Zahlen kodierten Rot-Grün-Blau
# Farbkomponenten. Der #rrggbb String ist in sys.argv[1] gespeichert. Um auf den
# Rot-Anteil zuzugreifen wird sys.argv[1][1:3] verwendet. Die Grün- und Blau-
# Codes stehen an dementsprechend anderen Stellen im String. Die
# Text-Komponenten werden zuerst zu Integer Zahlen konvertiert. Dann werden
# diese zu Character-Symbolen konvertiert. Diese Zeichen werden dann auf den
# 1-Wire Bus geschrieben. Beim Ansteuern der RGB LED kam es zu Problemen. Die
# Farbe wurde in seltenen Fällen nicht korrekt übertragen. Wir haben das Problem
# gelöst, indem wir mehrmals hintereinander die Zeichen in das Bus-System
# schreiben.
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

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
