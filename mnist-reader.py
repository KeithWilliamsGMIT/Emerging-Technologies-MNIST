# Author: Keith Williams
# Date: 23/09/2017

from models import MnistDataSet

if __name__ == '__main__':
	test_set = MnistDataSet('data/t10k-images-idx3-ubyte.gz', 'data/t10k-labels-idx1-ubyte.gz')
	test_set.parse_files()