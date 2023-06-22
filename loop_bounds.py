# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:17:17 2023

@author: rowan
"""

chunck_size = 32 
lower_loop_bound = 0

for i in range(10): 
    
    upper_loop_bound = (lower_loop_bound) + (chunck_size - 1) 
    
    print(lower_loop_bound, upper_loop_bound)
    
    lower_loop_bound = upper_loop_bound + 1