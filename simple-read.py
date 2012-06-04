
# the 'b' modifier is used to prevend erroneous
# conversion of end-of-line characters on some platforms.
f = open("history.dat", "rb")

try:
    while True:
	bytes = f.read(1)
	if bytes == "":
	    break;
	# Do stuff with byte
	# e.g.: print as hex
	print "%02X " % ord(bytes[0]) 

except IOError:
	# Your error handling here
	# Nothing for this example
	pass
finally:
    f.close()
