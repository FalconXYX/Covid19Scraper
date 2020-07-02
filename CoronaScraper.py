import bs4
import requests
import re
res = requests.get('https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html#a1')
type(res)
res.raise_for_status()
ConfimedCasesHTML = []
ConfimedCasesSepperated = []
ConfimedCases = []
Deaths = []
ProbableCases = []

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
def scrape(colum, regex, variable):
    for x in range(1,15):
        number = ""
        a = str(x)
        bob = noStarchSoup.select('#dataTable > tbody > tr:nth-child('+a+') > td:nth-child('+colum+')')
        ConfimedCasesHTML.append(bob)
        bob = str(bob)
        lol = re.findall(regex, bob)
        ConfimedCasesSepperated.append(lol)
        k = len(lol)
        for j in range(0,k):
            number += lol[j]
        variable.append(number)
scrape("2", "\d", ConfimedCases)
scrape("3", "\d", Deaths)
scrape("4", "\d", ProbableCases)

print(ConfimedCases)
print(Deaths)
print(ProbableCases)
