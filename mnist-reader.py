# Author: Keith Williams
# Date: 23/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python

import gzip

# Open the gzip in read mode
file = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

# Read the first four bytes i.e. the magic number
magic = file.read(4)

# Convert the magic number from bytes to an int
magic = int.from_bytes(magic, byteorder='big')

print(magic)

file.close();