import pandas as pd
import numpy as np
from googletrans import Translator

book1 = pd.read_excel(r'C:\Users\Asus\Desktop\Intellisense\Ministry of Home AffairsTV.xls')
book2 = pd.read_csv(r'C:\Users\Asus\Desktop\Intellisense\Book2.csv')

#list of keyword as argument
def topic_sort(headlines):
    for keyword in book2.Keywords:
        keyword = str(keyword)
        curr_topic = book2[book2.Keywords == keyword]['Topic']
        if headlines.count(keyword) > 0:
            book1['Topic'] = np.where(book1['Notes'] == headlines, curr_topic, 'Generic')
            row = book1[book1.Notes == headlines]
            break
        else:
             pass
    return row

if __name__ == "__main__":
    rows = list()
    for headline in book1.Notes:
        row = topic_sort(headline)
        rows.append(row)
    
    df = rows[0]
    for row in rows[1:]:
        df = pd.concat([df,row])
    
    book1 = book1[~book1.ClipId.isin(df.ClipId)]
    book1 = pd.concat([df,book1])
    book1 = book1.sort_index(axis = 0)
    book1.to_csv(r'C:\Users\Asus\Desktop\Intellisense\final_1.csv') # final file save path