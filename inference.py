import os
import sys
import getopt
import joblib
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import feature_extraction
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
import glob
files = glob.glob(r'C:\Users\Temirlan\Desktop\Language_Detection\Transcriptions\*.txt')
import joblib
import json

import warnings
warnings.filterwarnings("ignore")

def inference(mode, model):
    
    if mode=='txt':
        if len(os.listdir(directory +r'/inference/txt/')) == 0:
            print(directory +r'/inference/txt/' + " is empty")
            sys.exit(2)    
        else:
            filename = glob.glob(directory + r'/inference/txt/*.txt')[0]
            with open(filename) as file:
                lines = file.readlines()
                text = []
                for line in lines:
                    line = line.replace('\n','')
                    text.append(line)
            data = pd.Series(text)
        predictions = pd.DataFrame()
        predictions['Text'] = data
        predictions['Language'] = model.predict(data)
        predictions.to_csv(directory + r'/runs/inference/result.csv', index=False)
        del(predictions)
        
        
    if mode=='csv':
        if len(os.listdir(directory +r'/inference/csv/')) == 0:
            print(directory +r'/inference/csv/'+" is empty")
            sys.exit(2)
        else:
            filename = glob.glob(directory + r'/inference/csv/*.csv')[0]
        data = pd.read_csv(filename)
        if 'Unnamed: 0' in data.columns:
            data.drop('Unnamed: 0', axis=1, inplace=True)
        predictions = pd.DataFrame()
        predictions['Text'] = data.iloc[:,0]
        predictions['Language'] = model.predict(data.iloc[:,0])
        predictions.to_csv(directory + r'/runs/inference/result.csv', index=False)
        del(predictions)
    
    if mode=='string':
        print('Input a string to detect')
        s = input()
        print(model.predict(pd.Series(s))[0])
            
            
def myfunc(argv):
    mode = ""
    arg_help = "{0} -m <mode (txt or word)>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hm:", ["help", "mode="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-m", "--mode"):
            mode = arg
        
    return(mode) 
        
if __name__ == "__main__":
    
    directory = os.getcwd()
    model = joblib.load(directory+r'/runs/train/model.pkl')#download trained model

    try:
        os.makedirs(directory + r'/runs/inference', exist_ok=True)
    except FileExistsError:
        # directory already exists
        pass

    mode = myfunc(sys.argv)
    inference(mode, model)
    