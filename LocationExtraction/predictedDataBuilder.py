import pandas as pd
from sklearn.externals import joblib



df = pd.read_csv('testTweetData_LA.csv',sep=' ',header=None)


predictData=joblib.load('predictedResultObject')

op=[]
df1 = pd.DataFrame(columns=['pred'])
for data in predictData:

    for i in data:
        df1=df1.append({'pred':i},ignore_index=True)

#print df1

df['predOp']=df1

df.to_csv('output_LA.csv')





#df = pd.read_csv('testTweetData_LA.csv',sep=' ',header=None)

df=df[df['predOp'].str.contains("location")==True]

import numpy as np
testdf = df.groupby(0)
print testdf
df_extract = testdf.agg({0:np.size})

print df_extract

print df_extract.sort_values(by=[0], ascending=False)

