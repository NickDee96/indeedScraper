import requests as req
import csv
import sys

countries={
    "ma":"Morocco",
    "za":"South Africa",
    "ng":"Nigeria",
    "eg":"Egypt"
}
with open("roles.txt","r") as rFile:
    roles=[x.strip() for x in rFile.readlines()]


fieldnames=[
        "Role",
        "jobtitle",
        "company",
        "city",
        "state",
        "country",
        "language",
        "formattedLocation",
        "source",
        "date",
        "snippet",
        "url",
        "onmousedown",
        "latitude",
        "longitude",
        "jobkey",
        "sponsored",
        "expired",
        "indeedApply",
        "formattedLocationFull",
        "formattedRelativeTime",
        "stations"]
url="http://api.indeed.com/ads/apisearch?publisher=9091824477922251&q={}&sort=&radius=&st=&jt=&start={}&limit=25&fromage=7&filter=1&latlong=1&co={}&chnl=&userip=1.2.3.4&format=json&useragent=Mozilla/%2F4.0(Firefox)&v=2"

with open("data/jobs2.csv","w",newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for role in roles:
        for code in countries.keys():
            try:
                location=req.get(url.format(role,0,code)).json()["results"][0]["country"]
            except IndexError:
                print("passed for {} in {}".format(role,countries[code]))
                pass
            length=req.get(url.format(role,0,code)).json()["totalResults"]
            if location=="US":
                print("passed for {} in {}".format(role,countries[code]))
                pass
            else:
                print("Getting for {} in {}".format(role,countries[code]))
                for i in range(0,length,25):
                    mUrl=url.format(role,i,code)
                    data=req.get(mUrl).json()
                    for j in data["results"]:
                        j.update({
                            "Role":role
                        })
                        writer.writerow(j)
                    print(i) 

