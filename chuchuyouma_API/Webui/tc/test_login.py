from selenium import webdriver
from Webui.pageobject.logopage import login
from Webui.pageobject.loginoutpage import loginout
from Webui.pylib.base_page import basepage
from Webui.pageobject.createadminlogo import createadminlogo
from Webui.pageobject.addadminlogo import addadminlogo
from Webui.pageobject.adminlogo import adminlogo
from Webui.pageobject.finish_adim_logo import finish_adim_logo
from Webui.cfg import *
from Webui.logs.log import log1
import time
import unittest
class test_login(unittest.TestCase):
    '''
       if a == firefox_path:
           driver = webdriver.Firefox(executable_path=a)
           log1.info('打开的浏览器为firefox')
       elif a == google_path:
           driver = webdriver.Chrome(a)
           log1.info('打开的浏览器为Chrome')

       @classmethod
       def setUpClass(cls):
           driver.get("http://www.ccym88.com")
           driver.implicitly_wait(2)
           log1.info("成功打开处处有码官网")

       @classmethod
       def tearDownClass(cls):
           driver.quit()
    '''

    def setUp(self):
        if a == firefox_path:
            self.driver = webdriver.Firefox(executable_path=a)
            log1.info('打开的浏览器为firefox')
        elif a == google_path:
            self.driver = webdriver.Chrome(a)
            log1.info('打开的浏览器为Chrome')
        bro=basepage(self.driver)
        bro.openbrow("http://192.168.0.241:3003/")
        self.driver.maximize_window()
        # bro.openbrow("http://www.ccym88.com")

    def tearDown(self):
        bro=basepage(self.driver)
        bro.closebrow()

    def login_sucess(self):
        login_user=login(self.driver)
        login_user.click_denglu()
        time.sleep(2)
        login_user.click_ringlogin()
        time.sleep(2)
        login_user.send_user("13262849250")
        login_user.send_password("test123456")
        login_user.click_login()
        time.sleep(3)
        login_sucess_page=loginout(self.driver)
        if login_sucess_page.checkusername() == '13262849250':
            print("帐号登录成功")
        else:
            print("没有登录成功")

    def login_password_fail(self):
        login_user = login(self.driver)
        login_user.click_denglu()
        time.sleep(2)
        login_user.click_ringlogin()
        time.sleep(2)
        login_user.send_user("13262849250")
        login_user.send_password("123456")
        login_user.click_login()
        time.sleep(3)
        if login_user.login_password_error()=="请输入至少6位数字+字母":
            print("密码格式不对")

    def login_username_fail(self):
        login_user = login(self.driver)
        login_user.click_denglu()
        time.sleep(2)
        login_user.click_ringlogin()
        time.sleep(2)
        login_user.send_user("13262849111")
        login_user.send_password("test123456")
        login_user.click_login()
        c=basepage(self.driver)
        if c.alert_text()=="该用户不存在，请注册":
            print("该用户不存在，请注册")

    def checkloginout(self):
        self.login_sucess()
        check=loginout(self.driver)
        if check.checklefttext()=="首页,数据概览,活码工具,二维码工具,消息中心,会员中心" and check.checkmidtext()=='活码管理,创建活码,二维码管理,生成二维码':
            print('页面内容显示正确')
        else:
            print("页面内容显示错误")

    def create_logo(self): #创建活码
        self.login_sucess()
        a=loginout(self.driver)
        a.clickcreateadminlgo()
        self.driver.find_element_by_css_selector(".create-bar>div:nth-child(1)").click()
        b=createadminlogo(self.driver)
        b.clickquelogo()
        b.sendkey_title("用unittest取活码页标题")
        b.sendkey_name("我是备注")
        b.clickadminlogo()
        time.sleep(2)
        c=basepage(self.driver)
        c.uploadimg(r"d:\bbaidu.jpg")
        b.clickdumber()
        b.clicksafe()
        b.clicklower()
        d=addadminlogo(self.driver)
        d.sendtitle("我是群聊名称")
        d.clickqunma()
        time.sleep(2)
        c.uploadimg(r"d:\bbaidu.jpg")
        d.clickqunimg()
        c.uploadimg(r"d:\bbaidu.jpg")
        d.clearpinlv()
        d.sendpinlv("6")
        d.send_beizhu_text("我是备注，我是备注")
        d.clicklower()
        e=adminlogo(self.driver)
        e.clicklower()
        f=finish_adim_logo(self.driver)
        f.click_finish()






# a=testlogopage()
# a.login_sucess()
# a.checkloginout()

