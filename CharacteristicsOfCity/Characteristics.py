"""
This program builds characteristics of city using TFIDF score
"""
import pandas as pd
import sys
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

reload(sys)

# Reading user account tweets file
df = pd.read_csv('./userAccountTweetsDatas.csv',encoding="utf-8",error_bad_lines=False,sep=';')
sys.setdefaultencoding('utf8')

# clean processed dataframe
finalDf= pd.DataFrame(columns=['tweet'])


# Preprocessing the data
for index, row in df.iterrows():

    try:
        # Replacing http/https URLs with empty string
        replaced = re.sub("(?P<url>https?://[^\t]+)", 'URL', row['text'])

        # Removing punctuation
        cleanTweet = ' '.join(re.sub("(@+)|([^0-9A-Za-z \t])", " ", replaced).split())

        cleanTweet = cleanTweet.replace('URL', "")

        #Removing digits
        cleanTweet = ''.join(i for i in cleanTweet if not i.isdigit())

        #3 letter word regex to be removed
        cleanTweet = re.sub(r"\b[a-zA-Z][a-zA-Z][a-zA-Z]\b", '', cleanTweet)

        finalDf.loc[index]=cleanTweet

    except Exception:
        pass

#define vectorizer parameters
vectorizer = TfidfVectorizer(max_features=200,
min_df=3,max_df=8,stop_words='english',
                                use_idf=True,
                                  ngram_range=(2,4))

X = vectorizer.fit_transform(finalDf['tweet'])
terms = vectorizer.get_feature_names()

impWords=[]

def generateTFIDFScores(vectorizer, tfidf_result):

    scores = zip(vectorizer.get_feature_names(),
                 np.asarray(tfidf_result.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for item in sorted_scores:
        impWords.append(item[0])
        #print ("{0:20} Score: {1}".format(item[0], item[1]))

generateTFIDFScores(vectorizer, X)

with open("characteristics.csv",'wb') as resultFile:
    wr = csv.writer(resultFile)
    for row in impWords:

        wr.writerow([row])