# Intermediate 5 : Chrome Developer Tool
***

**권장 : 앞으로 내용에서는 HTML /CSS에 대한 기초 지식이 권장됩니다.(기본적인 태그, html 구조, css selector) 부족하시다고 생각되는분들은 https://opentutorials.org/course/3084 를 수강하고 오시는걸 권장합니다.**
***

크롬에서 개발자 도구를 열어보자. 개발자 도구를 보면 Elements, source, console등등 여러 창이 있는것들을 볼 수 있다. 이 개발자 도구에서 우리는 Elements창을 사용할 것이다. 이 창에서는 요소선택기(마우스 커서 모양)의 아이콘을 클릭하여, 각 레이아웃들에 대해 마우스를 가져가면 해당 레이아웃에 대한 HTML소스를 볼 수 이있다. 예를 들어서 내가 이미지가 있는 레이아웃에 대해 HTML소스를 보고싶다면 다음과 같이 할 수 있다.

<center><img src="https://user-images.githubusercontent.com/45956041/147309900-6827a3ef-66f9-443c-a617-f04f2f342c2b.png" width="1000" height="800"></center>


BeautifulSoup객체에 find()메소드에 HTML태그를 전달하면, 해당 태그에 대해 가장 첫번째로 만나는 값을 반환하게 된다. 자 우선 [BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/index.html)에 기재된 find()메소드에 대해 살펴볼까요? 자신이 사용하고자 하는 모듈 / 클래스가 있다면 Document를 한번 읽어보고 사용하는 습관을 들이는것이 좋습니다.   

<center><img src="https://user-images.githubusercontent.com/45956041/147311648-970a9b36-9bdd-4ff5-9de9-b3d954c7b544.png" width="500" height="800"></center>

정리를 해보겠습니다. 우선 매개변수입니다

  - name : 태그의 이름을 입력합니다
  - attrs : 태그에 대한 CSS Selector 혹은 HTML tag attribute(속성)를 입력합니다
  - recursive : 자식태그까지에 대한 재귀 순환에 대한 여부입니다. default는 true이며, false로 변경시 name,attrs로 지정된 최상위 태그 이후 자식태그에 대한 검색을 하지 않습니다
  - string : 문자열값을 가지고 검색을 합니다. re객체를 사용해서 전달할 수 도 있습니다.

이 매개변수중 저희가 사용할 매개변수는 name, attrs입니다. 이제 본문 정리를 해보면, 뒤에서 보게 되겠지만 find_all()메소드는 입력된 태그에 대한 모든 값을 리스트로 반환하지만, find()는 입력된 태그 정보에 대해 최초로 만나는 값 하나만 반환한다는것을 알 수 있습니다. 만약 검색에 실패하면 None을 반환합니다.
find()태그는 주로 HTML문서 안에 딱 하나만 있을거로 확신이 드는 태그에 대해 검색할때만 사용됩니다. 예를 들어 <title>태그가 있겠군요. 우선 이번 장에서는 그럼 find()메소드를 이용해서 <title>태그와 <title>태그의 content까지 출력해 보겠습니다. 코드는 아래와 같습니다. 각 코드가 왜 이렇게 유도가 되었는지 생각해보면서 작성해주세요.
  
```python3
import requests,sys
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C"
# Get response from url
resp = requests.get(url)
#Get HTML text from response
resp_text = resp.text
# Variable for Beautiful Soup Instance
html = None

# If status code is in range of 200 : response is normal
if resp.status_code >= 200 and resp.status_code <300:
    print(f"Response Code : {resp.status_code}")
    html = BeautifulSoup(resp_text,'html.parser')
# If status code is not in range 200 : Abnormal connection
else:
    print(f"Connection Status is {resp.status_code}. Abnormal Response.")
    sys.exit()

title_tag = html.find('title')
print(title_tag)
print("\n")
print(title_tag.text)
''''
Response Code : 200
<title>애플 - 위키백과, 우리 모두의 백과사전</title>


애플 - 위키백과, 우리 모두의 백과사전
'''  
```
