import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import feature_extraction
from sklearn.naive_bayes import MultinomialNB
from sklearn import pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
import os
import itertools
import joblib

import warnings
warnings.filterwarnings("ignore")


print('Creating runs folder. Trained model will be saved there')
directory = os.getcwd()
try:
    os.makedirs(directory + r'/runs/train', exist_ok=True)
except FileExistsError:
    # directory already exists
    pass
print('Success!')

#Getting data
print('Getting data...')
data = pd.read_csv(directory+r'/dataset/data.csv')
data.dropna(axis=0, inplace=True)
x = data['Text']
y = data['Language']


print('Splitting the data')
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=.2, random_state=42, stratify=y)

vectorizer = feature_extraction.text.TfidfVectorizer(ngram_range=(1,3), analyzer='char')
print('Success!')


print('Start Training...')
pipeMNB = pipeline.Pipeline([      #pipeline to transform data and pass it to the model
    ('vectorizer', vectorizer),
    ('clf', MultinomialNB())
]).fit(xTrain, yTrain)
print('Success!')

MNBPreds = pipeMNB.predict(xTest)
print('Training results')
print('MNB results \n' +  metrics.classification_report(MNBPreds, yTest))
print('ROC AUC: {}\n F1: {}'.format(metrics.roc_auc_score((MNBPreds=='Russian'),yTest == 'Russian'),
                                    metrics.f1_score((MNBPreds=='Russian'), (yTest == 'Russian'))))

print('Saving model to /runs/train')
joblib.dump(pipeMNB, directory +r'/runs/train/model.pkl')


