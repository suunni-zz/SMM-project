from nltk import word_tokenize, pos_tag
import pandas as pd
import csv
import sys
import nltk
import re

reload(sys)
#
sys.setdefaultencoding('utf8')

#df = pd.read_csv('output_got_LA_poi.csv',sep=';')
df = pd.read_csv('LA_Oct2017_old.csv',sep=';')

#print pos_tag(word_tokenize("I'm learning NLP"))

with open('testTweetData_LA.csv','wb') as out:
    csv_out=csv.writer(out,delimiter=' ')

    for tweetText in df['text']:
        try:
            text = re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', ' ', tweetText.lower())
            print "text" , text
            words = re.findall(r'[a-z]+', text)
            print "words", words
            someseries = pd.Series(words)
            someseries.drop(['https','www','http'])
            clean_tweet = ' '.join(list(someseries))

            listOfPos=pos_tag(word_tokenize(clean_tweet.decode('utf-8').strip()))
        except Exception as x:
            pass

        for row in listOfPos:
            row+=('O',)

            csv_out.writerow(row)
        csv_out.writerow(())

# nltk.download('brown')
# brown_a =nltk.corpus.brown.tagged_sents(categories='a')
# bigram_tagger=nltk.BigramTagger(brown_a,cutoff=0)
# sent = "Thieves leave young athletes in the dard".split()
#
# print bigram_tagger.tag(sent)

# from nltk.util import ngrams
# token = nltk.word_tokenize(df['text'][0])
# # bi = ngrams(token,2)
# # trigrams = ngrams(token,3)grams
# fourgrams = ngrams(token,4)
#
# #print list(fourgrams)
#
# for l in list(fourgrams):
#     print "l" , l
#     listOfPos=pos_tag(l)
#     print listOfPos
