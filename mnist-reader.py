# Author: Keith Williams
# Date: 23/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python

import gzip

# Read next four bytes from the file.
# Convert these bytes to an int.
# Return the integer value.
def get_next_integer():
	value = file.read(4)
	return int.from_bytes(value, byteorder='big')

# Open the gzip in read mode
file = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

# Read the first four bytes i.e. the magic number
magic = get_next_integer()

# Read the next four bytes i.e. the number of images
images = get_next_integer()

# Read the next four bytes i.e. the number of rows
rows = get_next_integer()

# Read the next four bytes i.e. the number of cols
cols = get_next_integer()

print(magic)
print(images)
print(rows)
print(cols)

# Close the gzip file
file.close();