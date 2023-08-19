# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:39:47 2023

@author: user
"""

import json

dict1 = {}
 
# fields in the sample file
fields = ['Index','Abstract']

with  open('C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.txt', 'r', encoding="utf-8") as in_file:
    
    # count variable
    n = 1
    for line in in_file:
        # reading line by line from the text file
        description = list( line.strip().split('::'))
        
        # for output see below
       # print(description)
         
        #for automatic creation of index for each abstarct
        sno ='Abstarct'+str(n)
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields):
             
                # creating dictionary for each employee
                dict2[fields[i]]= description[i]
                i = i + 1
                 
        # appending the record of each employee to
        # the main dictionary
        dict1[sno]= dict2
        n = n + 1
 
 
# creating json file       
out_file = open('C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.json', 'w', encoding="utf-8")
json.dump(dict1, out_file, indent=len(description))
out_file.close()