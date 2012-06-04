#
# Modify a HeavyWeather WS3600 history
# by adjusting the temperature by 1.4 deg. C
#
# Store the modificationis in a new file
#
# by Sylvain Leroux - www.chicoree.fr
#
# This example code is in the public domain.
#

import struct
import datetime

# source file for reading (r)b
src = open("history.dat", "rb")

# destination file for writing (w)b
dst = open("adjusted.dat", "wb")

try:
    # Record struct format
    s = struct.Struct("<dffflfffffffl")

    while True:
	# Read a record from source file
	record = src.read(56)
	if len(record) != 56:
	    break;

	# Adjust data
	fields = s.unpack(record)
	adjusted = list(v+1.4 if i == 9 else v for i,v in enumerate(fields))
	
	# Encode the record and write it to the dest file
	record = s.pack(*adjusted)
	dst.write(record)

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    src.close()
    dst.close()
