#!/usr/bin/python

# readTemperature.py
# Auslesen der Temperatur eines DS18B20
#
# Das Skript liest die Temperatur aus der entsprechenden Datei des 1-Wire Busses aus. 
# Zuerst wird die Datei im Lese-Modus geöffnet. Dann wird in der Datei mit file.seek(69) 
# zur Position der Temperatur navigiert. Die Temperatur wird als fünfstellige Zahl ausgegeben. 
# Die ersten zwei Ziffern sind die Vorkommastellen und die letzten drei Ziffern die 
# Nachkommestellen. Deshalb wird die ausgelesene Temperatur zuerst zum Typ float konvertiert 
# und dann durch 1000 geteilt. Es resultiert die aktuelle Temperatur als Kommazahl. Diese wird 
# mit “print” angezeigt und damit zurück an die php Funktion gegeben.
#
# Author: Alexander Ehre, Michael Strupp
# Date: 17.07.2020

file = open('/sys/bus/w1/devices/28-0516a79b05ff/w1_slave', 'r')
file.seek(69)
temp = float(file.read(5))
file.close()

print(temp / 1000)