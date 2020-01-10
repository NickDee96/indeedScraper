from bs4 import BeautifulSoup as soup
import requests as req
import pandas as pd
import csv

from multiprocessing import Pool

data=pd.read_csv("data/jobs2.csv")
def scraper(start):
    stop=start+400
    with open("data/jd.csv","a",newline="") as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=["Role","jobkey","jd"])
        writer.writeheader()
        for i in range(start,stop):
            try:
                page=soup(req.get(data["url"][i]).content,"lxml")
                text=page.find_all("div",{"id":"jobDescriptionText"})[0].text
                writer.writerow({"Role":data.Role[i],
                                "jobkey":data.jobkey[i],
                                "jd":text})
                print(i)
            except KeyError:
                break


if __name__ == "__main__":    
    p = Pool(10)
    p.map(scraper, range(0,len(data),200))

