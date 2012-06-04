#
# Read an decode HeavyWeather WS3600 history
# data file
# by Sylvain Leroux - www.chicoree.fr
#
# This example code is in the public domain.
#

import struct
import datetime

import pytz

f = open("history.dat", "rb")

try:
    origin = datetime.datetime(1899,12,30,0,0,0, tzinfo=pytz.utc)
    min = None
    max = None

    s = struct.Struct("<dffflfffffffl")
    while True:
	record = f.read(56)
	if len(record) != 56:
	    break;

	fields = s.unpack(record)
	(timestamp,temp) = (fields[i] for i in (0,8))
	
	# adjust date
	timedelta = datetime.timedelta(timestamp)
	date = origin + timedelta

	# Record min and max
	if min is None or min[1] > temp:
	    min = (date, temp)
	if max is None or max[1] < temp:
	    max = (date, temp)

    print "min", min
    print "max", max

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    f.close()
