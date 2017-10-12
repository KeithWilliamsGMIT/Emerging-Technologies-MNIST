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
			# Read the first four bytes i.e. the magic number (should be 2051).
			magic = int.from_bytes(file.read(4), 'big')

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
			self.images = [[[int.from_bytes(file.read(1), byteorder='big') for i in range(cols)] for j in range(rows)] for k in range(number_of_images)]
	
	# Parse all labels in the given file to a list.
	def parse_labels(self, labels_file_path):
		# Open the label gzip in read bytes mode.
		with gzip.open(labels_file_path, 'rb') as file:
			# Read the first four bytes i.e. the magic number (should be 2049).
			magic = int.from_bytes(file.read(4), 'big')

			# Read the next four bytes i.e. the number of labels.
			number_of_labels = int.from_bytes(file.read(4), 'big')

			print("Magic number: " + str(magic))
			print("Number of labels: " + str(number_of_labels))
			
			self.labels = [int.from_bytes(file.read(1), 'big') for i in range(number_of_labels)]
	
	# Output the image to the console by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.
	def print_to_console(self, index):
		# Draw the image.
		for i in range(len(self.images[index])):
			for j in range(len(self.images[index][i])):
				print('.' if self.images[index][i][j] < 128 else '#', end='')
			
			print()
		
		# Output the label too.
		print('Label: ' + str(self.labels[index]))
	
	# Save all of the labelled images as PNGs.
	def save_all_images(self):
		for i in range(len(self.images)):
			self.save_png(i)
	
	# Save the image at the given index as a PNG in a subfolder called images.
	# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png
	# 	1) Where XXXXX is the image number (where it occurs in the data file).
	#	2) Where Y is its label.
	# For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png.
	def save_png(self, index):
		img = pil.fromarray(np.array(self.images[index], dtype='uint8'))
		img = img.convert('RGB')
		img.save('images/%s-%05i-%d.png' % (self.name, index, self.labels[index]))