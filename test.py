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

    # 登录
    display = Display(visible=0, size=(800, 800))  
    display.start()
    browser = webdriver.Chrome()
    browser.get('https://yqfk.dgut.edu.cn')
    # browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 100)
    # User = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    # Pwd = wait.until(EC.presence_of_element_located((By.ID, 'casPassword')))
    # button = wait.until(EC.element_to_be_clickable((By.ID, 'loginBtn')))
    User = browser.find_element_by_id('username')
    Pwd = browser.find_element_by_id('casPassword')
    button = browser.find_element_by_id('loginBtn')
    
    User.send_keys(username)
    Pwd.send_keys(password)
    if not button:
        raise Exception("找不到登录按钮")
    button.click()

    # result = browser.find_elements_by_class_name('remind___fRE9P')
    result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.remind___fRE9P')))
    # if not result[0].text:
    #     time.sleep(1)
        # result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.remind___fRE9P')))
        # result = browser.find_elements_by_class_name('remind___fRE9P')
    if not result[0].text:
        raise Exception("可能是网络很差，或者服务端有问题")
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.am-button-primary')))
    # button = browser.find_elements_by_class_name('am-button-primary')
    for i in result:
        print(i.text)
    # print(result[0].text)
    # if "您今日尚未打卡" in [i.text for i in result]:
    #     if button:
    #         button.click()
    #         print("已提交")
    #     else:
    #         print("提交失败，没有找到提交按钮")
        # browser.get('https://yqfk.dgut.edu.cn')
        # result =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'remind___fRE9P')))
        # print(result[0].text)

except Exception as e:
    print(e)


finally:
    if browser:
        browser.close()