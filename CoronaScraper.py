import bs4
import requests
import re
import threading, time
import matplotlib.pyplot as plt
res = requests.get('https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html#a1')
type(res)

res.raise_for_status()
ConfimedCasesHTML = []
ConfimedCasesSepperated = []
ConfimedCases = []
Deaths = []
ProbableCases = []
Area = []
c = ["r","m","y","b", "g"]
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
def scrape(colum, regex, variable):
    for x in range(1,15):
        number = ""
        a = str(x)
        bob = noStarchSoup.select('#dataTable > tbody > tr:nth-child('+a+') > td:nth-child('+colum+')')
        ConfimedCasesHTML.append(bob)
        bob = str(bob)
        print(bob)
        lol = re.sub(regex,"", bob)
        ConfimedCasesSepperated.append(lol)
        line = int(colum)
        if(line != 1):
            print(line)
            lol = int(lol)
        else:
            lol=lol[1:len(lol)-1]
        variable.append(lol)

threadObj = threading.Thread(target=scrape("1", "<.*?>", Area))
threadObj.start()
threadObj2 = threading.Thread(target=scrape("2", "\D", ConfimedCases))
threadObj2.start()
threadObj3 = threading.Thread(target=scrape("3", "\D", Deaths))
threadObj3.start()
plt.legend(Area)
plt.pie(ConfimedCases[1:15], labels=Area[1:15],colors = c)
plt.show()
