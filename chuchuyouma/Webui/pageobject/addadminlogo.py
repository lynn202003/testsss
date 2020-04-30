from selenium import webdriver
from Webui.pylib.base_page import basepage
class addadminlogo(basepage):
    def clicknormalmode(self): #点击标准模式
        self.click("css",".create-content>.childEdit>.create-form>div:nth-child(2)>div>div:nth-child(1)>.box-name")
    def clickquelogo(self): #点击适配模式
        self.click("css",".create-content>.childEdit>.create-form>div:nth-child(2)>div>div:nth-child(2)>.box-name")

    def clickquelogo(self):  # 点击裁剪模式
        self.click("css", ".create-content>.childEdit>.create-form>div:nth-child(2)>div>div:nth-child(3)>.box-name")
    def sendtitle(self,text):  #输入群聊名称
        self.sendkey("css",'.create-content>.childEdit input[placeholder="请输入名称"]',text)

    def clickqunma(self):  # 点击上传群聊码按扭
        self.click("css", '.create-content>.childEdit>.create-form>div:nth-child(4) .common-btn')

    def clickdelimg(self):  # 点击删除图片按扭
        self.click("css", '.create-content>.childEdit>.create-form>div:nth-child(4) .box-bot')

    def deleallimg(self,by,values):  # 删除所有图片按扭
        self.delallimg("css", '.create-content>.childEdit>.create-form>div:nth-child(4) .box-bot')


    def clickqunimg(self):  # 点击自定义群头像
        self.click("css", '.create-content>.childEdit>.create-form>div:nth-child(5) .common-btn')

    def sendpinlv(self, text):  # 输入切换频率
        self.sendkey("css", '.create-content>.childEdit input[placeholder="请输入切换频率"]',text)
    def clearpinlv(self):   # 清除切换频率
        self.cleartext("css", '.create-content>.childEdit input[placeholder="请输入切换频率"]')

    def send_beizhu_text(self, text):  # 输入引导文字
        self.sendkey("css", '.create-content>.childEdit textarea[type="textarea"]', text)

    def clicklower(self):  # 点击下一步
        self.click("css", ".create-bar>div:nth-child(5)")

    def clickupper(self):  # 点击上一步
        self.click("css", ".create-bar>div:nth-child(6)")