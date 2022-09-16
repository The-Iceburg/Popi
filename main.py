import requests as rq

from bs4 import BeautifulSoup

r = rq.get("https://www.coop.co.uk/products/sitemap.xml", allow_redirects=False)
urlist = str(r.content)

Bs_data = BeautifulSoup(r.content, "xml")
b_unique = Bs_data.find_all('loc')
for i in range(len(b_unique)):
    b_unique[i] = b_unique[i].replace("<loc>", "")
    b_unique[i] = b_unique[i].replace("</loc>", "")

print(b_unique)

#for i in urllist:
#    url = urllist[i]
#    r = rq.get(url, allow_redirects=False)
#    test2 = str(r.content)
#    test1 = test2.split('class="coop-u-red-mid">&pound;')
#    test3 = test1[1].split("<")
#    print(test3[0])
#
#    urlsplit = url.split('/')
#    urlsplit2 = urlsplit[-1].replace("-", " ")
#    print(f"The price of {urlsplit2} is £{test3[0]}")