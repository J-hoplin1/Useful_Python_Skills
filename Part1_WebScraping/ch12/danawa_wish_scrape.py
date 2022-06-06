import os,json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

danawa_url = 'http://www.danawa.com/'

id = ""
pw = ""

#Get Driver
driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver")
driver.implicitly_wait(5)
#Request to danawa
driver.get(danawa_url)

driver.find_element(By.CLASS_NAME,'btn_user--login').click()
driver.implicitly_wait(3)
#Send ID
driver.find_element(By.ID,'danawa-member-login-input-id').send_keys(id)
#Send Key
driver.find_element(By.ID,'danawa-member-login-input-pwd').send_keys(pw)
#Find Login Button and log in
driver.find_element(By.ID,'danawa-member-login-loginButton').click()
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME,'btn_user--wish').click()
page_html = driver.page_source
driver.close()

json_element = dict()

soup_instance = BeautifulSoup(page_html,'html.parser')
get_element_per_items = soup_instance.find("table",attrs={'class' : 'wish_tbl'}).find('tbody').find_all('tr')

os.system('clear')

for j,i in enumerate(get_element_per_items,start=1):
    img_link = i.find('td',{'class' : 'img'}).find('a').get('href')
    item_title = i.find('td',{'class' : 'info'}).find('div',{'class' : 'tit'}).text
    item_spec = i.find('td',{'class' : 'info'}).find('dd',{'class' : 'spec_list'}).find('a').text
    item_cost = i.find('td',{'class' : 'lowest'}).find('span',{'class' : 'price'}).find('em').text + "원"
    json_element[f"Item {j}"] = {
        "Image URL" : f"{img_link}",
        "Item Title" : item_title,
        "Item Spec" : item_spec,
        "Item Cost" : item_cost
    }
    statement = f'''
    {"=" * 40}
    Item title : {item_title}
    Item Spec : {item_spec}
    Item Cost : {item_cost}
    {"=" * 40}
    '''
    print(statement)

with open("My_WishList.json",'w') as f:
    #ensure ascii : 한글은 기본적으로 16진수로 표기되어 저장된다. 한글로 저장하기 위해서는 ensure_ascii를 false로 바꿔줘야한다.
    json.dump(json_element,f,indent=4,ensure_ascii=False)


print("Json saved!")
