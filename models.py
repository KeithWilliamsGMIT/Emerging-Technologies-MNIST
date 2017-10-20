# Author: Keith Williams
# Date: 27/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#	https://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python
#	https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/learn/python/learn/datasets/mnist.py

import gzip
import numpy as np
import PIL.Image as pil

IMAGE_MAGIC_NUMBER = 2051
LABEL_MAGIC_NUMBER = 2049

class MnistDataSet:
	# __init__ is called when the object is created.
	# Assign name and parse given files.
	def __init__(self, name, images_file_path, labels_file_path):
		self.name = name
		
		# Parse files to objects.
		self.parse_images(images_file_path)
		self.parse_labels(labels_file_path)
	
	# Parse all images in the given file to a list.
	def parse_images(self, images_file_path):
		# Open the image gzip in read bytes mode.
		with gzip.open(images_file_path, 'rb') as file:
			# Read the first four bytes i.e. the magic number.
			magic = int.from_bytes(file.read(4), 'big')
			
			# Raise an exception if the magic number is incorrect (should be 2051).
			if magic != IMAGE_MAGIC_NUMBER:
				raise ValueError('Incorrect magic number value %d in MNIST image file %s! Correct value is %d.' % (magic, images_file_path, IMAGE_MAGIC_NUMBER))

			# Read the next four bytes i.e. the number of images.
			number_of_images = int.from_bytes(file.read(4), 'big')

			# Read the next four bytes i.e. the number of rows.
			rows = int.from_bytes(file.read(4), 'big')

			# Read the next four bytes i.e. the number of cols.
			cols = int.from_bytes(file.read(4), 'big')

			print("Magic number: " + str(magic))
			print("Number of images: " + str(number_of_images))
			print("Number of rows: " + str(rows))
			print("Number of cols: " + str(cols))
			
			# Read all the images in the file in sequence.
			# An image in this case is a 2D list of integers representing each pixels in the image.
			# According to the MNIST website:
			#	"Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black)."
			#self.images = [[[int.from_bytes(file.read(1), byteorder='big') for i in range(cols)] for j in range(rows)] for k in range(number_of_images)]
			
			# Using the above line, which uses nested for loops to read in images from the data file, took approximately 3 minutes for both datasets to be parsed.
			# After investigating the MNIST script used by tensorflow I found the below method.
			# This reads in the remainder of the file to a buffer that is then turned into a 3D list.
			# This method reduced the time to approximately 0.5 seconds for both datasets.
			buffer = file.read(rows * cols * number_of_images)
			data = np.frombuffer(buffer, dtype=np.uint8)
			self.images = data.reshape(number_of_images, rows, cols)
			
	# Parse all labels in the given file to a list.
	def parse_labels(self, labels_file_path):
		# Open the label gzip in read bytes mode.
		with gzip.open(labels_file_path, 'rb') as file:
			# Read the first four bytes i.e. the magic number.
			magic = int.from_bytes(file.read(4), 'big')
			
			# Raise an exception if the magic number is incorrect (should be 2049).
			if magic != LABEL_MAGIC_NUMBER:
				raise ValueError('Incorrect magic number value %d in MNIST label file %s! Correct value is %d.' % (magic, labels_file_path, LABEL_MAGIC_NUMBER))

			# Read the next four bytes i.e. the number of labels.
			number_of_labels = int.from_bytes(file.read(4), 'big')

			print("Magic number: " + str(magic))
			print("Number of labels: " + str(number_of_labels))
			
			#self.labels = [int.from_bytes(file.read(1), 'big') for i in range(number_of_labels)]
			
			# The remaining bytes in the label data file is read into a buffer.
			# This buffer is then turned into a list.
			buffer = file.read(number_of_labels)
			self.labels = np.frombuffer(buffer, dtype=np.uint8)
	
	# Output the image at the given index to the console.
	# This is achieved by representing any pixel value less than 128 as a full stop and all other pixel value as a hash symbol.
	def print_to_console(self, index):
		for i in range(len(self.images[index])):
			for j in range(len(self.images[index][i])):
				print('.' if self.images[index][i][j] < 128 else '#', end='')
			
			print()
		
		# Output the label too.
		print('Label: ' + str(self.labels[index]))
	
	# Save all of the images as PNGs.
	def save_all_images(self):
		for i in range(len(self.images)):
			self.save_png(i)
	
	# Save the image at the given index as a PNG in a subfolder called images.
	# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png
	# 	1) Where XXXXX is the image number (where it occurs in the data file).
	#	2) Where Y is its label.
	# For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png.
	def save_png(self, index):
		img = pil.fromarray(self.images[index])
		img = img.convert('RGB')
		img.save('images/%s-%05i-%d.png' % (self.name, index, self.labels[index]))