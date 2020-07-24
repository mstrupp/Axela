#!/usr/bin/python
file = open('/sys/bus/w1/devices/28-0516a79b05ff/w1_slave', 'r')
file.seek(69)
temp = float(file.read(5))
file.close()

print(temp / 1000)