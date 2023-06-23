# -*- coding: utf-8 -*-
"""
Created: April 2023

@author: rowan twilley 

Description: 

Image --> bin file 
    
This script converts a color image(3 channel RGB, 8 bit per channel) of any si-
ze to a binary file. The purpose of this is to make an image suitable for proc-
essing in VHDL. Raw Bit map output. 

"""

from PIL import Image
import numpy as np
import logging
import tkinter as tk
from tkinter import filedialog

def convert_image_to_bin_file(image_path, output_file):
    """
    @docstring: 
    Convert a color image to a binary file.

    Args:
        image_path (str):       Path to the input image file.
        output_file (str):      Path to save the output binary file.

    Returns:
        numpy.ndarray or None: The flattened image array if conversion is successful, else None.
    """
    
    try:
        # Open the image file
        img = Image.open(image_path)

        # Get the dimensions of the image
        width, height = img.size

        # Convert the image to a numpy array
        img_array = np.array(img)

        # Check if the image has three color channels
        if len(img_array.shape) != 3 or img_array.shape[2] != 3:
            error_msg = "Invalid image format. Expected a color image with three channels."
            logging.error(error_msg)
            return None

        # Flatten the image array
        flattened_array = img_array.flatten()

        # Save the pixel values to a binary file
        with open(output_file, "wb") as f:
            f.write(bytearray(flattened_array))

        return flattened_array

    except FileNotFoundError:
        logging.error("Input image file not found: %s", image_path)
    except Exception as e:
        logging.error("An error occurred during image conversion: %s", e)

    return None 


def main():
    
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()
    
    #set the window to focus and to be ontop of all other open windows on the computer
    root.focus_force()
    root.attributes("-topmost",True)
    
    # Prompt the user to select an image file
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg")])
    
    # Specify the input image path
    # image_path = "pakistan_sat_img.jpg"
    
    if image_path:
       
       # Specify the output file path for the binary image
       output_file = r"image_binaries\image_1.bin"

       # Convert the image and get the flattened array
       flattened_array = convert_image_to_bin_file(image_path, output_file)

       # Print the flattened array if conversion was successful, for testing purposes
       if flattened_array is not None:
        binary_array = bytearray(flattened_array[:20])
    print(binary_array.__str__())
        
if __name__ == "__main__":
    main()
