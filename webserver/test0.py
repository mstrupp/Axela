#!/usr/bin/python
file = open('/sys/bus/w1/devices/29-00da24080000/output', 'w')
file.seek(0)
file.write('\x00')
file.close()
print('Ausgeschaltet.')
