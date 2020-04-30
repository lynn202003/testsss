from selenium import webdriver
from Webui.pylib.base_page import basepage
class adminlogo(basepage):
    def clickaddqun(self): #点击添加群聊码
        self.click("css",".create-table>.table-nav>div:nth-child(1)")

    def onoff(self): #开启轮播模式
        elementtext=self.find_element('css','.create-table>.table-nav>div:nth-child(2) .switch-btn')
        classattribute=elementtext.get_attribute('class')
        if "switch-btn-on" not in classattribute:
            self.click("css",".create-table>.table-nav>div:nth-child(2) .switch-btn")

    def clickall(self):  # 点击全选按扭
        self.click("css", ".create-table>.table-nav>div:nth-child(1)")

    def clicktime(self):  # 点击有效期按扭
        self.click("css", ".create-table>.table-nav .right-btns>div:nth-child(1)")

    def clickpingce(self):  # 点击有切换频率按扭
        self.click("css", ".create-table>.table-nav .right-btns>div:nth-child(2)")

    def clickdele(self):  # 点击删除按扭
        self.click("css", ".create-table>.table-nav .right-btns>div:nth-child(3)")

    def clicklower(self):  # 点击下一步
        self.click("css", ".create-bar>div:nth-child(7)")

    def clickupper(self):  # 点击上一步
        self.click("css", ".create-bar>div:nth-child(8)")