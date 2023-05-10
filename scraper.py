from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
all_data=[]
temp_list=[]
headers=['Name','Distance','Mass','Radius']

star_table=soup.find_all("table")
table_rows=star_table[7].find_all("tr")

for tr in table_rows:
    td=tr.find_all("td")
    row=[x.text.strip() for x in td]
    temp_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

star_df=pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=headers)
star_df.to_csv("scraped_data.csv")


