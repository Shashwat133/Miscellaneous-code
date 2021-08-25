#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
from textblob import TextBlob
import os, glob


# In[2]:


#Import the dat
path = "D:/job/"#downloaded files folder path

all_files = glob.glob(os.path.join(path, "*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
#merge the files    
merged_df = pd.concat(all_df, ignore_index=True, sort=True)


# In[3]:


merged_df


# In[4]:


#export the merged files
pd.DataFrame(merged_df).to_csv("D:\job\demo10.csv")#export path name


# In[7]:


#sentiment analysis
merged_df['sentiment'] = ' '
merged_df['polarity'] = None
for i,tweets in enumerate(merged_df['headline']) :
    blob = TextBlob(tweets)
    merged_df['polarity'][i] = blob.sentiment.polarity
    if blob.sentiment.polarity > 0 :
        merged_df['sentiment'][i] = 'positive'
    elif blob.sentiment.polarity < 0 :
        merged_df['sentiment'][i] = 'negative'
    else :
        merged_df['sentiment'][i] = 'neutral'
merged_df.head()


# In[8]:


#export the sentiment file in excel
col1 = pd.DataFrame(merged_df['sentiment'], columns=['sentiment'])

col2 = pd.DataFrame(merged_df['headline'], columns=['headline'])

col3 = pd.DataFrame(merged_df['polarity'], columns=['polarity'])

results = pd.concat([col1, col2, col3], axis=1)
results.to_excel('D:\job\Result1001.xlsx')


# In[ ]:




