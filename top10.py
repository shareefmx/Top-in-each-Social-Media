#top 10 account in each social media

import pandas as pd
import requests
from bs4 import BeautifulSoup

wikiurl="https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)

soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
df=pd.DataFrame(df[0])

wikiurl1="https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts#:~:text=Most-followed%20accounts%20%20%20%20Rank%20%20,%20%2073.9%20%2022%20more%20rows%20"
table_class1="wikitable sortable jquery-tablesorter"
response1=requests.get(wikiurl1)

soup1 = BeautifulSoup(response1.text, 'html.parser')
indiatable1=soup1.find('table',{'class':"wikitable"})

df1=pd.read_html(str(indiatable1))
df1=pd.DataFrame(df1[0])

wikiurl2="https://en.wikipedia.org/wiki/List_of_most-followed_Facebook_pages#:~:text=Most-followed%20Facebook%20pages%20%20%20%20Rank%20,%20United%20Kingdom%20%2036%20more%20rows%20"
table_class2="wikitable sortable jquery-tablesorter"
response2=requests.get(wikiurl2)

soup2 = BeautifulSoup(response2.text, 'html.parser')
indiatable2=soup2.find('table',{'class':"wikitable"})

df2=pd.read_html(str(indiatable2))
df2=pd.DataFrame(df2[0])

wikiurl3="https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts#:~:text=Most%20followed%20accounts%20on%20Twitter%20%20%20,%20%20113.6%20%2022%20more%20rows%20"
table_class3="wikitable sortable jquery-tablesorter"
response3=requests.get(wikiurl3)

soup3 = BeautifulSoup(response3.text, 'html.parser')
indiatable3=soup3.find('table',{'class':"wikitable"})

df3=pd.read_html(str(indiatable3))
df3=pd.DataFrame(df3[0])

wikiurl4="https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts"
table_class4="wikitable sortable jquery-tablesorter"
response4=requests.get(wikiurl4)

soup4 = BeautifulSoup(response4.text, 'html.parser')
indiatable4=soup4.find('table',{'class':"wikitable"})

df4=pd.read_html(str(indiatable4))
df4=pd.DataFrame(df4[0])

wikiurl5="https://en.wikipedia.org/wiki/List_of_most-followed_Twitch_channels"
table_class5="wikitable sortable jquery-tablesorter"
response5=requests.get(wikiurl5)

soup5 = BeautifulSoup(response5.text, 'html.parser')
indiatable5=soup5.find('table',{'class':"wikitable"})

df5=pd.read_html(str(indiatable5))
df5=pd.DataFrame(df5[0])


data = df[['Rank','Name']]
data1 = df1[['Owner']]
data2 = df2[['Page name']]
#data3 = df3[['Account name']]
dattt=df4.rename(columns={"Owner":"sp"})
data4 = dattt[['sp']]

data5 = df5[['Channel']]
da=pd.concat([data,data1,data2,data4,data5],axis=1)

dst=da.rename(columns={"Name":"YouTube channels","Owner":"Instagram accounts","Page name":"Facebook pages","Channel":"Twitch channels","sp":"TikTok accounts"})

print(dst.head(10))
