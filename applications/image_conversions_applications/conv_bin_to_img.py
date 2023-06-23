# -*- coding: utf-8 -*-
"""
Created: April 2023

@author: rowan twilley

Description: 

bin file --> Image 
   
This scipt converts a binary file, to a color image(3 channel RGB, 8 bit per c-
hannel). The purpose of this is to see what a processed image looks like once 
it has been processed in VHDL. 
              
NOTE: The dimensions of the image is required to reconstruct the image from the 
      binary file. Change the width and height variables as necesary. 
"""

import numpy as np
import logging 
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def convert_binary_to_image(binary_file, output_image_path, width, height):
    """
    @docstring: 
    Convert a binary file representing an 8-bit per channel RGB color image
    back to an image array and save it as an image file.

    Args:
        binary_file (str):          Path to the input binary file.
        output_image_path (str):    Path to save the output image file.
        width (int):                Width of the output image.
        height (int):               Height of the output image.

    Returns:
        numpy.ndarray or None: The image array if conversion is successful, else None.
    """
    
    try:
        # Read the binary file
        with open(binary_file, "rb") as f:
            binary_data = f.read()

        # Calculate the expected number of pixels based on the image dimensions
        expected_pixel_count = width * height * 3

        # Check if the binary data size matches the expected pixel count
        if len(binary_data) != expected_pixel_count:
            error_msg = "Invalid binary file. The number of bytes doesn't match the specified image dimensions."
            logging.error(error_msg)
            return None

        # Convert the binary data to a numpy array
        image_array = np.frombuffer(binary_data, dtype=np.uint8)

        # Reshape the array to match the specified dimensions and color channels
        image_array = image_array.reshape((height, width, 3))

        # Create an Image object from the array
        image = Image.fromarray(image_array)

        # Save the image to the specified output path
        image.save(output_image_path)

        return image_array

    except FileNotFoundError:
        logging.error("Input binary file not found: %s", binary_file)
    except ValueError as ve:
        logging.error("An error occurred during image conversion: %s", ve)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
    return None
def setup_logging_config():
    
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")   
def image_selector():
    

    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost",True)
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.bin")])
       
    return image_path
def get_file_name():
    
    output_file_name = input("Enter the filename for the saved file : \n")
    return output_file_name
    
def get_image_dimensions():
    
    #specify the image dimensions here
    
    width = int(input("Enter the Image Width : "))  #width  = 4537
    height = int(input("Enter the Image Height : ")) #height = 5000
    
    return width, height

def get_output_image_path(output_file_name):
    return r"C:\github\image_processing_python\raw_images(after noise addition)\\" + output_file_name + ".jpg"
    
def main():
    
    setup_logging_config()
    binary_file_path = image_selector()
    output_file_name = get_file_name()
    output_image_path = get_output_image_path(output_file_name)
    width, height = get_image_dimensions()
    image_array = convert_binary_to_image(binary_file_path, output_image_path, width, height)

    # Print the image array if conversion was successful, for testing purposes
    if image_array is not None:
        print(image_array)

if __name__ == "__main__": 
    main()