from selenium import webdriver
import time
import sys
from pyvirtualdisplay import Display


try:
    username = sys.argv[1]
    password = sys.argv[2]

    display = Display(visible=0, size=(800, 800))  
    display.start()
    browser = webdriver.Chrome()
    browser.get('https://yqfk.dgut.edu.cn')
    User = browser.find_element_by_id('username')
    User.send_keys(username)
    Pwd = browser.find_element_by_id('casPassword')
    Pwd.send_keys(password)
    button = browser.find_element_by_id('loginBtn')
    button.click()
    # browser.get('https://yqfk.dgut.edu.cn')
    # print(button.text)
    print(browser.page_source)
    
    browser.close()

except Exception as e:
    print(e)
