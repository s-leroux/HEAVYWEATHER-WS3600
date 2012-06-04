#
# Read an decode HeavyWeather WS3600 history
# data file
# by Sylvain Leroux - www.chicoree.fr
#
# This example code is in the public domain.
#

import struct

f = open("history.dat", "rb")

try:
    s = struct.Struct("<dffflfffffffl")
    while True:
	record = f.read(56)
	if len(record) != 56:
	    break;
    
	print s.unpack(record)

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    f.close()
