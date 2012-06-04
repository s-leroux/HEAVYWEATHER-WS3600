#
# Modify a HeavyWeather WS3600 history
# by adjusting the temperature by 1.4 deg. C
#
# Modify the data file /in place/
#
# by Sylvain Leroux - www.chicoree.fr
#
# This example code is in the public domain.
#

import struct
import datetime
import os

# source file to read an modify (r+)b
f = open("history.dat", "r+b")

try:
    # Record struct format
    s = struct.Struct("<dffflfffffffl")

    while True:
	# Read a record from the file
	record = f.read(56)
	if len(record) != 56:
	    break;

	# Adjust data
	fields = s.unpack(record)
	adjusted = list(v+1.4 if i == 9 else v for i,v in enumerate(fields))
	
	# Encode the record
	record = s.pack(*adjusted)
    
	# ''Rewind'' the file one record back
	f.seek(-56,os.SEEK_CUR);

	# Overwrite the record with the modified version
	f.write(record)

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    f.close()
