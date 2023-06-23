# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:15:17 2023

@author: rowan twilley

per colomn processing method. 
"""

import numpy as np
from PIL import Image
from tkinter import filedialog
import tkinter as tk

def image_selector():
    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost",True)
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg")])
    
    return image_path

def save_image(modified_image): 
    file_name = input("Enter the save file name :")
    modified_image.save("C:\github\image_processing_python\processed_images(after correction)\\" + file_name + ".jpg")
    
def main(): 
    
    # Set the random seed
    np.random.seed(100)

    # Open the image file
    selected_image = image_selector()
    image = Image.open(selected_image)

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
    
    #save the image to the destination file location
    save_image(modified_image)

if __name__ == "__main__": 
    main()
