# -*- coding: utf-8 -*-
"""PubMed_Abstract_TJA_Denoising.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qC-y49_YjuieokZDboosi21qesfElcMH
"""

############################################################################
# PubMed Abstracts: Denoising
############################################################################

# Mounting your Google Drive

from google.colab import drive
drive.mount('/content/drive')

import re
f = open('/content/drive/MyDrive/dataset.txt')
text = f.read()
f.close()
text = text.replace('\n', 'BLANK')
try:
    marker1 = 'Author information:'
    marker2 = 'DOI:'
    regexPattern = marker1 + '(.+?)' + marker2
    #regexCommentPattern = "Comment (in|on) .* (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).{15,25}\."
    abtracts = re.findall(regexPattern, text)

    f = open('/content/drive/MyDrive/dataset_output.txt', 'w')
    skip = False
    output = ''
    #counter =1
    for abtract in abtracts:
        #f.write(str(counter) + ':\n').
        #counter+=1
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
                    f.write(line)
        f.write('\n=========================\n')
    f.close()
except AttributeError:
    str_found = 'Nothing found between two markers'