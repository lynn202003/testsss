from selenium import webdriver
from Webui.cfg import *
from Webui.logs.log import log1
def getdriver():
    if a == firefox_path:
        driver = webdriver.Firefox(executable_path=a)
        log1.info('打开的浏览器为firefox')
        return driver
    elif a == google_path:
        driver = webdriver.Chrome(a)
        log1.info('打开的浏览器为Chrome')
        return driver
getwebdriver=getdriver()