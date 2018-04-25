"""
This setup file will extract locations from the tweets data.
The final locations extracted will be stored in /processedDataset/pointOfInterests.csv
"""
import createTestingData
import trainLocationModel
import predictedDataBuilder
import createPoiList
import shutil

inputRawDataFileName="./rawInputDataset/LA_Oct_Dec_2017_data.csv"
posTagFileName="posTagOfData.csv"
predictedDataFileName="predictedData.csv"
pointOfInterestFileName="./processedDataset/pointOfInterests.csv"
nltkFolderName="C:/Users/Bhagyashree/AppData/Roaming/nltk_data/corpora/conll2002/"

ritterTrainingFileName="./ritter-train.tsv"


#Tweet raw text data is taken as an input
#Every tweet is converted in tokens and is given a pos tag.
#For each token 'O' is appended which is the target label to be predicted.
#Target label will be for assigning location label to token

createTestingData.createTestingData(inputRawDataFileName,posTagFileName)

# copying ritter training data set to nltk folder
shutil.copy2(ritterTrainingFileName, nltkFolderName)

# copying pos tag file to nltk folder
shutil.copy2(posTagFileName, nltkFolderName)

# Model is trained on ritter dataset and applied to pos tag file created by above step.
trainLocationModel.trainLocationModel(posTagFileName,ritterTrainingFileName)

# Add the predicted labels to pos tag file
predictedDataBuilder.buildPredictedDataSet(posTagFileName,predictedDataFileName)

#Create point of interest list
createPoiList.buildPointOfInterestLocations(predictedDataFileName,pointOfInterestFileName)