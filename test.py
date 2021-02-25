from selenium import webdriver, common
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
    # display = Display(visible=0, size=(800, 800))  
    # display.start()
    browser = webdriver.Chrome()
    browser.get('https://yqfk.dgut.edu.cn')
    user = browser.find_element_by_id('username')
    pwd = browser.find_element_by_id('casPassword')
    login = browser.find_element_by_id('loginBtn')
    user.send_keys(username)
    pwd.send_keys(password)
    if not login:
        raise ValueError("找不到登录按钮")
    login.click()

    # 点击提交    
    wait = WebDriverWait(browser, 30)
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.am-button-primary')))
    if not submit:
        raise ValueError("找不到提交按钮")
    submit.click()

except IndexError:
    print("请完整输入账号和密码（核对是否设置了Secrets）")

except ValueError as e:
    print(f"error:{e}")

except common.exceptions.TimeoutException:
    result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.remind___fRE9P')))
    if "您已连续打卡" in result[0].text:
        print(f"今日已提交，{result[0].text}")
    else:
        print("请求超时，原因可能是服务器有问题无法加载成功")
    

# except:
#     print("服务器无法响应")

finally:
    if 'browser' in dir():
        browser.close()