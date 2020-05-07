
*** Settings ***
Library  SeleniumLibrary
Variables      Webui/pylib/getdriver.py
Variables       Webui/cfg.py
Library  Webui.pylib.base_page.basepage      ${getwebdriver}
Library  Webui.pageobject.loginoutpage.loginout       ${getwebdriver}
Library  Webui.pageobject.logopage.login          ${getwebdriver}
Test Setup   Webui.pylib.base_page.basepage.openbrow     http://www.ccym88.com
Suite Teardown      Webui.pylib.base_page.basepage.closebrow

*** Test Cases ***
登录成功--ui00001
    click_denglu
    sleep     2
    click_ringlogin
    sleep     2
    send_user     13262849250
    send_password     test123456
    click_login
    sleep    3
    ${checkusertext}     checkusername
    should be Equal      ${checkusertext}       13262849250

密码错误--ui00002
    click_denglu
    sleep     2
    click_ringlogin
    sleep     2
    send_user     13262849250
    send_password     123456
    click_login
    sleep    3
    ${checkpasstext}     Webui.pageobject.logopage.login.login_password_error
    should be Equal       ${checkpasstext}        请输入至少6位数字+字母

用户名错误--ui00003
    click_denglu
    sleep     2
    click_ringlogin
    sleep     2
    send_user     13262849111
    send_password     test123456
    click_login
    sleep    3
    ${alerttext}     Webui.pylib.base_page.basepage.alert_text
    should be Equal       ${alerttext}         该用户不存在，请注册
    Webui.pylib.base_page.basepage.click_alert




