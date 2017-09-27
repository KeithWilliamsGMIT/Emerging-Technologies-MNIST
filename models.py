# Author: Keith Williams
# Date: 27/09/2017

class LabelledImage:
	# __init__ is called when the object is created.
	# Assign values to this objects image and label values.
	def __init__(self, image, label):
		self.image = image
		self.label = label