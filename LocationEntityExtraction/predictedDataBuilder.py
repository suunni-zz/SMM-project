"""
This program will append actual predicted label to pos tag file.

"""
import pandas as pd
from sklearn.externals import joblib
import sys

def buildPredictedDataSet(posTagFileName,predictedDataFileName):

    df = pd.read_csv(posTagFileName,sep=' ',header=None)
    predictData=joblib.load('predictedResultObject')

    df1 = pd.DataFrame(columns=['pred'])
    for data in predictData:

        for i in data:
            df1=df1.append({'pred':i},ignore_index=True)


    df['predOp']=df1

    df.to_csv(predictedDataFileName)

if __name__ == '__main__':
    buildPredictedDataSet(sys.argv[1],sys.argv[2])





