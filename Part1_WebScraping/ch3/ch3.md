# Intermediate3 : 로봇 배제 표준(robots.txt)
***

로봇 배제 표준이란, **웹사이트에 대해, 로봇이 접근하는것을 방지하기 위한 규약**이다. 이 접근 제한에 대한것은 **root디렉토리에, robots.txt에 기술**을 한다고 한다. 크롤링 등을 통해 웹페이지에 접근하는 경우, 이 robots.txt를 반드시 확인하고 가이드라인을 따라야 한다. 로봇 배제 표준 종류에는 아래와 같다.

|예시|설명|
|:---:|:---:|
|User-agent: *<br>Allow: /|모든 로봇에 대해 루트 디렉토리 이하<br>모든 문서에 접근을 허용함 |
|User-agen: *<br>Disallow: /|모든 로봇에 대해 루트 디렉토리 이하<br>모든 문서에 대한 접근을 차단한다.|
|User-agent: *<br>Disallow: (디렉토리)|모든 로봇에 대해 특정 디렉토리에 대한<br> 접근을 차단한다.|
|User-agent: 특정봇<br>Disallow: /|특정 봇에 대해 모든 문서에 대한 <br>접근을 차단한다.|

크롤링 등 로봇으로 접근을 할 시에는 **웹서버에 무리가 가지 않도록 반복적인 요청은 하지 말것** 그리고 **취득한 자료, 데이터에 대해 임의 배포 및 변경하는 행위는 저작권에 문제가 될 수 있으므로 하지 않아야**한다.

robots.txt는 주로 루트 디렉토리에 있으므로, 쉽게 접근할 수 있다(URL/robots.txt). https://www.python.org/robots.txt

```python3
import requests

urls = ["https://www.naver.com","https://www.python.org"]
robots = "robots.txt"

for i in urls:
    resp = requests.get(f"{i}/{robots}")
    print(resp.text)
    print("\n")
```