# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:36:37 2023

@author: rowan

Per 32 pixel chunk processing.

"""

import numpy as np
from PIL import Image

def load_into_buffer_and_process(image_chunk, A_chunk, B_chunk):

    processed_chunk = A_chunk * image_chunk + B_chunk 
    return processed_chunk 

def update_image(processed_image, processed_chunk,lower_buffer_bound,upper_buffer_bound):
    processed_image[lower_buffer_bound:upper_buffer_bound, : ] = processed_chunk
    
# Set the random seed
np.random.seed(100)

# Open the image file and show the original image
image = Image.open(r"processed_images\raw_sat_img.jpg")



# Convert the image to RGB mode if necessary
if image.mode != 'RGB':
    image = image.convert('RGB')
    
# Convert the image to a NumPy array
image_array = np.array(image)
num_rows, num_columns, num_channels = image_array.shape
image_array_2d = image_array.reshape(num_rows*num_columns,3)
processed_image = np.zeros((num_rows*num_columns,3))
# Generate random Gaussian array (A) and random integer array (B)

A = 1 / (np.random.randn(num_columns) * (0.1) + 1)
A = A.reshape(-1, 1)
A = np.tile(A, (1, 3))

B = (-1) * np.random.randint(10, size=(num_columns))
B = B.reshape(-1, 1)
B = np.tile(B, (1, 3))

chunk_size = 32 
#load the image chunk into a buffer for processing
loop_iterations_col = num_columns/chunk_size #assumes that the number of cols is divisible by the chuck_size
loop_iterations_row = num_rows

for i in range(loop_iterations_row):
    
    lower_buffer_bound = 0
    
    for i in range(int(loop_iterations_col)):
        
        upper_buffer_bound = (lower_buffer_bound) + (chunk_size - 1)
        image_chunk = image_array_2d[lower_buffer_bound:upper_buffer_bound,: ]
        A_chunk     = A             [lower_buffer_bound:upper_buffer_bound, :] 
        B_chunk     = B             [lower_buffer_bound:upper_buffer_bound, :]
        
        processed_chunk = load_into_buffer_and_process(image_chunk,A_chunk,B_chunk)
        update_image(processed_image, processed_chunk,lower_buffer_bound,upper_buffer_bound)
        
        #update buffer bounds
        lower_loop_bound = upper_buffer_bound + 1


# Create a PIL image from the modified NumPy array
modified_image = Image.fromarray(image_array.astype(np.uint8))

# Display the altered image using PIL
modified_image.show()