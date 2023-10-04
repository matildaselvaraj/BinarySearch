# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:02:42 2023

@author: ninae
"""

import numpy as np
'''
def checkforprime(numb):
    iterations = numb-1
    #iterations = np.floor(np.sqrt(numb))
    for i in range(2, int(iterations) + 1):
        if numb%i == 0:
            return f' {numb} is not a prime'    
    return f' {numb} is a prime' 
'''            



numb = int(input('Sätt in ett tal '))

iterations = np.floor(np.sqrt(numb))
for i in range(2, int(iterations)):
    if numb%i == 0:
        f'{numb} is not a prime'    
f' {numb} is a prime' 


