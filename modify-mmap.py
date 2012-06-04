#
# Modify a HeavyWeather WS3600 history
# by adjusting the temperature by 1.4 deg. C
#
# Modify the memory mapped data file
#
# by Sylvain Leroux - www.chicoree.fr
#
# This example code is in the public domain.
#

import struct
import datetime
import mmap

# source file to read an modify (r+)b
f = open("history.dat", "r+b")

try:
    # Record struct format
    s = struct.Struct("<dffflfffffffl")

    # Memory map the whole file (size = 0)
    map = mmap.mmap(f.fileno(),0)

    # Walk record by record throught the address space
    for idx in xrange(0, map.size(), 56):
	# Unpack the current record and adjust it
	fields = s.unpack(map[idx:idx+56])
	adjusted = list(v+1.4 if i == 9 else v for i,v in enumerate(fields))
	
	# Encode the record
	map[idx:idx+56] = s.pack(*adjusted)

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    map.close()  # unmap
    f.close()    # close the file
