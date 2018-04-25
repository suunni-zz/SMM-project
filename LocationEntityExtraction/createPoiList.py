"""
This program will take the predicted file data and extract names which
are labelled as location.
For eg) B-noun.location , I-noun.location

Creating bigram and trigram list of those location names - which is our point of interest/locations

"""
import sys
reload(sys)
import pandas as pd
sys.setdefaultencoding('utf8')
import six
import csv
import copy

def buildPointOfInterestLocations(predictedDataFileName,pointOfInterestFileName):

    df = pd.read_csv(predictedDataFileName,sep=',')

    locationList=[]
    bigList=[]
    invalidLabels=['la','ca','los','angeles','california']
    for index, row in df.iterrows():

        label=row['predOp']
        if isinstance(row[1], six.string_types):

            value=row[1].lower()
        else:
            value = row[1]
        if(label.find('location') > -1):
            if(value not in invalidLabels):
                locationList.append(value)
        else:

            if(len(locationList)!=0):
                li2 = copy.deepcopy(locationList)
                bigList.append(li2)
                locationList=[]

    # Bigrams
    bigramDict={}
    for input in bigList:

        bigrams=zip(input, input[1:])

        if(len(bigrams)!=0):
            for eachbigram in bigrams:
                bigramStr = " ".join(eachbigram)

                if (bigramStr in bigramDict):
                    bigramDict[bigramStr] = bigramDict.get(bigramStr) + 1
                else:
                    bigramDict[bigramStr] = 1

    # Trigrams
    trigramDict = {}
    for input in bigList:

        trigrams = zip(input, input[1:], input[2:])

        if (len(trigrams) != 0):
            for eachtrigram in trigrams:
                trigramstr = " ".join(eachtrigram)

                if (trigramstr in trigramDict):
                    trigramDict[trigramstr] = trigramDict.get(trigramstr) + 1
                else:
                    trigramDict[trigramstr] = 1

    bigramDict.update(trigramDict)
    sortedValues=sorted(bigramDict, key=bigramDict.get, reverse=True)[:30]


    with open(pointOfInterestFileName, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in sortedValues:
            writer.writerow([val])

if __name__ == '__main__':
    buildPointOfInterestLocations(sys.argv[1],sys.argv[2])




