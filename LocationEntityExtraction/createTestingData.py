"""
This program will take raw input tweet data.
Each tweet is converted to tokens.
Each token is labelled with part of speech
Each token is also appended with target label (with temporary holder 'O') which needs to be predicted.
The target label is : predicting whether its location entity or some other entity
"""

from nltk import word_tokenize, pos_tag
import pandas as pd
import csv
import sys

import re
reload(sys)
sys.setdefaultencoding('utf8')

def createTestingData(inputFileName,outputFileName):

    df = pd.read_csv(inputFileName, sep=';', error_bad_lines=False)

    try:

        with open(outputFileName,'wb') as out:
            csv_out=csv.writer(out,delimiter=' ')

            for tweetText in df['text']:

                #Preprocessing done
                replaced = re.sub("(?P<url>https?://[^\t]+)", 'URL', tweetText)

                cleanTweet = ' '.join(re.sub("(@+)|([^0-9A-Za-z \t])", " ", replaced).split())
                cleanTweet=cleanTweet.replace('URL',"")
                listOfPos = pos_tag(word_tokenize(cleanTweet.decode('utf-8').strip()))

                for row in listOfPos:
                    row += ('O',)

                    csv_out.writerow(row)
                csv_out.writerow(())

    except Exception as x:
        pass

if __name__ == '__main__':
    createTestingData(sys.argv[1],sys.argv[2])
