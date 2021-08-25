#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from googletrans import Translator


# In[2]:


book1 = pd.read_csv(r'D:\job\Book1.csv')
book2 = pd.read_csv(r'D:\job\Book2.csv')


# In[3]:


transl = []
count = 0
for element in book1['Keywords']:
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
            print("<<--Hedline is in English...")
            transl.append(element)
        ### end Checking...###


# In[4]:


book1['Trans'] = transl
book1.head()


# In[5]:


pd.set_option('display.max_columns',None)


# In[6]:


book1['Topic'] = np.nan
book1.Trans[0][0]


# In[7]:


book2[book2.Keywords == 'National Population Register']['Topic']


# In[8]:


#list of keyword as argument
def topic_sort(keywords):
    keywords_list = keywords.split(',')
    for keyword in keywords_list:
        print("h" + keyword)
        topic = book2[book2.Keywords == keyword]['Topic']
        print("1" + topic)
        if not topic.empty:
            print("2" + topic)
            print(keywords)
            #book1.loc[book1['Trans'] == keywords, 'Topic'] = topic
            book1['Topic'] = np.where(book1['Trans'].isin(keywords.split(',')), topic,'Generic')
            break
        else:
            book1['Topic'] = np.where(book1['Trans'].isin(keywords.split(',')), topic,'Generic')            


# In[9]:


book1.apply(lambda row: topic_sort(row['Trans']),axis=1)


# In[10]:


book1.Topic


# In[12]:


col1 = pd.DataFrame(book1['Topic'], columns=['Topic'])

col2 = pd.DataFrame(book1['Headline'], columns=['Headline'])

col3 = pd.DataFrame(book1['Keywords'], columns=['Keywords'])

results = pd.concat([col1, col2, col3], axis=1)
results.to_excel('D:\job\ResultTopic.xlsx')


# In[ ]:




