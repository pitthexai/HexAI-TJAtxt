# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:20:18 2023

@author: user
"""
# importing pandas library
import pandas as pd

# reading the given csv file 
# and creating dataframe
account = pd.read_csv(r"C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.txt", encoding="utf-8", delimiter = '::',engine='python',header = None)
account.columns = ['Index','Abstracts']  
  
# store dataframe into csv file
account.to_csv('C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.csv', encoding='utf-8', index= None)