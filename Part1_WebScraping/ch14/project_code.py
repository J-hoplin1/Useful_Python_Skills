import os,pprint,enum,time,csv
from enum import Enum
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class findStatByKeyWord(object):
    url = 'https://ecos.bok.or.kr/jsp/vis/keystat/#/key'
    def __init__(self):
        pass

    #webdriver반환하는 메소드
    def getDriver(self):
        return webdriver.Chrome(f"{os.getcwd()}/chromedriver")

    # 콘솔창을 클리어해주는 클래스 메소드
    @staticmethod
    def clearConsole():
        os.system('clear')
    
    #검색 결과에 대해 선택을 하여, 선택된 값을 반환하는 메소드
    def returnSelectedOption(self, li):
        opt = [[f'{i.value}. {i.name}'] for i in li]
        loop = True
        while loop:
            print("=" * 20)
            for i in opt:
                print(i[0])
            print("=" * 20)
            try:
                select = input(">> ")
                # Command : /back : go back to previous page
                if select == "/back":
                    self.clearConsole()
                    return False
                else:
                    select = int(select)
                    # 올바른 범위 내에서 입력 되면, 값을 반환
                    if 1 <= select <= len(opt):
                        return li(select)
                    #올바른 범위 내에서 입력이 되지 않았다면, 다시 입력하도록 함
                    else:
                        self.clearConsole()
            # 만약 올바르지 않은 값이 입력되면 다시 입력하도록
            except ValueError as e:
                self.clearConsole()
                pass
            except KeyboardInterrupt as e:
                self.clearConsole()
                pass


    def main(self):
        #드라이버 호출
        driver = self.getDriver()
        
        findStatByKeyWord.clearConsole()
        while True:
            #검색을 완료한 후에 다시 100대 경제지표 페이지로 돌아와 검색을 해야한다. 그렇기 때문에, 해당 작업을 다시 해주는것이며, 
            # 혹시라도 작업을 하는 과정에 토픽 이름이 변경되는등의 경우를 생각해 토픽 딕셔너리도 다시 생성한다.(사실 여기까진 필요없지만 그냥 생각해 보자 라는 의미)
            driver.get(findStatByKeyWord.url)
            driver.implicitly_wait(5)
            layout = driver.find_elements(By.CLASS_NAME,'HSthemeA')
            total_topic = []
            for i in layout:
                for j in i.find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'a'):
                    total_topic.append(j.text)
            '''
            #검색된 모든 토픽들 보기
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(total_topic_text)
            print(len(total_topic_text)) # 100
            '''
            try:
                search_key_word = input("검색하고자 하는 단어 입력하기 >> ")
            #Ctrl + C를 눌러 취소하기
            except KeyboardInterrupt as e:
                driver.quit()
                break
            search_success = []
            for i in total_topic:
                if search_key_word in i:
                    search_success.append(i)
                else:
                    pass
            #If search result not found
            if not search_success:
                print("검색 실패")
            #else
            else:
                enums = Enum('opt',search_success)
                print(f"< 총 {len(search_success)}개의 관련 자료 검색 완료 >")
                select = self.returnSelectedOption(enums)
                if not select:
                    driver.quit()
                    break
                else:
                    select = select.name
                driver.find_element(By.LINK_TEXT,select).click()
                driver.implicitly_wait(5)
                #driver ui에서 그래프, 테이블 로딩을 위해 10초대긴
                time.sleep(6)
                html_value = driver.page_source
                soup = BeautifulSoup(html_value,'html.parser')
                print("Getting title...")
                title = soup.find('h3',{'class' : 'ng-binding'}).text
                print("Getting variables...")
                headers = [k.text for k in soup.find('div',attrs={'class' : 'HSobj2 HSoh HSh753'}).find('table').find('thead').find('tr').find_all('th')]
                print("Getting Datas...")
                get_table_layout = soup.find('div',attrs={'class' : 'HSobj2 HSoh HSh753'}).find('table').find('tbody').find_all('tr')
                datas = []
                for i in get_table_layout:
                    capsule = [j.text for j in i.find_all('td')]
                    datas.append(capsule)

                # csv모듈을 import해서 csv를 저장해 봅시다.
                with open(f"{title}.csv",'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    for i in datas:
                        writer.writerow(i)
                print(f"Complete to save {title}.csv")


if __name__ == "__main__":
    k = findStatByKeyWord()
    k.main()
