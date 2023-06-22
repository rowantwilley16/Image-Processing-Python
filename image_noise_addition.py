# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:53:57 2023

@author: rowan twilley 

@description:   This script takes in reads in an image and displays it. It adds 
                an f(x) = Ax + B offset to each colomn of pixels. 
"""

import numpy as np 
import logging 
import tkinter as tk
from tkinter import filedialog
from PIL import Image 

def setup_logging_config():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
def image_selector():
    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost",True)
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg")])
    
    return image_path

def display_image(image_array): 
    image = Image.fromarray(image_array)
    image.show()
    
def alter_colomns(noisy_image, image_array,gain_array,offset_array,width):
    
    for i in range(0,width):
        noisy_image[:,i,:] = np.maximum(np.minimum(image_array[:,i,:]*gain_array[i]+offset_array[i], 255), 0)
        
    return noisy_image
   
def add_noise(image_path):
    
    try:  
        np.random.seed(100)
        
        img = Image.open(image_path)
        width, height = img.size
        channels = 3
        
        #dtype float in order to do calculations without the under/overflowing during multiplication
        image_array = np.array(img, dtype=float) 
        noisy_image = np.zeros((height, width, channels), dtype=np.uint8)
        
        #gain and offset co-efficent arrays
        gain_array = np.random.randn(width)*(0.1) + 1
        offset_array = np.random.randint(10,size=(width))
        
        #check if the image is in the correct format
        if len(image_array.shape) != 3 or image_array.shape[2] != 3:
            error_msg = "Invalid image format. Expected a color image with three channels."
            logging.error(error_msg)
            return None
        
        noisy_image = alter_colomns(noisy_image, image_array,gain_array, offset_array,width)
            
        return noisy_image
    
    except Exception as e:
         logging.error("An error occurred during image conversion: %s", e)
        
    return None
def convert_image_to_bin_file(img_array):
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
        #specify the output file path
        output_file_name = get_file_name()
        output_file_path = get_output_image_path(output_file_name)
        
        # Flatten the image array
        flattened_array = img_array.flatten()

        # Save the pixel values to a binary file
        with open(output_file_path, "wb") as f:
            f.write(bytearray(flattened_array))
        logging.info("Image sucessfully saved as a bin file.")
        return flattened_array

    except FileNotFoundError:
        logging.error("Input image file not found: %s", image_path)
    except Exception as e:
        logging.error("An error occurred during image conversion: %s", e)

    return None

def get_file_name():
    
    output_file_name = input("Enter the filename for the saved file : \n")
    return output_file_name

def get_output_image_path(output_file_name):
    
    return r"image_binaries\\"+ output_file_name +".bin"

def main(): 
    
    image_path = image_selector()
    
    if image_path:
        logging.info("Image Sucessfully opened")
        noisy_image = add_noise(image_path)
        display_image(noisy_image)
        
        flattened_array = convert_image_to_bin_file(noisy_image)

#        if flattened_array is not None:
#            binary_array = bytearray(flattened_array[:20])
#            print(binary_array.__str__())
        
if __name__ == "__main__": 
    main()

