# Intermediate 7 : 모든 하이퍼링크 추출하기
***

앞에서 저희는 find()라는 메소드를 보았습니다. 이 find()라는 메소드는 매개변수로 전달해준 조건에 대해 '최초로 만나는 요소' 에 대해서 하나의 값만 반환하였죠. 이번에는 매개변수 조건으로 해당되는 '모든' 값을
한번에 반환해주는 find_all()메소드를 살펴보도록 하겠습니다. 우선 find_all()의 [documentation](https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_all#find-all)부터 살펴보겠습니다

<img src="https://user-images.githubusercontent.com/45956041/147397930-cea2bc02-6789-4c26-937d-11b64c386a70.jpeg" width="1000" height="800">

해석을 해보면, 이 메소드는 자신의 필터에 대한 모든 자손을 반환한다고 합니다. 매개변수중 저희가 유심히 살펴볼것은 name과 attrs입니다.이 두개의 값은 find()에 건내주는 값과 동일합니다

  - name : 태그 이름
  - attrs : html element속성값
  - limit : 최대 검색개수

그리고 밑에 있는 예제들을 보면 반환값은 '리스트' 자료구조 형태로 되는것을 볼 수 있군요. 그러면 저희는 우선 하나의 가정을 해보겠습니다. 만약 모든 하이퍼링크된 url을 가져온다는 가정을 말이죠. 하이퍼링크는 기본적으로
<a>태그를 통해서 만듭니다. 그리고 링크는 <a>태그의 href속성에 넣어주죠. 그렇다면 find_all()을 이용해서 모든 <a> 태그를 가져오고, 이 <a>태그 안에 있는 링크들까지 가져와 보도록 하겠습니다.저번에는 attrs속성
 을 통해서 속성값을 가져왔었죠, 이번에는 마지막에 배운 .get()메소드를 이용해서 속성값을 가져와 보도록 하겠습니다. 이 장부터 예제에 파이썬 숏코딩, 메소드 체이닝등 잡기술이 들어갈 예정입니다. 사실 추후 유지보수나
  협업을 위해서는 풀어쓰는 것이 좋긴하지만, 어느정도의 모두가 아는 보편적인 잡기술이 들어가는 정도는 괜찮다고 개인적으로 생각합니다.
  
  ```python3
import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C"
resp = requests.get(url)
html = BeautifulSoup(resp.text,'html.parser')

get_all_a_tags = html.find_all('a')

get_a_tags_links = [i.get('href') for i in get_all_a_tags]
print(*get_a_tags_links,sep='\n') #수많은 url들
print(len(get_a_tags_links)) # 1156 (실행 시점에 따라 달라질 수 있음)
  ```
  되게 많은 url들이 검색됩니다. 이번에는 html속성까지 더해서 검색을 해보도록 하겠습니다. 예를 들어 "/wiki/"라는 부분이 들어가는 url만 찾고싶으며, 최대 5개까지만 검색을 하고싶다고 가정을 합시다. 이를 
  위해서는 당연히 find_all()메소드의 attrs, limit 속성을 활용해 주어야겠죠? 그리고 추가적으로 /wiki/라는 부분이 들어가는 url만 찾기 위해서는 re라는 모듈을 사용해야합니다. re는 Regular Expression,즉 정규표현식을 검사하는 모듈입니다. 이 정규표현식에 대해서는 추후 다뤄보도록 하겠습니다. 
  find_all()뿐만 아니라 find()메소드 또한 attrs속성에 대해서 re모듈을 통해 정규표현식 검사를 넣어줄 수 있습니다.우선 지금은 re.compile(정규표현식) 을 하면 입력한 정규표현식에 알맞는 조건을 가진 문자열일 경우 true를 반환한다는것만
  알아두시면 됩니다. 여기서 실행될때 흐름은, a태그를 검색하고, href속성을 검색한 다음, 해당 href속성에 대해 정규표현식 조건에 유효하면 해당 href값을 저장하고, 아닌 경우 무시한다고 생각하시면 됩니다.
  정규표현식에 대해 알아보고 싶으신 분들은 [여기](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=is_king&logNo=221566914429) 링크를 들어가셔서
  한번 보시는것도 좋습니다
  
  ```python3
  import requests,re
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C"
resp = requests.get(url)
html = BeautifulSoup(resp.text,'html.parser')

get_all_a_tags = html.find_all('a',attrs={'href' : re.compile("/wiki/")},limit=5)

get_a_tags_links = [i.get('href') for i in get_all_a_tags]
print(*get_a_tags_links,sep='\n') #5개의 url
print(len(get_a_tags_links)) # 5
  ```

위 코드를 실행해 보면 5개의 '/wiki/'가 들어간 url이 출력되는것을 볼 수 있습니다.
 
