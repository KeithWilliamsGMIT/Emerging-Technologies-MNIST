# Emerging-Technologies-MNIST

This repository contains the solutions to the second problem sheet on the MNIST dataset, given as part of my fourth year [emerging technologies](https://emerging-technologies.github.io/) module in college. Note that the solutions to these problems were written in Python 3.5.

## Problems to solve

#### 1. Read the data files

Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

#### 2. Output an image to the console

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

#### 3. Output the image files as PNGs

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png.

## Getting Started

Clone the repository and navigate to the root.

```
git clone https://github.com/KeithWilliamsGMIT/Emerging-Technologies-MNIST.git
cd Emerging-Technologies-MNIST
```

Next, download the following files from the [MNIST website](http://yann.lecun.com/exdb/mnist/) into the data folder at the root of the repository.

| Description         | Size            | Save as                    |
|---------------------|-----------------|----------------------------|
| training set images | (9912422 bytes) | train-images-idx3-ubyte.gz |
| training set labels | (28881 bytes)   | train-labels-idx1-ubyte.gz |
| test set images     | (1648877 bytes) | t10k-images-idx3-ubyte.gz  |
| test set labels     | (4542 bytes)    | t10k-labels-idx1-ubyte.gz  |

Note that the files must be saved as the name provided in the above table. This solution requires the numpy and pillow libraries. The easiest way to install these is through [Anaconda](https://www.anaconda.com/download/). Finally, use the following command to run the solution.

```
python3 mnist-reader.py
```

The images from the MNIST dataset will be outputted in PNG format to the images folder at the root of the repository.