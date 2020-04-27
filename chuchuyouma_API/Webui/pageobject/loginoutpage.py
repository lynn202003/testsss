from selenium import webdriver
from Webui.pylib.base_page import basepage
class loginout(basepage):
    def checklefttext(self):  #创建活码页左侧显示的5个title
        getelementstext=self.getelementstext("xpath",'//div[@class="create"]//div[@class="adminEdit"]/div/div/div[1]')
        return getelementstext

    def checkmidtext(self):  # 创建活码页中间显示的4个title
        getelementstext=self.getelementstext("xpath", '.indexTools .btn')
        return getelementstext
    def clickadminlgo(self):   #点击活码管理
        self.click('xpath',"//div[@class='flex-wrap']/div[1]/div[2]/div[1]")
    def clickcreateadminlgo(self):  #点击创建活码
        self.click('xpath',"//div[@class='flex-wrap']/div[1]/div[2]/div[2]")
    def clickvip(self):  #点击开通会员
        self.click('xpath','//div[@class="recharge flex-middle-y"]/div[@class="common-btn"]')
    def checkusername(self): #获取登录用户名
        elementtext=self.elementtext('xpath','//div[@class="account flex-middle-y"]/div[@class="account-name"]')
        return elementtext
