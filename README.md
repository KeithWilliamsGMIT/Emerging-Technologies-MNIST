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

Clone the repository and navigate to the root of the repository.

```
git clone https://github.com/KeithWilliamsGMIT/Emerging-Technologies-MNIST.git
cd Emerging-Technologies-MNIST
```

Next, download the following files from the [MNIST website](http://yann.lecun.com/exdb/mnist/) into a folder called data in the root of the repository.
+ training set images (9912422 bytes) 
+ training set labels (28881 bytes) 
+ test set images (1648877 bytes) 
+ test set labels (4542 bytes)

Create another new folder called images in the root of the repository. Finally, use the following command to run the solution.

```
python3 mnist-reader.py
```