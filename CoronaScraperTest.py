import bs4
import requests
import re
res = requests.get('https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html#a1')
type(res)
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
bob = noStarchSoup.select('#dataTable > tbody > tr:nth-child(2) > td:nth-child(2)')
print(type(bob))
print(len(bob))
print(bob)
thing =  str(bob)
x  = re.findall("\d", thing)
print(x)
l = len(x)
i = 0
number = ""
while(i < l):
    number += x[i]
    i += 1
print(number)
