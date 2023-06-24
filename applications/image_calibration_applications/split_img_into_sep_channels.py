# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:56:13 2023

@author: rowan twilley
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def split_img_into_channels(image):
    
    # Convert the image to numpy array
    image_array = np.array(image)
    
    #copy the image 
    
    red_image = image_array.copy()
    blue_image = image_array.copy()
    green_image = image_array.copy()
     
    #red 
    red_image[:, :, 1] = 0  
    red_image[:, :, 2] = 0 
    #green 
    green_image[:, :, 0] = 0  
    green_image[:, :, 2] = 0
    #blue 
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0
    
    # Separate the channels
    return image_array, red_image,green_image,blue_image   

def display_seperate_RGB_images(image_array, red_image,green_image,blue_image):
    
    # Display the original image and the individual channels
    plt.figure(figsize=(12, 4))
    
    # Original RGB image
    plt.subplot(141)
    plt.imshow(image_array)
    plt.title('Original Image')
    plt.axis('off')
    
    # Red channel
    plt.subplot(142)
    plt.imshow(red_image)
    plt.title('Red Channel')
    plt.axis('off')
    
    # Green channel
    plt.subplot(143)
    plt.imshow(green_image)
    plt.title('Green Channel')
    plt.axis('off')
    
    # Blue channel
    plt.subplot(144)
    plt.imshow(blue_image)
    plt.title('Blue Channel')
    plt.axis('off')
    
def print_line_scanned_image(updating_image):
    
    plt.figure(2,figsize=(100,4),dpi=(200))
    plt.imshow(updating_image)
    
    
def scan_image(image_array,red_image,blue_image,green_image):
    """
    Parameters
    ----------
    image_array : a number array of depth 3. 
         
    red_image : only the red channel of the original image is shown. 
        
    blue_image : a 2D nd.numpy array that only contains the blue channel of the orginal image. 
        
    green_image : a 2D numpy array thart only contains the green channel of the original image. 

    """
    #set out a blank image that will be filled over time 
    
    updating_image = image_array.copy()
    
    #initilize the temp image 
    updating_image[:,:,:] = 0 
    
    #for testing purposes
    print_line_scanned_image(updating_image)
    
    RED_FILTER_LOC      = 0 # pixel row where the red filter is applied
    BLUE_FILTER_LOC     = 500 #pixel row where the blue filter is applied 
    GREEN_FILTER_LOC    = 1000 # pixel row where the green filter is applied
    
    image_height = image_array.shape[0]
    image_width = image_array.shape[1] 
    
    IMAGING_AREA = image_height - 1; 
    #current_row_index goes from the image height downto 0 - from the bottom 
    #of the image to the top, since the imager moves over the target location from
    #bottom to top. 

    #This is the linescan code to display the image, each iteration of the for 
    #loop can be thought of as a time period that has passed. We can see that 
    #the range starts way before the imaging area and then ends way after the imaging area. 
    
    for current_row_index in range(6000, -1000, -1):
        
        if current_row_index + RED_FILTER_LOC <= IMAGING_AREA:
            updating_image[current_row_index,:,0] = red_image[current_row_index,:,0]
        
        if current_row_index + BLUE_FILTER_LOC <= IMAGING_AREA:
            updating_image[current_row_index + BLUE_FILTER_LOC,:,1] = blue_image[current_row_index+BLUE_FILTER_LOC,:,1]
        
        if current_row_index + GREEN_FILTER_LOC <=IMAGING_AREA: 
            updating_image[current_row_index + GREEN_FILTER_LOC,:,2] = green_image[current_row_index + GREEN_FILTER_LOC,:,2
                                                                                   ]
    print_line_scanned_image(updating_image)
    
def image_selector():

    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost",True)
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg")])

    return image_path

def main():
    
    # Open the image file
    image_path = image_selector()  
    image = Image.open(image_path)    
    
    image_array,red_image,green_image,blue_image = split_img_into_channels(image)
    display_seperate_RGB_images(image_array, red_image,green_image,blue_image)   

    scan_image(image_array,red_image,green_image,blue_image)
    
if __name__ == "__main__": 
    main()