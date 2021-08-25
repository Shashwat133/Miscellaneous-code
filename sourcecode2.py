#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from nltk.tokenize import WordPunctTokenizer
from flair.models import TextClassifier
from flair.data import Sentence
from googletrans import Translator


# In[ ]:


df=pd.read_excel(r'C:\Users\shardul\Downloads\Result1010.xlsx')


# In[ ]:


transl = []
count = 0
for element in df['Headline']:
    count += 1
    #print("element-" + str(count) + ": " + str(element))
    if(element != ''):
        count += 1
        # check if String is in English or Not
        try:
            readitem = str(element)
            readitem.encode('ascii')
        except UnicodeEncodeError:
            #print("-->>>>Hedline is not in English...")
            # REINITIALIZE THE API
            trans = Translator()
            translatedtext = trans.translate(str(element)).text
            transl.append(translatedtext)
            #print(translatedtext)
        else:
            #print("<<--Hedline is in English...")
            transl.append(element)
        ### end Checking...###


# In[ ]:


df['Nheadline']=transl


# In[ ]:


df1['New_sentiment'] = ' '
count = 0
for i,tweets in enumerate(df1['tidy_tweet']) :
  count += 1
  print(str(count))
  classifier = TextClassifier.load('sentiment')
  sentence = Sentence(tweets)
  classifier.predict(sentence)
  label = sentence.labels[0]
  df1['New_sentiment'][i] = label.value
  if label.score < 0.85:
    df1['New_sentiment'][i]= 'Neutral'


# In[ ]:


df['new_sentiment']=np.nan


# In[ ]:


df.new_sentiment=df.New_sentiment


# In[ ]:


df['new_sentiment']=df['new_sentiment'].replace('NEGATIVE',np.nan)


# In[ ]:


df.new_sentiment.fillna(df.Sentiment, inplace=True)


# In[ ]:


df.drop(['Nheadline',  'New_sentiment'], axis=1)


# In[ ]:


df.to_excel(r'C:\Users\shardul\Downloads\new1.xlsx') 

