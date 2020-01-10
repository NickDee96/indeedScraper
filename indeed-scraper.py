from bs4 import BeautifulSoup as soup
import requests as req
import pandas as pd
import csv
data=pd.read_csv("web_developer.csv")
with open("C:\\Users\\nickdee96\\Documents\\Linux upload\\glassdoor upload\\sanity1.csv","a",newline="") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=["level","text"])
    for i in range(len(data)):
        page=soup(req.get(data["url"][i]).text,'lxml')
        text=page.find_all('div',{'id':'jobDescriptionText'})[0].text
        text=text.strip().replace("\n"," ").replace("'","").replace('"','').replace(":","")
        writer.writerow({"level":"web developer",
                        "text":text})
        print(i)


