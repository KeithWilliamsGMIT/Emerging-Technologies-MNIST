# Author: Keith Williams
# Date: 23/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

file = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

print(file.read(1))

file.close();