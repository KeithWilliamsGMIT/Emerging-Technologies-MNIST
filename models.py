# Author: Keith Williams
# Date: 27/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python

import gzip

class MnistDataSet:
	# __init__ is called when the object is created.
	# Assign values to this objects images_file_path and labels_file_path values.
	def __init__(self, images_file_path, labels_file_path):
		self.images_file_path = images_file_path
		self.labels_file_path = labels_file_path
	
	def parse_files(self):
		# Open the gzip in read mode.
		images_file = gzip.open(self.images_file_path, 'rb')

		# Read the first four bytes i.e. the magic number.
		magic = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of images.
		number_of_images = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of rows.
		rows = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of cols.
		cols = self.read_next_integer_from_file(images_file, 4)

		# Read all the images in the images file.
		images = self.read_all_images(images_file, number_of_images, rows, cols)

		print("Magic number: " + str(magic))
		print("Number of images: " + str(number_of_images))
		print("Number of rows: " + str(rows))
		print("Number of cols: " + str(cols))
		print("Total images read: " + str(len(images)))

		# Close the gzip file.
		images_file.close()
	
	# Read the next given number of bytes from the given file.
	# Convert these bytes to an int and return the integer value.
	def read_next_integer_from_file(self, file, number_of_bytes):
		value = file.read(number_of_bytes)
		return int.from_bytes(value, byteorder='big')

	# Read the next image in the given file.
	# Return a 2D list of integers representing the pixels in the image.
	# According to the MNIST website:
	#	"Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black)."
	def read_next_image(self, images_file, rows, cols):
		pixels = []

		for i in range(rows):
			row = []

			for j in range(cols):
				pixel = self.read_next_integer_from_file(images_file, 1)
				row.append(pixel)

			pixels.append(row)

		return pixels

	# Read all the images in the given file.
	# Return a list of LabelledImage object.
	def read_all_images(self, images_file, number_of_images, rows, cols):
		images = []

		for i in range(number_of_images):
			image = self.read_next_image(images_file, rows, cols)
			images.append(LabelledImage(image, 0))

		return images

class LabelledImage:
	# __init__ is called when the object is created.
	# Assign values to this objects image and label values.
	def __init__(self, image, label):
		self.image = image
		self.label = label