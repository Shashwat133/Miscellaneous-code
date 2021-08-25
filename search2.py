import pandas as pd
import numpy as np
from googletrans import Translator
# -*- coding: utf-8 -*-

df = pd.read_csv('C:\\Users\\ankitgupta\\Desktop\\Shashwat\\demodata1.csv')

df.head(5)


transl = []
count = 0
for element in df['Headline']:
    count += 1
    print("element-" + str(count) + ": " + str(element))
    if(element != ''):
        count += 1
        # check if String is in English or Not
        try:
            readitem = str(element)
            readitem.encode('ascii')
        except UnicodeEncodeError:
            print("-->>>>Hedline is not in English...")
            # REINITIALIZE THE API
            trans = Translator()
            translatedtext = trans.translate(str(element)).text
            transl.append(translatedtext)
            print(translatedtext)
        else:
            print("<<--Hedline is in English...")
            transl.append(element)
        ### end Checking...###

df['trans'] = transl

df.head(5)
