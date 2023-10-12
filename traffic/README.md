# Traffic Sign Detector
This program trains a traffic sign detector, which can take an image of traffic signs as an input and output what traffic sign is present in the image.

## Libraries
- cv2
- numpy
- os
- sys
- tensorflow
- sklearn

To install these dependencies, run `pip3 install -r requirements.txt` in the command line

## Summary
This is a program written in Python 3. It uses a Convolutional Neural Network to train a model that can accurately identify stop signs from mixed traffic signs. The program will save the trained model in a file which can then be used to detect what kind of traffic sign is present in images. This is a feed forward neural network with 1 convolutional layer, 1 max pooling layer and 1 hidden layer, with 128 nodes. Feel free to edit the number of layers present in the `get_model()` function. A model.h5 file is included of an already trained model if you would like to use it straight away in your code.

## Features
- Takes an image file of a stop sign as an input and outputs whether it is a stop sign or not
- Utilizes the Convolutional Neural Network to train the model
- Saves the trained model to a .h5 file


## Usage
- Clone repository to local machine
- Run `pip3 install -r requirements.txt` to install dependencies
- Run `python3 traffic.py [data_directory] [model.h5]` to train the model and save to .h5 file

## Dataset
The dataset used for training (and testing) the model is the German Traffic Sign Recognition Benchmark. If you wish to use the dataset, please download it from https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/data