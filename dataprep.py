import pandas as pd 
import numpy as np
import string
from pathlib import Path
import re

import os
#create file with final Data set

directory = os.getcwd()
raw_datadir = directory+r'/raw_data'
try:
    os.makedirs(directory + r'/dataset', exist_ok=True)
except FileExistsError:
    # directory already exists
    pass

import warnings
warnings.filterwarnings("ignore")

#get all data

print('Getting Wiki Data (Kaz/Rus)...')
kazakhData = pd.read_csv(raw_datadir + r'/kazdata.txt', sep='\t', header=None, names=['Kazakh'])
russianData = pd.read_csv(raw_datadir + r'/rusdata.txt', sep='\t', header=None, names=['Russian'])\

# Creating mapping dictionary from ord(char)=>None, to remove special characters in the text

translate_table = dict((ord(char), None) for char in string.punctuation)
translate_table[ord('«')] = None
translate_table[ord('»')] = None
translate_table[ord('–')] = None
translate_table[ord('•')] = None
translate_table[ord('№')] = None
translate_table[ord('—')] = None
translate_table[ord('“')] = None
translate_table[ord('²')] = None
translate_table[ord('í')] = None
translate_table[ord('ö')] = None
translate_table[ord('ı')] = None
translate_table[ord('−')] = None
translate_table[ord('…')] = None

print('Cleaning Kaz Wiki data...')
# Data preprocessing (data parsed from Wikipedia => a lot of noise)
kazDataPrep = []
kazLang = []
for i, line in kazakhData.iterrows():
    line = line['Kazakh']
    if len(line)!=0:
        line = line.lower()
        line = re.sub(r'\d+','',line)
        line = re.sub(r'[a-zA-Z]+','',line) #removing all english characters
        line = line.translate(translate_table) 
        line = re.sub(r'^\\u$[a-zA-Z]','', line) #removing special characters from wikipedia articles
        line = re.sub(r'\ufeff','', line) #removing special characters from wikipedia articles
        line = re.sub(r'\u200b','', line) #removing special characters from wikipedia articles
        line = re.sub(r'[\u4e00-\u9fff]+','', line) #removing special characters from wikipedia articles
        line = "".join(c for c in line if c.isalpha() or c == " ")
        kazDataPrep.append(line)
        kazLang.append('Kazakh')
print('Success!')
        
print('Cleaning Rus Wiki data...')        
# Russian Data from wiki preprocessing
rusDataPrep = []
rusLang = []
for i, line in russianData.iterrows():
    line = line['Russian']
    if len(line)!=0:
        line = line.lower()
        line = re.sub(r'\d+','',line)
        line = re.sub(r'[a-zA-Z]+','',line) #removing all english characters
        line = line.translate(translate_table) 
        line = re.sub(r'^\\u$[a-zA-Z]','', line) #removing special characters from wikipedia articles
        line = re.sub(r'\ufeff','', line) #removing special characters from wikipedia articles
        line = re.sub(r'\u200b','', line) #removing special characters from wikipedia articles
        line = re.sub(r'[\u4e00-\u9fff]+','', line) #removing special characters from wikipedia articles
        line = re.sub('\n\t', '', line)
        line = "".join(c for c in line if c.isalpha() or c == " ")
        
        rusDataPrep.append(line)
        rusLang.append('Russian')
print('Success!')

print('Loading ISSAI Kazakh Corpus Dataset')
#ISSAI Kazakh Corpus dataset, no need to clean
kazDataPrep2 = pd.read_csv(raw_datadir + r'/result.txt', sep='utf-8', names=['text']) 
kazLang2 = []
for i in range(kazDataPrep2.shape[0]):
    kazLang2.append('Kazakh')
print('Success!')

print('Loading Russian Jokes Data (dialogues)...')
#Russian Dialogues data (imported from Russian jokes dataset)    
ruData2 = pd.read_csv(raw_datadir + r'/jokesData.csv',sep='utf-8',names=['text'])
ruData2
ruDataPrep2 = []
ruLang2 = []
for i, line in ruData2.iterrows():
    line = line['text']
    if len(line)!=0:
        line = line.lower()
        line = re.sub(r'\d+','',line)
        line = re.sub(r'[a-zA-Z]+','',line) 
        line = line.translate(translate_table) 
        line = re.sub(r'^\\u$[a-zA-Z]','', line) 
        line = re.sub(r'\ufeff','', line) 
        line = re.sub(r'\u200b','', line)
        line = re.sub(r'[\u4e00-\u9fff]+','', line) 
        line = "".join(c for c in line if c.isalpha() or c == " ")
        ruDataPrep2.append(line)
        ruLang2.append('Russian')
print('Success!')

print('Putting everything into one single csv file')
#Put everything in        
data = pd.DataFrame({
    'Text': rusDataPrep + ruDataPrep2 + kazDataPrep + list(kazDataPrep2['text']),
    'Language': rusLang + ruLang2 + kazLang + kazLang2
})
print('Success')

print('Concatening with dialogues dataset')
#concating with Dialogues dataset parsed from website
kazRusData = pd.read_csv(raw_datadir + '/kazrusDial.csv')
data = pd.concat([data, kazRusData])
print('Success')


print('Saving as '+directory + r'/dataset/data.csv')
#Save for further use
data.to_csv(path_or_buf=directory + r'/dataset/data.csv', index=False)
print('Done!')
