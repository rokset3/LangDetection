# LangDetection

To inference: !python inference.py -m \<mode\> 

Currently, there are 3 modes available: 'txt', 'csv' and 'string'

in 'txt' mode upload a txt file into /inference/txt, then run inference script. Model will use pretrained weights (runs/train/model.pkl) and output csv file with text - class output 

in 'csv' mode upload a csv file into /inference/csv, then run inference script. NOTE: currently script accepts csv files with .shape = (n,1), so please, upload csv file containing text only 

in 'string' mode, input string to be detected into console. the output of detection will be printed in the console. 

There are other two scripts: 

dataprep.py - to collect all datasets into final training dataset

train.py - trains model with .20 test_size via Multinomial Naive Bayes classifier with default tuning on dataset created by dataprep.py

Datasets have not been uplodaded due to size, but they can be accessed, as I uploaded them to Drive (PM if you are interested)

Used datasets:

  
