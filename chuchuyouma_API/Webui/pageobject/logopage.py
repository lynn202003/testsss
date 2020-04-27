from selenium import webdriver
from Webui.pylib.base_page import basepage
class login(basepage):
    def send_user(self,username):  #输入用户名
        self.sendkey("css",".board>div:nth-child(4)>div:nth-child(1) input",username)

    def send_password(self, password):  # 输入密码
        self.sendkey("css", ".board>div:nth-child(4)>div:nth-child(2) input", password)

    def click_login(self):  # 点击登录按扭
        self.click("css", ".board>div:nth-child(6)")








