# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 22:42:44 2023

@author: user
"""

import pandas as pd

# reading the given csv file 
# and creating dataframe
abstract = pd.read_csv(r"C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.txt", encoding="utf-8", delimiter = '::',engine='python',header = None)
abstract.columns = ['Index','Abstracts']  
output_file = "C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.xlsx"

abstract.to_excel(output_file, index=False, header=True, engine='openpyxl')