#!/usr/bin/python
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

