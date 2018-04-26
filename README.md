# SMM-project
Social Media Mining


Copy /LocationEntityExtraction/processedDataset/pointOfInterests.csv to /TwitterDataTourism-sentimentnalysiswith1.6M/Raw_data/pointOfIntersts.csv




-  GetTopTourstSpots.ipynb
This file describes the process of executing the GetTopTouristSpots.ipynb

Requirements for executing:- 
- Python 3.0
- Executable in Jupyter notebook

Python Packages: 
- pandas
- urllib.request
- json
- pprint
- everygrams from NLTK
- word_tokenzie from NLTK
- stopwords from NLTK.corpus
- defaultdict from collections
- joblib from sklearn.externals
- numpy
- preprocessing from sklearn

Models input files:
- /Model/sentiment_model3.0.sav
- /Model/tfidf_vectorizer3.0.sav

Tweets input files:
- /Raw_data/full_LA_Oct-Dec2017.csv
- /Raw_data/pointOfInterests.csv

If you have all the required packages installed, you just need the 4 input files mentioned right above. Then you just need to execute the "GetTopTouristSpots.ipynb" file to generate your top tourist spot list. The final result will be saved to "FinalReport.csv" after the succesfull execution of the script.

Note: Please note the input tweets file is large and the program takes some time to execute the whole thing.
