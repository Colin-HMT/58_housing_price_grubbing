import re
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import time

json={"漕泾": 7073,"枫泾": 7071,"金山工业区": 20058,"金山卫": 21991,"金山新城": 7074,"金山周边": 7078,"廊下": 22012,"吕巷": 20060,"山阳": 20059,"石化": 21990,"亭林": 7072,"兴塔": 20061,"张堰": 20062,"朱泾": 7070,"朱行": 11614}
citynm= list(json.keys())
cityc= list(json.values())
for cityname,citycode in zip(citynm,cityc):
    fangjiaym=[]
    fangjiaval=[]
    for i in range(2008,2023):
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
        url = f'https://www.58.com/fangjiawang/shi-{i}-101/sq-{citycode}/'
        response = requests.get(url=url, headers=headers)
        print(response.text)
        bs_duixiang = BeautifulSoup(response.text,"lxml")
        fangjiabox = bs_duixiang.find_all('div',class_='p-c-w mt15')
        if len(fangjiabox) == 0:
            continue
        else:
            fangjiaym1 = re.findall('<b data-v-2a40ba50="">(.*?)</b>',str(fangjiabox),re.S)
            fangjiaval1 = re.findall('<span data-v-2a40ba50="">(.*?)</span>',str(fangjiabox),re.S)
            fangjiaym.extend(fangjiaym1)
            fangjiaval.extend(fangjiaval1)
        time.sleep(5)

    data=dict(zip(fangjiaym,fangjiaval))
    df = pd.DataFrame(data=data)
    df = (df.T)
    print (df)
    df.to_excel(f'{cityname}.xlsx')
    time.sleep(20)