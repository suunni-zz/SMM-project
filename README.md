# SMM-project
Social Media Mining


-  GetTopTourstSpots.ipynbThis file describes the process of executing the GetTopTouristSpots.ipynb
Requirements for executing:- 
Python 3.0- 
Executable in Jupyter notebook

Python Packages: 
- pandas
- urllib.request
- json
- pprint
- everygrams from NLTK- word_tokenzie from NLTK- stopwords from NLTK.corpus- defaultdict from collections- joblib from sklearn.externals- numpy- preprocessing from sklearn
Models already created and saved, used as input:- sentiment_model3.0.sav- tfidf_vectorizer3.0.sav
Tweets input file:full_data.csv
If you have all the required packages installed, you just need the input file,"full_data.csv", "sentiment_model3.0.sav", 
"tfidf_vectorizer3.0.sav" in the local directory. Then you just need to execute the "GetTopTouristSpots.ipynb" file to generateyour top torist spot list. The final result will be saved to "FinalReport.csv" after the succesfull execution of the script.
Note: Please note the input tweets file is large and the program takes some time to execute the whole thing.
