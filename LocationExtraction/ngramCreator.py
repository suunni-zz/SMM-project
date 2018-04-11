import re
from nltk import word_tokenize, pos_tag
import pandas as pd
import csv
import sys
import nltk
from nltk.util import ngrams

reload(sys)

sys.setdefaultencoding('utf8')

df = pd.read_csv('output_got_LA_poi.csv',sep=';')
#clean_tweet = re.match('(.*?)http.*?\s?(.*?)', str)


with open('testNgramsTweetData.csv','wb') as out:
    csv_out=csv.writer(out,delimiter=' ')

    for tweetText in df['text']:

        #clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweetText)
        #clean_tweet=re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweetText, flags=re.MULTILINE)
        text = re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', ' ', tweetText.lower())
        words = re.findall(r'[a-z]+', text)
        clean_tweet= ' '.join(words)
        print clean_tweet
        #print type(clean_tweet[0])
        listOfPos=pos_tag(word_tokenize(clean_tweet.decode('utf-8').strip()))
        fourgrams = ngrams(listOfPos, 3)

        for row in list(fourgrams):
            row+=('O',)
            csv_out.writerow(row)
        csv_out.writerow(())