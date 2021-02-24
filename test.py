from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from pyvirtualdisplay import Display


try:
    username = sys.argv[1]
    password = sys.argv[2]

    display = Display(visible=0, size=(800, 800))  
    display.start()
    browser = webdriver.Chrome()
    # browser.get('https://cas.dgut.edu.cn/home/Oauth/getToken/appid/illnessProtectionHome/state/home.html')
    browser.get('https://yqfk.dgut.edu.cn')
    User = browser.find_element_by_id('username')
    User.send_keys(username)
    Pwd = browser.find_element_by_id('casPassword')
    Pwd.send_keys(password)
    button = browser.find_element_by_id('loginBtn')
    button.click()
    # browser.implicitly_wait(20)
    wait = WebDriverWait(browser, 60)
    result =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'remind___fRE9P')))
    # print(browser.page_source)
    if result[0].text == "":
        time.sleep(1)
        result =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'remind___fRE9P')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.am-button-primary')))
    for i in result:
        print(i.text)
    a = [i.text for i in result]
    # print(a)
    if "您今日尚未打卡" in a:
        button.click()
        print("已提交")
    else:
        print("已打卡")
    

except Exception as e:
    print(e)
    
finally:
    browser.close()