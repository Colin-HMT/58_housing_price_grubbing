import re

import requests
import os
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import time

while True:
    cityname=input("cityname")
    citycode=input("citycode")
    fangjiaym=[]
    fangjiaval=[]
    for i in range(2008,2023):
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
        url = f'https://www.58.com/fangjiawang/shi-{i}-101/sq-{citycode}/'
        response = requests.get(url=url, headers=headers)
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
    df = pd.DataFrame(data=data, index=[0])
    df = (df.T)
    print (df)
    df.to_excel(f'{cityname}.xlsx')
    if cityname =="over":
        print("手动结束")
        break