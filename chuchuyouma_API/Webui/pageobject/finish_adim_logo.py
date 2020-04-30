from selenium import webdriver
from Webui.pylib.base_page import basepage
from Webui.logs.log import log1
class finish_adim_logo(basepage):
    def fininsh_admin_img(self):   #成功生成活码图片
        self.find_element("css",".result-image")
        log1.info("成功生成活码图片")
    def link(self): #永久链接
        self.find_element("css",".result-image+.result-link")

    def click_link(self): #点击永久链接
        self.click("css",".result-image+.result-link")

    def load_link(self): #点击下载二维码
        self.click("css",".result-image+.result-link+.result-link>.common-link")

    def click_finish(self): #点击完成
        self.click("css",".create-bar>div:nth-child(9)")

    def click_againadd(self):  # 点击再次创建
        self.click("css", ".create-bar>div:nth-child(10)")




