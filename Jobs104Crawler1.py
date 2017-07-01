
import requests
from bs4 import BeautifulSoup
from collections import Counter


def parseOnePage(jsData,pcCtr): 
    for x in jsData:
        y = x.get('PCSKILL_ALL_DESC')  
        try: 
            if (y.strip() != 'None') and (y.strip() != ''):
                yList=y.strip().split()
                for word in yList:
                    word = word.lower()
                    if word in pcCtr:
                        pcCtr[word] += 1
                    else:
                        pcCtr[word] = 1        
        except AttributeError:
            pass
    return pcCtr

pcCtr=Counter();

res = requests.get('http://www.104.com.tw/i/apis/jobsearch.cfm?cat=2007001004&page=%d&pgsz=200&fmt=8&comp&cols=PCSKILL_ALL_DESC'%(1))
js=res.json()

# for i in range(1,js['TOTALPAGE']):
for i in range(1,int(js['TOTALPAGE'])):
    print(i)
    res = requests.get('http://www.104.com.tw/i/apis/jobsearch.cfm?cat=2007001004&page=%d&pgsz=200&fmt=8&comp&cols=PCSKILL_ALL_DESC'%(i))
    js=res.json()
    pcCtr = parseOnePage(js['data'],pcCtr)

print(pcCtr)
    





