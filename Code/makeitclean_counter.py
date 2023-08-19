# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:40:14 2023

@author: user
"""

# with open('C:/Users/user/Desktop/Ahmad/Abstract_cleaned.txt', 'r', encoding="utf-8") as fp:
#     for count, line in enumerate(fp):
#         print("Abstract",count)
#         print(line)

import re
f = open("C:/Users/user/Desktop/Ahmad/dataset_output.txt", 'r', encoding="utf-8")
text = f.read()
f.close()
text = text.replace('BLANK', '')


try:
    marker1 = 'ABSTARCT'
    marker2 = 'ABSTARCT'
    regexPattern = marker1 + '(.+?)' + marker2
    #regexCommentPattern = "Comment (in|on) .* (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).{15,25}\."
    abtracts = re.findall(regexPattern, text)

    f = open('C:/Users/user/Desktop/Ahmad/Abstract_cleaned_3.txt', 'w', encoding="utf-8")
    skip = False
    output = ''
    #counter =1
    for count ,abtract in  enumerate(abtracts):
        article = abtract.replace('HexAI', '\n')
        for line in article.split('\n'):
            if len(line) > 1:
                if skip:
                  if(line[len(line)-1] != '.'): # to skip the second, third line of author informations
                    skip = True
                    continue
                  else:
                    skip = False
                    continue
                if (line[0] == '(' and line[1].isdigit() and line[2].isdigit() and line[3] == ')')  or (line[0]== '(' and line[1].isdigit() and line[2] == ')') :
                    if(line[len(line) -1] == '.'):  # to fix online author information
                      skip = False
                    else:
                      skip = True
                else:
                    f.write(str(count+1)+':: '+line)
        f.write('\n')
    f.close()
except AttributeError:
    str_found = 'Nothing found between two markers'        
    
 