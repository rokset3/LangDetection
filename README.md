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
1) KSC (published by ISSAI open-source kazakh speech corpus dataset)
2) Rus Parsed from wikipedia articles
3) Kaz parsed from wikipedia articles
4) Russian Jokes dataset (https://github.com/Koziev/NLP_Datasets)
5) Parsed from (http://testent.ru/load/ucheniku/kazakhskij_jazyk/audio_dialogi_na_kazahskom_jazyke_s_perevodom/26-1-0-3871) Ru \& Kaz dialogue dataset
  
