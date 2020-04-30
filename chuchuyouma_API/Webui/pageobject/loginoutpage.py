from selenium import webdriver
from Webui.pylib.base_page import basepage
class loginout(basepage):

    def checklefttext(self):  #左侧列表5个导航
        getelementstext=self.getelementstext("css",'.bar-list>div')
        return getelementstext

    def checkmidtext(self):  # 创建活码页中间显示的4个title
        getelementstext=self.getelementstext("css", '.indexTools .btn')
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

    def click_hmgl(self):  #点击左侧导航栏中活码管理
        hmgl=self.click("css",'.bar-list>div:nth-child(3)>div:nth-child(2)>div:nth-child(2)')

    def click_cjhm(self):  #点击左侧导航栏中创建活码
        cjhm=self.click("css",'.bar-list>div:nth-child(3)>div:nth-child(2)>div:nth-child(1)')
    def click_sjgl(self):  #点击左侧导航栏中数据概览
        sjgl=self.click("css",'.bar-list>div:nth-child(2)')

    def click_news(self):  # 点击左侧导航栏中消息中心
        news = self.click("css", '.bar-list>div:nth-child(5)')

    def click_vips(self):  # 点击左侧导航栏中会员中心
        vips = self.click("css", '.bar-list>div:nth-child(6)')

    def click_homepage(self):  # 点击左侧导航栏首页
        homepage= self.click("css", '.bar-list>div:nth-child(1)')

    def click_ewmgj(self):  # 点击左侧导航栏二维码工具
        ewmgj= self.click("css", '.bar-list>div:nth-child(4)')