# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:33:12 2024

@author: ADMIN
"""
import bs4
from bs4 import BeautifulSoup as bs
import requests
page=requests.get("https://www.imdb.com/title/tt0068646/reviews/?ref_=tt_ql_2")
page
page.content
soup=bs(page.content,"html.parser")
print(soup.prettify)
########################################################

title=soup.find_all('a',class_="title")
title
review_title=[]
for i  in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n') for title in review_title]
review_title
len(review_title)


#########
#now let us scrap rating
rating=soup.find_all('span',class_='rating-other-user-rating')
rating
rate=[]
for i  in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('\n\n\n\n\n\n') for r in rate]
rate=[r.replace('/10', '') for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)


#Let us scrap the review body
review=soup.find_all('div',class_='text show-more__control')
review
review_body=[]
for i  in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)

#create a dataframe
import pandas as pd
df=pd.DataFrame()
df['Review_title']=review_title
df['Rate']=rate
df['Review']=review_body
df
######################
#now create csv file
df.to_csv(r"C:\Users\ADMIN\8-Text Mining\Text Mining\IMDb_reviews1.csv",index=True)
########

#Sentiment Analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv(r"C:\Users\ADMIN\8-Text Mining\Text Mining\IMDb_reviews1.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
