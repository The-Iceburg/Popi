import requests as rq

from bs4 import BeautifulSoup

r = rq.get("https://www.coop.co.uk/products/sitemap.xml", allow_redirects=False)
urlist = str(r.content)

Bs_data = BeautifulSoup(r.content, "xml")
b_unique = Bs_data.find_all('loc')
for i in range(len(b_unique)):
    b_unique[i] = str(b_unique[i]).replace("<loc>", "")
    b_unique[i] = str(b_unique[i]).replace("</loc>", "")



for i in range(0, len(b_unique)):
    url = b_unique[i]
    
    r = rq.get(url, allow_redirects=False)
    test2 = str(r.content)

    test1 = test2.split('&pound;')
    if len(test1) != 2:
        continue
    else:
        price = test1[1].partition("\\")

        urlsplit = url.split('/')
        urlsplit2 = urlsplit[-1].replace("-", " ")
        # print(f"The price of {urlsplit2} is £{price[0]}")
        with open("result.txt","a") as f:
            f.write(f"The price of {urlsplit2} is £{price[0]}\n")
    
