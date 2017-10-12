# Author: Keith Williams
# Date: 23/09/2017

import time
from models import MnistDataSet

if __name__ == '__main__':
	# Load the training data set.
	print('Loading training set...')
	start_time = time.time()
	train_set = MnistDataSet('train', 'data/train-images-idx3-ubyte.gz', 'data/train-labels-idx1-ubyte.gz')
	print('Elapsed time: '  +str(time.time() - start_time))
	
	# Load the test data set.
	print('Loading test set...')
	start_time = time.time()
	test_set = MnistDataSet('test', 'data/t10k-images-idx3-ubyte.gz', 'data/t10k-labels-idx1-ubyte.gz')
	print('Elapsed time: '  +str(time.time() - start_time))
	
	# Output the third image in the training set to the console.
	train_set.print_to_console(2)
	
	# Save all images in the training and test data sets.
	
	print('Saving all images...')
	train_set.save_all_images()
	test_set.save_all_images()