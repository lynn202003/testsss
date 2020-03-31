#coding:utf8
from selenium import  webdriver
from cfg import *
import time
#driver = webdriver.Chrome(r"D:\software\chromedriver\78\chromedriver_win32\chromedriver.exe")
#driver.implicitly_wait(10)

def startBrowser(name):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if name=="firefox" or name=="Firefox" or name=="ff":
            print("start browser name:Firefox")
            driver=webdriver.Firefox()
            return driver
        elif name=="chrome" or name=="Chrome":
            print("start browser name:Chrome")
            driver=webdriver.Chrome(r"D:\software\chromedriver\78\chromedriver_win32\chromedriver.exe")
            return driver
        elif name=="ie" or name=="Ie":
            print("start browser name:Ie")
            driver=webdriver.Ie()
            return driver
        else:
            print("Not found this browser,You can use'firefox','chrome','id'or'phantomjs'")
    except:
        print("启动浏览器出现异常：%s"%(name,))

def run_case(name):
        driver=startBrowser(name)
        driver.implicitly_wait(10)



class webtest():
    #定义一个初始化函数
    def __init__(self,username,password,a):
        self.username=username
        self.password=password
        self.a=a

    def login(self):
        driver.get(self.a)
        driver.find_element_by_id('txt_name').send_keys(self.username)
        driver.find_element_by_css_selector("#txt_pwd").send_keys(self.password)
        driver.find_element_by_css_selector("#btn_submit").click()
        driver.maximize_window()
      #  driver.quit()
    #检查左侧页面页签内容
    def pagechecked(self):
        self.login()
     #   driver.maximize_window()
        li=driver.find_elements_by_xpath("//div/ul/li")
        newlist=[]
        for i in li:
           newlist.append(i.text)
        a="|".join(newlist)
        return a
    #检查商户管理内容
    def merchant(self):
        self.login()
    #    driver.maximize_window()
        driver.find_element_by_css_selector("div>ul>li:nth-child(2)").click()
        li=driver.find_elements_by_css_selector("div>ul>li:nth-child(2) li")
        newlist=[]
        for i in li:
            newlist.append(i.text)
        print(newlist)

    #填写更多信息
    def basic(self):
         self.login()
         import win32com.client
      #   driver.maximize_window()
         driver.find_element_by_css_selector("div>ul>li:nth-child(2) span").click()
         driver.find_element_by_css_selector("li>a[href='MerchantInfo.aspx']").click()
         time.sleep(2)
         a=driver.find_element_by_css_selector(".row>div:nth-child(4) .form-horizontal>div:nth-child(1) input")
         a.clear()
         a.send_keys("test名字哈哈哈能否成功呢")
         b=driver.find_element_by_css_selector(".row>div:nth-child(4) .form-horizontal>div:nth-child(2) input")
         b.clear()
         b.send_keys("16625452582")
         driver.execute_script("window.scrollTo(0, 600)")
         #找到上传图片的按扭
         element=driver.find_element_by_id("ContentPlaceHolder1_LOGOImageFileUpload")
         # 通过JS方法进行点击操作
        # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
         driver.execute_script("arguments[0].click()", element)
    #     fly = driver.find_element_by_css_selector(".row>div:nth-child(4) .col-sm-2>input[type=file]")
         time.sleep(2)
         # fly.send_keys(r"d:\bbaidu.jpg"+ '\n')
         #上传图片
         from selenium.webdriver.common.keys import Keys
         shell = win32com.client.Dispatch("WScript.Shell")
         #   shell.Sendkeys(r"d:\bbaidu.jpg")
         shell.sendkeys(r"d:\bbaidu.jpg" + '\r\n')
         # send_keys(Keys.ENTER)
         # shell.send_keys(r"d:\bbaidu.jpg"+ '{ENTER}'+'\n')
         time.sleep(2)

         phone=driver.find_element_by_id("ContentPlaceHolder1_s_FileUpload1")
         driver.execute_script("arguments[0].click()",phone)
         time.sleep(2)
         shell.Sendkeys(r"d:\bbaidu.jpg"+"\r\n")
         time.sleep(2)
         driver.find_element_by_css_selector(".col-sm-9>div:nth-child(1)>div>input").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[1]/li[6]").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[2]/li[6]").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[3]/li[5]").click()
         driver.find_element_by_css_selector(".setok").click()
         driver.find_element_by_css_selector(".col-sm-9>div:nth-child(3)>div>input").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[1]/li[7]").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[2]/li[5]").click()
         driver.find_element_by_xpath("//div[@class='contime']/ul[3]/li[4]").click()
         driver.find_element_by_css_selector(".setok").click()
         checkbox=driver.find_element_by_css_selector("[type=checkbox]")
         select=checkbox.is_selected()
         if select:
             print("已经选中")
         else:
             checkbox.click()
         driver.find_element_by_css_selector(".form-horizontal>div:nth-child(7) input").send_keys("jijiji")
         driver.find_element_by_css_selector(".form-horizontal>div:nth-child(8) input").send_keys("48545")
         driver.find_element_by_css_selector('[value="确认"]').click()

