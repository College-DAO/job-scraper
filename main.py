import requests
from bs4 import BeautifulSoup
import pandas as pd 


def extract(page):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"}
    url =  f"https://web3.career/intern-jobs?page={page}"
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def transform(soup):
    divs = soup.find_all('tr', class_="table_row")
    for item in divs:
        try:
            title = item.find('h2').text.strip()
            print(title)
            company = item.find('h3').text.strip()
            print(company)
            salary = item.find('p', class_="text-salary").text.strip()
        except:
            salary = ''
        job = {
            "title":title,
            "company":company,
            "salary":salary
        }
        joblist.append(job)
    return


joblist = []

for i in range(1,5):
    print(f'Getting page {i}')
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
    
print(df.head())

df.to_csv("jobs.csv")