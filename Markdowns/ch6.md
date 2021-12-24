# Intermediate 6 : 웹상의 이미지를 로컬에 저장하기
***
**권장 : 앞으로 내용에서는 HTML /CSS에 대한 기초 지식이 권장됩니다.(기본적인 태그, html 구조, css selector) 부족하시다고 생각되는분들은 https://opentutorials.org/course/3084 를 수강하고 오시는걸 권장합니다.**
***

앞에서 보았던 BeautifulSoup객체의 find()메소드를 이용해서 이미지를 저장해 보도록 하겠습니다.우선 이미지는 서버 어딘가에 저장되어, 이 저장된 이미지를 가지고 html에서도 페이지를 구성하는 방식입니다.
저희는 이 이미지의 링크를 가져와서 다운로드를 할 것입니다. 자 우선 자신이 다운로드 하고자 하는 이미지에 요소 선택기(크롬 개발자 도구의 마우스 커서 모양 아이콘)을 선택한 후 마우스를 가져가 봅시다.
<center><img src="https://user-images.githubusercontent.com/45956041/147314281-465c972d-357e-4c40-b938-18e2ee99db18.png" width="1000" height="500"></center>
이미지의 태그를 보니 되게 여러가지 속성이 있는것을 알 수 있습니다. 

<center><img src="https://user-images.githubusercontent.com/45956041/147314434-907447da-7229-4c61-9da3-d472ac6b3663.png" width="1000" height="500"></center>

제가 선택한 이미지의 레이아웃 html을 자세히 보면 아래와 같습니다.저는 이 태그를 지정하기 위해서 'alt'라는 속성을 이용하여 지정할 것입니다. 그리고, <img>태그에서 이미지를 불러올 주소/디렉토리를 지정하는 속성요소는 'src'입니다.그렇기 때문에 불러온 <img>태그에서 'src'속성의 값을 불러와야합니다.
그렇다면 지난 장에서 해보았던 find()메소드를 이용해서 다운로드 하고자 하는 이미지의 <img>태그를 지정하고, src의 값을 가져와 보겠습니다.

우선 아래와 같이 <img>태그에 대한 지정까지 해봅시다. find() 메소드의 attrs값을 전달할때는 딕셔너리 형태로 {'(속성 이름)' : '(속성 값)'}을 입력해 주세요. 저와 다른 링크에서 실습을 하신다면, 자신이 사용할 링크의 html요소에 맞춰서 코드를 변경해주세요.

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

img_tag = html.find('img',attrs={'alt' : 'Apple park cupertino 2019.jpg'})
print(img_tag)

'''
Response Code : 200
<img alt="Apple park cupertino 2019.jpg" data-file-height="3070" data-file-width="5464" decoding="async" height="124" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/220px-Apple_park_cupertino_2019.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/330px-Apple_park_cupertino_2019.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/440px-Apple_park_cupertino_2019.jpg 2x" width="220"/>
'''
print(type(img_tag.attrs)) # <class 'dict'>

print(img_tag.attrs)
'''
{'alt': 'Apple park cupertino 2019.jpg', 'src': '//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/220px-Apple_park_cupertino_2019.jpg', 'decoding': 'async', 'width': '220', 'height': '124', 'srcset': '//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/330px-Apple_park_cupertino_2019.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Apple_park_cupertino_2019.jpg/440px-Apple_park_cupertino_2019.jpg 2x', 'data-file-width': '5464', 'data-file-height': '3070'}
'''
```
이 코드를 실행하면 저희가 지정하고 싶었던 <img>태그의 값이 나오는것을 볼 수 있습니다. 그리고 가져온 태그 정보(변수 img_tag)에 대해서 .attrs결과 값을 출력해 보면 해당 태그의 속성값들이 딕셔너리 형태로
나오는것을 볼 수 있으며, 실제 이 값의 type은 딕셔너리인것을 알 수 있습니다. 그러면 이제 'src'값을 key값으로 .attrs의 결과값에서 value를 가져오게 되면 됩니다.
```python3
print(img_tag.attrs['src'])
```
위 코드를 추가로 작성해 실행하면 'src'값이 나오는것을 볼 수 있습니다. 이제 앞에 https:를 붙여서 이미지를 다운로드 해보겠습니다.
```python3
import requests,sys
from bs4 import BeautifulSoup

def checkResp(resp) -> None:
    # If status code is in range of 200 : response is normal
    if resp.status_code >= 200 and resp.status_code <300:
        print(f"Response Code : {resp.status_code}")
        return True
    # If status code is not in range 200 : Abnormal connection
    else:
        print(f"Connection Status is {resp.status_code}. Abnormal Response.")
        return False
    
url = "https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C"
# Get response from url
resp = requests.get(url)

# Variable for Beautiful Soup Instance
html = None
#Check Response Status
resp_check = checkResp(resp)

if not resp_check:
    sys.exit()
else:
    #Get HTML text from response
    resp_text = resp.text
    #Make html text to BeautifulSoup 
    html = BeautifulSoup(resp_text,'html.parser')

#Get <img> tag
img_tag = html.find('img',attrs={'alt' : 'Apple park cupertino 2019.jpg'})
# Get <img> tag src value
get_img_src = img_tag.attrs['src']
#Image URL
img_url = f"https:{get_img_src}"
#Request to Image URL
img_req = requests.get(img_url)
#Check response
check_img_req = checkResp(img_req)
#Image response content
img_resp_content = None

if not check_img_req:
    sys.exit()
else:
    # If normal response save contents
    #Contents saved as 'byte'
    img_resp_content = img_req.content
# Download Image : wb 는 write byte를 의미합니다. content는 우선적으로 byte로 불러오기 때문에 write byte를 통해 사진을 저장합니다.
with open('download_img.jpg','wb') as f:
    f.write(img_resp_content)
    print("Image saved completed")
```
위 코드를 입력하면 이미지가 저장되는것을 볼 수 있습니다. 이 src값을 저희는 .attrs속성 값에서 불러오는 형식으로 했지만, get()메소드를 이용해도 src 값을 불러올 수 있습니다. get()메소드의 기본적인 매개변수는
'속성 이름'입니다. 아래와 같이 바꿔보아도 지정한 <img> 태그의 'src'값을 잘 가져오는것을 볼 수 있습니다.
```python3
get_img_src = img_tag.get('src')
print(get_img_src)
```
