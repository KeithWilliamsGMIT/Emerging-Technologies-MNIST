# Author: Keith Williams
# Date: 23/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python

import gzip

# Read the next given number of bytes from the file.
# Convert these bytes to an int.
# Return the integer value.
def get_next_integer(number_of_bytes):
	value = file.read(number_of_bytes)
	return int.from_bytes(value, byteorder='big')

# Read the next image in the file.
# Return a 2D list of integers representing the pixels in the image.
# According to the MNIST website:
#	"Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black)."
def get_next_image(rows, cols):
	pixels = []
	
	for i in range(rows):
		row = []
		
		for j in range(cols):
			pixel = get_next_integer(1)
			row.append(pixel)
		
		pixels.append(row)
	
	return pixels

# Read all the images in the file.
# Return the images in a list.
def read_all_images(number_of_images, rows, cols):
	images = []
	
	for i in range(number_of_images):
		image = get_next_image(rows, cols)
		images.append(image)
	
	return images

# Open the gzip in read mode
file = gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb')

# Read the first four bytes i.e. the magic number
magic = get_next_integer(4)

# Read the next four bytes i.e. the number of images
number_of_images = get_next_integer(4)

# Read the next four bytes i.e. the number of rows
rows = get_next_integer(4)

# Read the next four bytes i.e. the number of cols
cols = get_next_integer(4)

# Read all the images in the file.
images = read_all_images(number_of_images, rows, cols)

print(magic)
print(number_of_images)
print(rows)
print(cols)
print(len(images))

# Close the gzip file
file.close()