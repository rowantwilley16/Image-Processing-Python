# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:37:27 2023

@author: rowan twilley

per row processing method.
"""

import numpy as np
from PIL import Image

# Set the random seed
np.random.seed(100)

# Open the image file
image = Image.open(r"processed_images\raw_sat_img.jpg")

# Convert the image to RGB mode if necessary
if image.mode != 'RGB':
    image = image.convert('RGB')

# Convert the image to a NumPy array
image_array = np.array(image)

# Generate random Gaussian array (A) and random integer array (B)
num_columns = image_array.shape[1]

A = 1/ (np.random.randn(num_columns)*(0.1) + 1)
A = A.reshape(-1, 1)
A = np.tile(A, (1, 3))

B = (-1)*np.random.randint(10,size=(num_columns))
B = B.reshape(-1, 1)
B = np.tile(B, (1, 3))

# Iterate over each row and modify the pixel intensities per column
for row in range(image_array.shape[0]):
    image_array[row, :, :] = A * image_array[row, :, :] + B

# Create a PIL image from the modified NumPy array
modified_image = Image.fromarray(image_array)

# Display the altered image using PIL
modified_image.show()



