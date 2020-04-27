# 텍스트 마이닝 크롤링 - 네이버 영화 '기생충' 평점&리뷰 시각화

import pandas as pd
import urllib.request as req
from urllib.request import  urlopen
from selenium import webdriver
import re
import time


# dictionary 생성 -  key : 별점, values : 리뷰
dic = dict()

for j in range(1,3600):
    start = time.time()
    url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=161967&target=after&page={}".format(j)

    html = req.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('div', class_='score_result')
    for i in soup.findAll('td', {'class':'title'}):
        star = i.find('em').get_text()
        text = re.sub('기생충별점 - 총 \d+점 중\d+|신고', '', i.get_text(strip = True))
        if star in dic.keys():
            dic[star] = dic[star] + ' ' +  text
        else:
            dic[star] = text
    print("{}/3600 완료, 소요예상시간 : {} min".format(j, 
                                               round((time.time() - start)*(3600-j)/60)))
    
