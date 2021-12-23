# Intermediate 4 : BeautifulSoup객체 만들기
***

웹 서버로 부터 HTML 소스코드를 가져온 다음 이 HTML소스코드를 분석하는 과정을 거쳐야한다. HTML소스코드를 해석하는것을 '파싱(Parsing)'이라고 한다. HTML문서의 정보를 추출하기 위해서는 BeautifulSoup객체가 필요한다. BeautifulSoup는 아래 명령어로 다운로드 할 수 있다.

~~~
pip3 install beautifulsoup4
~~~
웬만하면 가상환경 혹은 아나콘다 가상환경을 사용하는것을 권장한다. 위키피디아에서 'Apple'이라는 검색어에 대한 결과를 파싱할 것이다. 우선 파싱하기 전에, 위키피디아의 robots.txt를 살펴보자.(https://en.wikipedia.org/robots.txt) 이 페이지를 내리다 보면 아래와 같은 부분을 볼 수 있다.
~~~
 Friendly, low-speed bots are welcome viewing article pages, but not dynamically-generated pages please.
~~~
이라고 되어있다. 이를 해석해 보면, 호의적이며, 느린 속도의 로봇이 게시글 페이지를 접근하는것은 환영하지만, JavaScript등에 의해 생성되는 동적 페이지에 대해서는 접근을 허용하지 않는다고 되어있다. 자 이제 본격적으로, BeautifulSoup를 이용하여 파싱을 해보자. BeautifulSoup객체의 매개변수는 기본적으로 두개가 있다.

~~~
BeautifulSoup(markup,parser)

markup에는 html text 소스가 들어가게 된다
parser에는 html을 파싱하는데 사용되는 파서를 적어준다
~~~
이 parser에도 여러가지 종류가 있다. 파서의 종류는 이 [링크](https://m.cafe.daum.net/flowlife/RUrO/42?q=D_MCiUSfMukTI0&)를 참고하자. 우리는 그중 가장 무난한 html.parser를 이용해 볼 것이다.

```python3
import requests
from bs4 import BeautifulSoup

url  = "https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C"
resp = requests.get(url)
htmltext = resp.text

soup = BeautifulSoup(htmltext,'html.parser')
# soup변수가 어떤 타입의 인스턴스인지 확인
print(type(soup))
print('\n')
#각 태그에 대한 접근은 (BeautifulSoup객체).(태그)로 기본적인 접근을 할 수 있다.
print(soup.head)
print('\n')
print(soup.body)
print('\n')
print(f"""
title태그 요소 : {soup.title}
title태그 name property : {soup.title.name}
title태그 문자열 : {soup.title.text}
""")
```

