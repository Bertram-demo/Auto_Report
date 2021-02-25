from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import json
import datetime
from pyvirtualdisplay import Display

def utc_local(t: datetime.datetime):
    if isinstance(t, datetime.datetime):
        return t+datetime.timedelta(hours=8)
    return False

def report(username: str, password: str):
    '''
    使用selenium模拟打卡

    username => dgut中央认证账号

    password => 密码
    '''
    try:
        # 登录
        display = Display(visible=0, size=(800, 800))  
        display.start()
        browser = webdriver.Chrome()
        browser.get('https://yqfk.dgut.edu.cn')
        user = browser.find_element_by_id('username')
        pwd = browser.find_element_by_id('casPassword')
        login = browser.find_element_by_id('loginBtn')
        user.send_keys(username)
        pwd.send_keys(password)
        if not login:
            raise ValueError('找不到登录按钮')
        login.click()

        # 点击提交   
        wait = WebDriverWait(browser, 30)
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.am-button-primary')))
        if not submit:
            raise ValueError('找不到提交按钮')
        submit.click()
        result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.remind___fRE9P')))
        info = {'code':1, 'message': f'打卡成功！{result[0].text}'}

    except IndexError:
        info = {'code': 0, 'message': '请完整输入账号和密码（核对是否设置了Secrets）'}

    except ValueError as e:
        info = {'code': 0, 'message': e}

    except common.exceptions.TimeoutException:
        result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.remind___fRE9P')))
        if "您已连续打卡" in result[0].text:
            info = {'code': 1, 'message': f"今日已提交过了，{result[0].text}"}
        else:
            info = {'code': 0, 'message': "请求超时，原因可能是服务器有问题无法加载成功"}

    except:
        info = {'code': -1, 'message': "服务器无法响应或密码错误"}

    finally:
        if 'browser' in dir():
            browser.close()
        return info


if __name__ == '__main__':
    try:

        # 获取账号密码
        username = sys.argv[1]
        password = sys.argv[2]

        # 0点20分启动
        while True:
            now = utc_local(datetime.datetime.utcnow())
            if now.hour == 0 and now.minute >= 20:
                break
            if 0 < now.hour < 23:
                print(f"当前时间是{now.hour}:{now.minute}，没有打卡计划")
                exit()

        # 程序启动：当打卡成功、已打过卡、密码错误或服务器发生未知错误时退出
        print("Script start...")
        print("-"*20)
        count = 1
        while count <= 10:
            print(f"第{count}次尝试打卡...")
            result = report(username, password)
            print(result['message'])
            if result:
                break
            count += 1
            time.sleep(60*10)
        print("-"*20)
        print("Script end...")
        if count > 10:
            raise Exception

    except IndexError:
        print("请完整输入账号和密码（核对是否设置了Secrets）")