class goods(webtest):
    #检查商品列表页面title 字段是否正确
    def checktitle(self):
        webtest.login(self)
        driver.find_element_by_css_selector("div>ul>li:nth-child(2)").click()
        driver.find_element_by_css_selector("li>a[href='GoodsManage.aspx']").click()
        titlename=driver.find_elements_by_css_selector('thead>tr[role="row"]>th')
        newlist=[]
        for title in titlename:
            newlist.append(title.text)
        a=",".join(newlist)
        print(a)
        filename="商品编号,商品名称,进货单价(元),出货单价(元),商品数量,商品规格,上架,入库时间,操作"
        if a==filename:
            print("测试通过")
        else:
            print(f'测试不通过，{filename},{a}')
          #  print("测试不通过,filename: "+"%s"%(filename,)+"  ,a: ""%s"%(a,))
        # 检查商品是否添加成功，初始化条件，将商品列表中的商品全部删除，再进行添加，添加完后查看页面中的内容包含刚刚添加的内容即添加成功
    def deletegood(self):
        # 先定义一个死循环
        while True:
             # 找到商品列表中所有的删除按扭
            alldelete = driver.find_elements_by_css_selector("tbody>tr>td:nth-child(9)>button:nth-child(2)")
            # 如果商品列表不为空，则点击第一个元素
            if alldelete == []:
                break
            else:
                alldelete[0].click()
                time.sleep(1)
                driver.find_element_by_id("ContentPlaceHolder1_btnDelete").click()
                time.sleep(1)

#添加商品
    def add(self,):
         import win32com.client
         driver.find_element_by_css_selector(".pull-right input").click()
         driver.find_element_by_id("ContentPlaceHolder1_txtGoodsName").send_keys("我要喝娃哈哈")
         driver.find_element_by_id("ContentPlaceHolder1_txtGoodsNorms").send_keys("一箱")
         driver.find_element_by_id("ContentPlaceHolder1_txtGoodsCount").send_keys("42")
         driver.find_element_by_id("ContentPlaceHolder1_txtPurchasePrice").send_keys("12")
         driver.find_element_by_id("ContentPlaceHolder1_txtOfferPrice").send_keys("23")
         driver.find_element_by_id("ContentPlaceHolder1_txtSort").send_keys("2")
         driver.find_element_by_id("ContentPlaceHolder1_txtGoodsExplain").send_keys("娃哈哈很好喝，快来买，又例如宜好")
         #滚动条滑到最底部
         js = "var q=document.documentElement.scrollTop=10000"
         driver.execute_script(js)
         #点击按扭
         chenck=driver.find_element_by_css_selector(".col-sm-6>input")
         driver.execute_script("arguments[0].click()",chenck)
         time.sleep(2)
         #上传图片
         shell=win32com.client.Dispatch("WScript.Shell")
         shell.sendkeys(r"d:\bbaidu.jpg"+'\r\n')
         time.sleep(2)
         driver.find_element_by_id("ContentPlaceHolder1_btnSave").click()
#检查是否添加成功
    def checkadd(self):
        self.deletegood()
        self.add()
        name=driver.find_element_by_xpath('//tr[@class="odd"]/td[2]').text
        dor=driver.find_element_by_xpath('//tr[@class="odd"]/td[3]').text
        price = driver.find_element_by_xpath('//tr[@class="odd"]/td[4]').text
        count = driver.find_element_by_xpath('//tr[@class="odd"]/td[5]').text
        if name=="我要喝娃哈哈" and dor=="12.00" and price=="23.00" and count=="42":
            print("商品添加成功")
        else:
            print(f'商品添加不成功，商品名称是{name},进货单价是{dor},出货单价是{price},商品数量是{count}')

    #添加职位
    def job(self):
        from selenium.webdriver.support.ui import Select
        import win32com.client
        driver.find_element_by_css_selector("div>ul>li:nth-child(7)").click()
        driver.find_element_by_css_selector("li>a[href='PublishJob.aspx']").click()
        driver.find_element_by_css_selector(".form-horizontal .form-group:nth-child(1)>.col-md-6>input[type=text]").send_keys("招临时工")
        select=Select(driver.find_element_by_id("ContentPlaceHolder1_selPayType"))
        select.select_by_visible_text("周结")
        driver.find_element_by_css_selector(".form-horizontal .form-group:nth-child(3)>.col-md-6>input[type=text]").send_keys("50")
        date=Select(driver.find_element_by_id("ContentPlaceHolder1_selSalaryCycleType"))
        date.select_by_visible_text("周")
        driver.find_element_by_id("ContentPlaceHolder1_txtEmployNum").send_keys("10")
        #找到元素进行点击，通过JS方式点击
        picture=driver.find_element_by_id("ContentPlaceHolder1_FileUpload4")
        driver.execute_script("arguments[0].click()",picture)
        time.sleep(1)
        #上传文件
        shell=win32com.client.Dispatch("WScript.Shell")
        shell.sendkeys(r"d:\bbaidu.jpg"+'\r\n')
        time.sleep(1)
        driver.find_element_by_id("ContentPlaceHolder1_btnSave").click()

    # 检查商品是否添加成功，初始化条件，将商品列表中的商品全部删除，再进行添加，添加完后查看页面中的内容包含刚刚添加的内容即添加成功






#c=webtest(localuser,localpass,localhost)
#c.basic()
#d=webtest(urluser,urlpass,urlhost)
#d.login()
g=goods(urluser,urlpass,urlhost)
g.checktitle()
g.deletegood()
#g.add()
#g.checkadd()
#g.job()
#c.pagechecked()
#c.merchant()


