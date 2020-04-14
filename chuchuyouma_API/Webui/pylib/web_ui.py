from selenium import webdriver
from cfg import *
import time
class web_ui:
#打开不同的浏览器调用不同的驱动

    def exe(self):
        global driver
        if a==firefoxexe:

            driver=webdriver.Firefox(a)
        elif a==google:
            driver=webdriver.Chrome(a)
    # driver=webdriver.Firefox(executable_path=r'D:\software\火狐浏览器\geckodriver-v0.26.0-win64\geckodriver.exe')
    # driver = webdriver.Chrome(r"D:\software\chromedriver\chrome版本 80.0.3987\chromedriver.exe")
    def open(self):#打开网页
        self.driver.get("http://www.ccym88.com")
        # self.driver.get("http://192.168.0.241:3003/")
        self.driver.implicitly_wait(10)
    def checkinfo(self):
        phonetext = self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(1) input")
        if phonetext.get_attribute("placeholder") == "请输入您的手机号/神手云账号":
            print("pass")
        passwordtext = self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(2) input")
        if passwordtext.get_attribute("placeholder") == "请输入您的密码":
            print("pass")

    def login(self,username,password):#登录
        self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(1) input").send_keys(username)
        self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(2) input").send_keys(password)
        self.driver.find_element_by_css_selector(".common-btn").click()
        values=self.driver.find_element_by_xpath('//div[@class="account flex-middle-y"]/div[@class="account-name"]')
        if username in values.text:
            print("帐号登录成功")

    # def paymoney(self):
    #     self.driver.find_element_by_css_selector(".bar-list>div:nth-child(6)>div:nth-child(2)>div:nth-child(1) .name")
    #     uservip = self.GetUserVipInfo()
    #     userlevel = uservip["result"]["level"]  # 获取当前用户等级
    #     if userlevel == 0 or userlevel == 1:  # 等级为0或者1时，id只能为2345
    #         elements=self.driver.find_elements_by_css_selector(".recharge-package>div")
    #         for one in elements:
    #             one.click()
    #             self.driver.find_element_by_css_selector(".recharge>div:nth-child(3) .common-modal-blank")
    #             self.driver.find_element_by_xpath("//div[@class='flex-side']/div[@class='common-btn tip tip-on']").click()
    #             self.driver.find_element_by_xpath( "//div[@class='flex-side']/div[@class='common-btn tip tip-on']").click()
    #
    #     elif userlevel ==2:  # 等级为2时，id只能为45
    #         elements=self.driver.find_elements_by_css_selector(".recharge-package>div")
    #         moneyinfo = self.Calculation(id)
    #         payorder = self.GetPayOrder(cycle, moneyinfo["result"]["money"], type, id)
    #         self.PayBack(type, payorder["result"]["orderNo"]
    #



    def addadmincode(self):#创建活码
        import win32com.client
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//div[@class="tool-btns flex"]/div[2]').click()  #点击创建活码
        self.driver.find_element_by_css_selector(".create-bar>div:nth-child(1)").click()  #点击我已详细阅读，进入下一步
        self.driver.find_element_by_css_selector(".create>div:nth-child(1)>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)").click()    #点击群聊码
        self.driver.find_element_by_css_selector('.admin-content>div:nth-child(2) .line-content div>input[placeholder*="活码页的页面"]').send_keys("取个标题吧")
        self.driver.find_element_by_xpath("//div[@class='admin-board flex-y']/div[5]/div[2]/div[1]/div[3]/div[1]/div[4]//div[@class='common-btn']").click()

        time.sleep(2)
        # 上传图片
        from selenium.webdriver.common.keys import Keys
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.sendkeys(r"d:\bbaidu.jpg" + '\r\n')
        time.sleep(2)
        self.driver.quit()



if __name__ == '__main__':
    web_ui=web_ui()
    web_ui.open()
    web_ui.login("13262849250","test123456")
    # web_ui.addadmincode()