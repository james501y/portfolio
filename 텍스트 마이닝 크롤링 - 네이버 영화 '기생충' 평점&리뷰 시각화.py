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
    

### 불용어 사전 만들기 위한 전체 단어 파악
text = str(dic.values())

### text 정제 - 명사, 형용사만 뽑기
from konlpy.tag import Okt
okt = Okt() 
pos = okt.pos(text, norm=True)

len(pos) # 전체 단어 갯수

noun_adj = []
cn = 1
for i in pos:
    if i[1] in ('Noun','Adjective'):
        # if i[1] == 'Noun' or 'Adjective':
         # 이렇게하면 안됨!!!!! 괄호로 각각 묶든가!!
        noun_adj.append(i[0])
    print("{}/{} 완료".format(cn, len(pos)))
    cn+=1

len(noun_adj) # 명사 형용사 갯수

# 빈도수 높은거 파악
import nltk
nl = nltk.Text(noun_adj)
nl.vocab().most_common(100)

stopwords = ['영화', '그', '것', '관람객', '이', '나', '보고', '말', 
             '수', '내', '세', '상', '입니다', '왜', '말', '없는', '그냥',
             '있는','때', '장면', '감독', '봉준호', '보고', '정말','작품',
             '스토리', '최고', '하나', '연출', '연기', '진짜','그냥',
             '같은','다시','이런', '표현', '가장', '모두', '입니다',
             '모든', '같다', '내', '기생충', '사람', '생각', '사회',
             '현실', '아카데미', '가족', '냄새', '재미']
# wordcloud


### 별 1점 형태소 분석
text = str(dic['1'])

# text 정제 - 명사, 형용사만 뽑기
from konlpy.tag import Okt
okt = Okt() 
pos = okt.pos(text, norm=True)

len(pos) 

## 명사 형용사만 뽑기
noun_adj = []
cn = 1
for i in pos:
    if i[1] in ('Noun','Adjective'):
        # if i[1] == 'Noun' or 'Adjective':
         # 이렇게하면 안됨!!!!! 괄호로 각각 묶든가!!
        noun_adj.append(i[0])
    print("{}/{} 완료".format(cn, len(pos)))
    cn+=1

text = " ".join(nl) # 다시 텍스트로

#word cloud
import matplotlib.pylab as plt
from wordcloud import WordCloud
wordcloud = WordCloud(font_path ="c://windows//Fonts/malgunbd.ttf",
                      stopwords = stopwords, # freq에서는 작동안함.
                      background_color = "white",
                      width = 1000,
                      height = 800).generate(text)
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis("off")




#### 별 10개 형태소 분석
text = str(dic['10'])

# text 정제 - 명사, 형용사만 뽑기
from konlpy.tag import Okt
okt = Okt() 
pos = okt.pos(text, norm=True)

len(pos) 

# 명사 형용사만 뽑기
noun_adj = []
cn = 1
for i in pos:
    if i[1] in ('Noun','Adjective'):
        # if i[1] == 'Noun' or 'Adjective':
         # 이렇게하면 안됨!!!!! 괄호로 각각 묶든가!!
        noun_adj.append(i[0])
    print("{}/{} 완료".format(cn, len(pos)))
    cn+=1

text = " ".join(nl) # 다시 텍스트로

#word cloud
import matplotlib.pylab as plt
from wordcloud import WordCloud
wordcloud = WordCloud(font_path ="c://windows//Fonts/malgunbd.ttf",
                      stopwords = stopwords, # freq에서는 작동안함.
                      background_color = "white",
                      width = 1000,
                      height = 800).generate(text)
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis("off")
