from selenium import webdriver
from Webui.cfg import *
import time
class web_ui:
#打开不同的浏览器调用不同的驱动
    ROBOT_LIBRARY_SCOPE = "GLOBAL"  # 解决初始化生成的实例和用例生成的实例是同一个实例
    def __init__(self):
        if a==firefox_path:
            self.driver=webdriver.Firefox(executable_path=a)
        elif a==google_path:
            self.driver=webdriver.Chrome(a)
    #     elif a==edgedriver_path:
    #         self.driver=webdriver.Edge(executable_path=a)
    # driver=webdriver.Edge(executable_path=r'D:\software\edgedriver\edgedriver_win64\MicrosoftWebDriver.exe')
    # driver=webdriver.Firefox(executable_path=r'D:\software\火狐浏览器\geckodriver-v0.26.0-win64\geckodriver.exe')
    # driver = webdriver.Chrome(r"D:\software\chromedriver\chrome版本 80.0.3987\chromedriver.exe")
    def openbrow(self):#打开网页
        self.driver.get("http://www.ccym88.com")
        # self.driver.get("http://192.168.0.241:3003/")
        self.driver.implicitly_wait(10)
    def closebrow(self):#关闭网页
        self.driver.close()

    def checkinfo(self):
        phonetext = self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(1) input")
        if phonetext.get_attribute("placeholder") == "请输入您的手机号/神手云账号":
            print("pass")
        passwordtext = self.driver.find_element_by_css_selector(".board>div:nth-child(3)>div:nth-child(2) input")
        if passwordtext.get_attribute("placeholder") == "请输入您的密码":
            print("pass")


    def login(self,username,password):#登录
        self.driver.find_element_by_css_selector("img[src*='7f220071.png']+div>div:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".board-toScan>img:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".board>div:nth-child(4)>div:nth-child(1) input").send_keys(username)
        self.driver.find_element_by_css_selector(".board>div:nth-child(4)>div:nth-child(2) input").send_keys(password)
        self.driver.find_element_by_css_selector(".board>div:nth-child(6)").click()
        time.sleep(2)
        values=self.driver.find_element_by_xpath('//div[@class="account flex-middle-y"]/div[@class="account-name"]')
        if values.text=='13262849250':
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
        self.driver.find_element_by_css_selector('.admin-content>div:nth-child(3) .line-content div>input[placeholder*="活码页的页面"]').send_keys("取个标题吧")
        self.driver.find_element_by_css_selector(".create-bar>div:nth-child(3)").click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector('.create-content>.childEdit input[placeholder="请输入名称"]').send_keys("4.27命名")
        self.driver.find_element_by_css_selector(".create-content>.childEdit>.create-form>div:nth-child(4) .common-btn").click()#上传群聊码
        time.sleep(2)
        # 上传图片
        from selenium.webdriver.common.keys import Keys
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.sendkeys(r"d:\bbaidu.jpg" + '\r\n')
        time.sleep(2)
        self.driver.find_element_by_css_selector(".create-content>.childEdit>.create-form>div:nth-child(5) .common-btn").click() #上传头像
        shell.sendkeys(r"d:\bbaidu.jpg" + '\r\n')
        time.sleep(2)
        self.driver.find_element_by_css_selector('.create-content>.childEdit input[placeholder="请输入切换频率"]').send_keys("10")  #输入切换频率
        # self.driver.find_element_by_css_selector('.create-content>.childEdit input[readonly="readonly"]').click()#选择日期
        self.driver.find_element_by_css_selector('.create-content>.childEdit textarea[type="textarea"]').send_keys("45825825455")
        self.driver.find_element_by_css_selector(".create-bar>div:nth-child(5)").click()  #点击下一步
        self.driver.find_element_by_css_selector(".create-bar>div:nth-child(7)").click()  #点击下一步生成活码
        self.driver.quit()


if __name__ == '__main__':
    webui=web_ui()
    webui.openbrow()
    webui.login("13262849250","test123456")
    # webui.addadmincode()