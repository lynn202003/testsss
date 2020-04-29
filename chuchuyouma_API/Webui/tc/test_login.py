from selenium import webdriver
from Webui.pageobject.logopage import login
from Webui.pageobject.loginoutpage import loginout
from Webui.pylib.base_page import basepage
import time
import unittest
class test_login(unittest.TestCase):
    def setUp(self):
        bro=basepage()
        self.driver=bro.openbrow("http://www.ccym88.com")

    def tearDown(self):
        self.driver.quite()

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

    def login_user_fail(self):
        self.driver.find_element_by_css_selector("img[src*='7f220071.png']+div>div:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".board-toScan>img:nth-child(1)").click()
        time.sleep(2)
        login_user = login(self.driver)
        login_user.send_user("13262849250")
        login_user.send_password("123456")
        login_user.click_login()
        time.sleep(3)
        if login_user.login_password_error()=="请输入至少6位数字+字母":
            print("密码格式不对")


#     def checkloginout(self):
#
#         if self.checklefttext()=="首页,数据概览,活码工具,二维码工具,消息中心,会员中心" and self.checkmidtext()=='活码管理,创建活码,二维码管理,生成二维码':
#             print('页面内容显示正确')
#         else:
#             print("页面内容显示错误")
#         self.closebrow()
#
# a=testlogopage()
# a.login_sucess()
# a.checkloginout()

