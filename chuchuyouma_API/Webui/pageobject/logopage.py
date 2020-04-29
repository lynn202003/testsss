from selenium import webdriver
from Webui.pylib.base_page import basepage
class login(basepage):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    def send_user(self,username):  #输入用户名
        self.sendkey("css",".board>div:nth-child(4)>div:nth-child(1) input",username)

    def send_password(self, password):  # 输入密码
        self.sendkey("css", ".board>div:nth-child(4)>div:nth-child(2) input", password)

    def click_login(self):  # 点击登录按扭
        self.click("css", ".board>div:nth-child(6)")

    def click_denglu(self):
        self.click("css","img[src*='7f220071.png']+div>div:nth-child(2)")

    def click_ringlogin(self):
        self.click("css","board-toScan>img:nth-child(1)")

    def login_password_error(self):
        password_error_text=self.elementtext("css","div[style*='margin-top']>div:nth-child(2) .input-warn")
        return password_error_text








