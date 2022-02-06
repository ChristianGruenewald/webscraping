# Data mining Test for Data science test:

import requests 
from bs4 import BeautifulSoup as bs
import os


url='https://the-morpheus.de/'
soup=bs(requests.get(url).content, "html.parser")
img_urls=[]

for img in soup.find_all("img"):
    img_url=(url + img.attrs.get("src"))
    img_urls.append(img_url)

for url in img_urls:
    response=requests.get(url)
    size=int(response.headers.get("Content-lenght",0))
    name=os.path.join("img", url.split("/")[-1])
    with open(name,"wb") as f_out:
        f_out.write(response.content)
