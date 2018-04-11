import pandas as pd
import pickle as pkl
import os

tweets = []

for file in os.listdir("."):
	if file.endswith(".pkl"):
		tweets.extend(pkl.load(open(file, "rb")))

df = pd.DataFrame.from_dict(tweets)
df.to_csv("Data.csv", encoding='utf-8', index=False)

print(df.head())