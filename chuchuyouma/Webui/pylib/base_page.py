from selenium import webdriver
from Webui.cfg import *
import time
import os
from Webui import getcwd
from Webui.logs.log import log1
class basepage:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self,driver):
        self.driver=driver

    def get_img(self):# 截图
        path=os.path.join(getcwd.get_cwd(),'screenshots/')  # 拼接截图保存路径
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time())) # 按格式获取当前时间
        screen_name=path+rq+'.png'  # 拼接截图文件名
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log1.info("截图保存成功")
        except BaseException:
            log1.error("截图失败", exc_info=1)


    def find_element(self,by,values):#查找某个元素
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by=='id':
                    element=self.driver.find_element_by_id(values)
                elif by=='name':
                    element=self.driver.find_element_by_name(values)
                elif by=='class':
                    element=self.driver.find_element_by_class_name(values)
                elif by=='css':
                    element=self.driver.find_element_by_css_selector(values)
                elif by=='xpath':
                    element=self.driver.find_element_by_xpath(values)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(values)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(values)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(values)
                else:
                    log1.error("没有找到元素")
                log1.info(f'元素定位成功，定位方式:{by},使用的值是{values}')
                return element
            except:
                log1.error('报错信息：',exc_info=1)
                self.get_img() #调用截图
        else:
            log1.error('输入的元素定位方式错误')

    def find_elements(self,by,values):#查找多个元素
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by=='id':
                    elements=self.driver.find_elements_by_id(values)
                elif by=='name':
                    elements=self.driver.find_elements_by_name(values)
                elif by=='class':
                    elements=self.driver.find_elements_by_class_name(values)
                elif by=='css':
                    elements=self.driver.find_elements_by_css_selector(values)
                elif by=='xpath':
                    elements=self.driver.find_elements_by_xpath(values)
                elif by == 'tag':
                    elements = self.driver.find_elements_by_tag_name(values)
                elif by == 'link':
                    elements = self.driver.find_elements_by_link_text(values)
                elif by == 'plink':
                    elements = self.driver.find_elements_by_partial_link_text(values)
                else:
                    log1.error("没有找到元素")
                log1.info(f'元素定位成功，定位方式是:{by},使用的值是{values}')
                return elements
            except:
                log1.error('报错信息：', exc_info=1)
                self.get_img()  # 调用截图
        else:
            log1.error('输入的元素定位方式错误')

      #封装获取元素的值
    def elementtext(self,by,values):
        element=self.find_element(by,values)
        try:
            ele_text=element.text
            log1.info(f'获取元素的内容是:{ele_text}')
            return ele_text
        except:
            log1.error("获取元素内容失败",exc_info=1)
            self.get_img()
     #封装输入方法
    def sendkey(self,by,values,text):
        element=self.find_element(by,values)
        try:
            element.send_keys(text)
            log1.info(f'输入的内容是{text}')
        except BaseException:
            log1.error("内容输入报错",exc_info=1)
            self.get_img()
#封装点击方法
    def click(self,by,values):
        element=self.find_element(by,values)
        try:
            element.click()
            log1.info('点击元素成功')
        except:
            log1.error('点击元素报错',exc_info=1)
            self.get_img()

        #封装获取多个元素值的方法
    def getelementstext(self,by,values):
        elements=self.find_elements(by,values)
        try:
            eles_text=[element.text for element in elements]
            newlist = ",".join(eles_text)
            log1.info(f'获取到的元素的值是:{newlist}')
            return newlist
        except:
            log1.error('获取元素值时报错',exc_info=1)
            self.get_img()

    def openbrow(self,url):#打开网页
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        log1.info('打开网页')
    def closebrow(self):#关闭网页
        self.driver.close()
        log1.info('关闭网页')

    def alert_text(self): #获取浏览器自带弹框的text
        time.sleep(4)
        try:
            textb=self.driver.switch_to.alert
            texts=textb.text
            log1.info(f"获取浏览器自带弹框值为:{texts}")
            return texts
        except:
            log1.error("获取浏览器自带弹框值失败",exc_info=1)
            self.get_img()

    def click_alert(self): #点击自带弹框
        time.sleep(2)
        try:
            textb=self.driver.switch_to.alert
            textb.accept()
            log1.info("系统自带弹框点击确定按扭")
        except:
            log1.error("自带弹框点击失败",exc_info=1)
            self.get_img()

    def uploadimg(self,pathload):   #上传图片
        import win32com.client
        # from selenium.webdriver.common.keys import Keys
        shell = win32com.client.Dispatch("WScript.Shell")
        try:
            shell.sendkeys(f'{pathload}' + '\r\n')
            time.sleep(2)
            log1.info("上传图片正确")
        except:
            log1.error("上传图片失败",exc_info=1)
            self.get_img()

    def cleartext(self,by,values): #清除数据
        self.find_element(by,values).clear()
        log1.info("数据清除成功")

    def delallimg(self,by,values):#删除所有图片
        elements=self.find_elements(by,values)
        try:
            for i in range(0,len(elements)):
                if elements > 1:
                    elements[0].self.click(by,values)

                else:
                    break
                log1.info("删除所有图片成功")
        except:
            log1.error("删除所有图片失败",exc_info=1)
            self.get_img()

if __name__ == '__main__':
    a=basepage()
    a.openbrow("http://www.ccym88.com")



