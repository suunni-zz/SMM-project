# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:53:42 2018
The program used CRF model to train the ritter dataset and to get predictions for
our tweets data.

"""
import nltk
import sklearn_crfsuite

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from sklearn.externals import joblib

def trainLocationModel(testingDataFileName,trainingDataFileName):

    #sending training data in list form
    train_sents = list(nltk.corpus.conll2002.iob_sents(trainingDataFileName))

    #function to calculate features of tokens
    def word2features(sent, i):
        word = sent[i][0]
        postag = sent[i][1]
        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'postag': postag,
            'postag[:2]': postag[:2],
        }
        if i > 0:
            word1 = sent[i - 1][0]
            postag1 = sent[i - 1][1]
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word.isupper()': word1.isupper(),
                '-1:postag': postag1,
                '-1:postag[:2]': postag1[:2],
            })
        else:
            features['BOS'] = True

        if i < len(sent) - 1:
            word1 = sent[i + 1][0]
            postag1 = sent[i + 1][1]
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word.isupper()': word1.isupper(),
                '+1:postag': postag1,
                '+1:postag[:2]': postag1[:2],
            })
        else:
            features['EOS'] = True

        return features


    # A function for extracting features in documents
    def sent2features(sent):
        return [word2features(sent, i) for i in range(len(sent))]


    # A function for generating the list of labels for each document
    def sent2labels(sent):
        return [label for token, postag, label in sent]


    def sent2tokens(sent):
        return [token for token, postag, label in sent]

    #splitting training data
    X_train = [sent2features(s) for s in train_sents]
    y_train = [sent2labels(s) for s in train_sents]

    # crf algorithm
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)

    # saving the crf model for reusing
    crf.tagger_.dump(filename="crf_tagger.txt")
    filename = 'finalized_model.sav'
    joblib.dump(crf, filename)

    #testing
    #crf=joblib.load('crf_tagger.txt')
    loaded_model = joblib.load(filename)
    test_sents = list(nltk.corpus.conll2002.iob_sents(testingDataFileName))
    X_test = [sent2features(s) for s in test_sents]
    y_test = [sent2labels(s) for s in test_sents]
    result = loaded_model.predict(X_test)

    joblib.dump(result,'predictedResultObject')

if __name__ == '__main__':
    trainLocationModel(sys.argv[1],sys.argv[2])
