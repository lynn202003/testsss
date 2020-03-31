from appium import webdriver
import time
desired_caps={"platformName":"Android",
              "platformVersion":"8.1",
              "deviceName":"test",
              "appPackage":"com.tencent.mm",
              "appActivity":".ui.LauncherUI",
              "unicodeKeyboard":True,
              "resetKeyboard":True,
              "noReset":True,
              "newCommandTimeout":6000,
             "automationName":"UIAutomator2"
              }
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
#找到微信下面的发现按扭并点击
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/bv']//android.widget.RelativeLayout[3]").click()
#找到小程序按扭并点击,等2S
driver.find_element_by_xpath("//*[@resource-id='android:id/list']/android.widget.LinearLayout[9]").click()
time.sleep(2)
#当出现右侧的图标时再对附近的小程序进行点击
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/w_']//android.widget.FrameLayout[@resource-id='com.tencent.mm:id/w7']")
#找到附近的小程序并点击
driver.find_element_by_id("com.tencent.mm:id/w_").click()
time.sleep(2)
#找到外卖并点击
driver.find_element_by_xpath("//android.webkit.WebView/android.view.View[2]//android.view.View[@text='外卖']").click()
time.sleep(2)

#获取起始和终点的xy坐标
def swipeup(t):#向上滑动
    size=driver.get_window_size()
    x=size['width']*0.5    #起始X坐标
    y=size['height']*0.6   #起始y坐标
    y1=size['height']*0.4   #终点Y坐标
    driver.swipe(x, y, x, y1, t)

#如果找到元素就点击，没有找到就继续上滑
def find_swipe(elemts,elemtsr,t):
    while True:
        swipeup(t)
        time.sleep(0.3)
        driver.implicitly_wait(0.1)
        shop = driver.find_elements_by_xpath(elemts)
        if shop:
            driver.find_element_by_xpath(elemtsr).click()
            break

#找到小面馆点击
a="//android.webkit.WebView/android.view.View[5]/android.view.View[@text='HI小面(学林路店)']"
b="//android.webkit.WebView/android.view.View[5]"
find_swipe(a,b,500)
time.sleep(2)
#找到点餐按扭，对要加购的元素点击+
driver.find_element_by_xpath("//android.webkit.WebView/android.view.View[3]//android.view.View[@text='点餐']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@resource-id='list-13374']//android.view.View[4]/android.widget.Image").click()
driver.find_element_by_xpath("//*[@resource-id='id_76046_13375']/following-sibling::android.view.View").click()
driver.find_element_by_xpath("//*[@resource-id='nav-13378']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@resource-id='list-13378']//*[@resource-id='id_76083_13378']/following-sibling::android.view.View").click()



