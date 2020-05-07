from selenium import webdriver
from Webui.pageobject.logopage import login
from Webui.pageobject.loginoutpage import loginout
import time
from Webui.pylib.getdriver import getwebdriver
from Webui.pylib.base_page import basepage

def logincusess(username,password,url):
    openbrowns=basepage(getwebdriver)
    openbrowns.openbrow(url)
    login_user = login(getwebdriver)
    login_user.click_denglu()
    time.sleep(2)
    login_user.click_ringlogin()
    time.sleep(2)
    login_user.send_user(username)
    login_user.send_password(password)
    login_user.click_login()
    time.sleep(4)
    login_sucess_page = loginout(getwebdriver)
    if login_sucess_page.checkusername() == username:
        print("帐号登录成功")
    else:
        print("没有登录成功")

if __name__ == '__main__':
    logincusess("13262849250","test123456","http://192.168.0.241:3003/")
