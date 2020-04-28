from selenium import webdriver
from Webui.pylib.base_page import basepage
class createadminlogo(basepage):
    def clickquelogo(self): #点击群聊码
        self.click("css",".create>div:nth-child(1)>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)")

    def clickkefulogo(self): #点击客服码
        self.click('css',".create>div:nth-child(1)>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)")

    def sendkey_title(self,text):  # 输入活码页标题
        self.sendkey('css','.admin-content>div:nth-child(3) .line-content div>input[placeholder*="活码页的页面"]',text)

    def gettitletext(self):  # 获取活码页标题框中默认内容
        elementtext=self.elementtext('css', '.admin-content>div:nth-child(3) .line-content div>input[placeholder*="活码页的页面"]')
        return elementtext

    def sendkey_name(self,text):  # 输入活码备注
        self.sendkey('css','.admin-content>div:nth-child(3) .line-content div>input[placeholder*="为了方便您"]',text)

    def getnametext(self):  # 获取活码备注框中默认内容
        elementtext = self.elementtext('css','.admin-content>div:nth-child(3) .line-content div>input[placeholder*="为了方便您"]')
        return elementtext

    def clickadminlogo(self):  # 点击上传活码logo
        self.click("css",".create-content .adminEdit>div>div:nth-child(4) .common-btn")

    def clickdumber(self):  # 勾选活码设置按扭：防止重复入群
        self.click("css",".create-content .adminEdit>div>div:nth-child(5)>.line-content>div:nth-child(1)>.box-pot")

    def clicksafe(self):  # 勾选活码设置按扭：安全验证提示
        self.click("css", ".create-content .adminEdit>div>div:nth-child(5)>.line-content>div:nth-child(2)>.box-pot")

    def clickkefu(self):  # 勾选活码设置按扭：客服功能
        self.click("css", ".create-content .adminEdit>div>div:nth-child(5)>.line-content>div:nth-child(3)>.box-pot")
    def clicklower(self): #点击下一步
        self.click("css",".create-bar>div:nth-child(3)")
    def clickupper(self):  # 点击上一步
        self.click("css", ".create-bar>div:nth-child(4)")

    def clickkefuma(self):  # 点击活码设置中上传客服码
        self.click("css", ".create-content .adminEdit>div>div:nth-child(5)>.line-content>div:nth-child(3) .common-btn")