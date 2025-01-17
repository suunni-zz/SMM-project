# SMM-project
Social Media Mining:

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

Steps to follow:
Location Entity Extraction:
1. Edit setup.py file. Change the location name of nltk folder as per your nltk installation.
nltkFolderName="C:/Users/Bhagyashree/AppData/Roaming/nltk_data/corpora/conll2002/"
2. Run "python setup.py" file from LocationEntityExtraction folder.
3. "/LocationEntityExtraction/processedDataset/pointOfInterests.csv" - points of interests file will be created.
4. Copy /LocationEntityExtraction/processedDataset/pointOfInterests.csv to /TwitterDataTourism-sentimentnalysiswith1.6M/Raw_data/pointOfIntersts.csv

Get top tourist spots:
1. Go to this folder "TwitterDataTourism-sentimentnalysiswith1.6M"
2. Open this "GetTopTourstSpots.ipynb" notebook
-  GetTopTourstSpots.ipynb : This file describes the process of executing the GetTopTouristSpots.ipynb
3. Run all code inside it.
4. The final result will be saved to "/TwitterDataTourism-sentimentnalysiswith1.6M/Processed_data/FinalReport.csv" after the succesfull execution of the script.

To get characteristics of city:
1. Go to "/CharacteristicsOfCity/"
2. Run "python Characteristics.py" 
3. Output is created in same folder "characteristics.csv"

To get popular hashtags:
1. Go to folder "/Hashtag-extraction/"
2. Run python notebook "ProminentHashtags.ipynb"
3. Output is in "/Hashtag-extraction/ProcessedDataSet/hashtag_NY.csv".
Note: Current hashtag extraction is for New York dataset.

