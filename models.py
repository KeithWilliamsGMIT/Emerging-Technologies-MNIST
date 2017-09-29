# Author: Keith Williams
# Date: 27/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python

import gzip
import numpy as np
import PIL.Image as pil

class MnistDataSet:
	# __init__ is called when the object is created.
	# Assign values to this objects name, images_file_path, labels_file_path and labelled_images values.
	def __init__(self, name, images_file_path, labels_file_path):
		self.name = name
		self.images_file_path = images_file_path
		self.labels_file_path = labels_file_path
		self.labelled_images = []
	
	def parse_files(self):
		# Open the image gzip in read mode.
		images_file = gzip.open(self.images_file_path, 'rb')

		# Read the first four bytes i.e. the magic number (should be 2051).
		magic = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of images.
		number_of_images = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of rows.
		rows = self.read_next_integer_from_file(images_file, 4)

		# Read the next four bytes i.e. the number of cols.
		cols = self.read_next_integer_from_file(images_file, 4)

		print("Magic number: " + str(magic))
		print("Number of images: " + str(number_of_images))
		print("Number of rows: " + str(rows))
		print("Number of cols: " + str(cols))
		
		# Open the label gzip in read mode.
		labels_file = gzip.open(self.labels_file_path, 'rb')

		# Read the first four bytes i.e. the magic number (should be 2049).
		magic = self.read_next_integer_from_file(labels_file, 4)

		# Read the next four bytes i.e. the number of labels.
		number_of_labels = self.read_next_integer_from_file(labels_file, 4)

		print("Magic number: " + str(magic))
		print("Number of labels: " + str(number_of_labels))
		
		# Read all the images and labels byte by byte.
		self.read_all_labelled_images(images_file, labels_file, number_of_images, rows, cols)
		
		# Close the label gzip file.
		images_file.close()
		
		# Close the image gzip file.
		labels_file.close()
	
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

	# Read all the images and labels in the given files.
	def read_all_labelled_images(self, images_file, labels_file, number_of_labelled_images, rows, cols):
		for i in range(number_of_labelled_images):
			image = self.read_next_image(images_file, rows, cols)
			label = self.read_next_integer_from_file(labels_file, 1)
			self.labelled_images.append(LabelledImage(image, label))
	
	# Save the image as a PNG in a subfolder.
	# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png
	# 	1) Where XXXXX is the image number (where it occurs in the data file).
	#	2) Where Y is its label.
	# For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png.
	def save_png(self, index):
		img = pil.fromarray(np.array(self.labelled_images[index].image, dtype='uint8'))
		img = img.convert('RGB')
		img.show()
		img.save('images/%s-%05i-%d.png' % (self.name, index, self.labelled_images[index].label))

class LabelledImage:
	# __init__ is called when the object is created.
	# Assign values to this objects image and label values.
	def __init__(self, image, label):
		self.image = image
		self.label = label
	
	# Output the image to the console by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.
	def print_to_console(self):
		# Draw the image.
		for i in range(len(self.image)):
			for j in range(len(self.image[i])):
				print('.' if self.image[i][j] < 128 else '#', end='')
			
			print()
		
		# Output the label too.
		print('Label: ' + str(self.label))