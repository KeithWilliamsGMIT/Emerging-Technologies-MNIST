# Author: Keith Williams
# Date: 23/09/2017

from models import MnistDataSet

if __name__ == '__main__':
	print("Parsing training set...")
	train_set = MnistDataSet('train', 'data/train-images-idx3-ubyte.gz', 'data/train-labels-idx1-ubyte.gz')
	train_set.parse_files()
	
	print("Parsing test set...")
	test_set = MnistDataSet('test', 'data/t10k-images-idx3-ubyte.gz', 'data/t10k-labels-idx1-ubyte.gz')
	test_set.parse_files()
	
	# Output the third image in the training set to the console.
	train_set.labelled_images[2].print_to_console()
	
	# Save all images in the training and test data sets.
	train_set.save_all_images()
	test_set.save_all_images()