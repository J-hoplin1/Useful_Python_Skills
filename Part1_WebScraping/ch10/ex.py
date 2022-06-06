import requests,json
from bs4 import BeautifulSoup
from requests.api import head
from urllib.parse import quote_plus


topic = input("검색할 주제 입력하기 >> ")

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = f"https://news.google.com/search?q={quote_plus(topic)}=ko&gl=KR&ceid=KR%3Ako"
resp = requests.get(url,headers=headers)
html = BeautifulSoup(resp.text,'html.parser')
find_news_one_layout = html.find('main', attrs={'class' : 'HKt8rc'}).find('div',attrs={'class' : "lBwEZb BL5WZb xP6mwf"}).find_all('div')

news = dict()

replace_str = 'https://news.google.com'
j = 1
for i in find_news_one_layout:
    try:
        news_hyperlink = i.find('a').get('href') # ./article/ 형식으로 나오므로 형태 변환을 해주어야한다.
        news_title = i.find('div',attrs={'class' : 'xrnccd'}).find('article').find('h3',attrs={'class' : 'ipQwMb ekueJc RD0gLb'})
        news_title = news_title.text
        news[f"News {j}"] = {
            "title" : news_title,
            "link" : f"{replace_str}{news_hyperlink[1:]}"
        }
        j+=1
    except AttributeError as e:
        pass

with open(f'GoogleNewsScrape_{topic}.json','w') as f:
    json.dump(news,f,indent=4,ensure_ascii=False)
