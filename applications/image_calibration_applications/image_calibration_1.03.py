# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:46:04 2023

@author: rowan twilley 

per 32 pixel chunks processing method.
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
num_rows, num_columns, num_channels = image_array.shape

A = 1 / (np.random.randn(num_columns) * (0.1) + 1)
B = (-1) * np.random.randint(10, size=(num_columns))

# Reshape A and B to match the block size (32 pixels)
block_size = 32
num_blocks = num_columns // block_size

A_blocks = A[:num_blocks * block_size].reshape(num_blocks, block_size)
print("A blocks shape", A_blocks.shape)
B_blocks = B[:num_blocks * block_size].reshape(num_blocks, block_size)
print("B_blocks shape", B_blocks.shape)

# Process 32-pixel blocks
# for row in range(num_rows):
#     for block in range(num_blocks):
#         start_col = block * block_size
#         end_col = (block + 1) * block_size
#         image_array[row, start_col:end_col] = A_blocks[block] * image_array[row, start_col:end_col] + B_blocks[block]

# Process remaining pixels
# start_col = num_blocks * block_size
# end_col = num_columns
# image_array[:, start_col:end_col] = A[start_col:end_col] * image_array[:, start_col:end_col] + B[start_col:end_col]

# Create a PIL image from the modified NumPy array
# modified_image = Image.fromarray(image_array.astype(np.uint8))

# Display the altered image using PIL
# modified_image.show()



