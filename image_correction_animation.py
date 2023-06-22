# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:53:34 2023

@author: rowan twilley

RT image processing in python

"""

#image_path = r"processed_images\raw_sat_img.jpg"  
#output_path = r"C:\Users\rowan\OneDrive\Documents\python_workspace\image_input_to_vhdl\processed_images\animation.mp4"

import imageio
import numpy as np
from PIL import Image

# Load the image
image_path = r"processed_images\raw_sat_img.jpg" 
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Get image dimensions
height, width, _ = image_array.shape

# Create a blank image to display
display_array = np.zeros((height, width, 3), dtype=np.uint8)

# Create a list to store the frames of the animation
frames = []

# Iterate over each row of the image
for row in range(height):
    # Copy the current row of pixels from the original image array
    row_pixels = np.copy(image_array[row])

    # Update the row of pixels in the display array
    display_array[:row+1] = row_pixels

    # Create an Image object from the display array
    frame = Image.fromarray(display_array)
    frames.append(frame)

# Save the frames as a video file
output_path = r"C:\Users\rowan\OneDrive\Documents\python_workspace\image_input_to_vhdl\processed_images\animation.mp4"
imageio.mimsave(output_path, frames, fps=10)  # Adjust the FPS (frames per second) as desired

print(f"Video saved successfully at '{output_path}'")






