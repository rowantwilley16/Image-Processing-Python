# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:49:18 2023

@author: rowan
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
A = np.random.normal(size=num_columns)
B = np.random.randint(0, 11, size=num_columns)

# Iterate over each row and modify the pixel intensities per column
for row in range(image_array.shape[0]):
    image_array[row, :, :] = A * image_array[row, :, :] + B[:, np.newaxis]

# Create a PIL image from the modified NumPy array
modified_image = Image.fromarray(image_array.astype(np.uint8))

# Display the altered image using PIL
modified_image.show()
