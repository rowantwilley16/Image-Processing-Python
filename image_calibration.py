# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:15:17 2023

@author: rowan twilley
"""

import numpy as np
from PIL import Image

# Set the random seed
np.random.seed(100)

# Open the image file
image = Image.open(r"processed_images\raw_sat_img.jpg")

if image.mode != 'RGB':
    image = image.convert('RGB')

image_array = np.array(image)

num_columns = image_array.shape[1]

A = 1/(np.random.randn(num_columns)*(0.1) + 1)
B = (-1)*np.random.randint(10,size=(num_columns))

for col in range(num_columns):
    image_array[:, col, :] = A[col] * image_array[:, col, :] + B[col]

modified_image = Image.fromarray(image_array)
modified_image.show()
