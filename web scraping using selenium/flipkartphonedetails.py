import requests
from bs4 import BeautifulSoup
import pandas as pd
for r in range(1,11):
    url="https://www.flipkart.com/search?q=phone+under+50%2C000+thousand&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(r)
    a=requests.get(url)
    scrap=BeautifulSoup(a.text ,"lxml")
    title=[]
    price1=[]
    description=[]
    rating=[]

    title1=scrap.find("div",class_="_1YokD2 _3Mn1Gg")
    phone_name=title1.find_all("div",class_="_4rR01T")
    for r in phone_name:
        a=r.text
        title.append(a)

    price=title1.find_all("div",class_="_30jeq3 _1_WHN1")
    for r in price:
        a=r.text
        price1.append(a)


    phone_rating=title1.find_all("div",class_="_3LWZlK")
    for r in phone_rating:
        a=r.text
        rating.append(a)

    phone_description=title1.find_all("ul",class_="_1xgFaf")
    for r in phone_description:
        a=r.text
        description.append(a)

s=pd.DataFrame({"phone_name":title,"phone_price":price1 ,"phone_rating":rating,"phone_description":description})
s.to_csv("flipkart_phonedetails.csv")

