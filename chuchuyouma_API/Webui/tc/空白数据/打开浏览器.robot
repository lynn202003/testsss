*** Settings ***
Library  SeleniumLibrary
Library  Webui.pylib.base_page.basepage
Library  Webui.pageobject.loginoutpage.loginout
Library  Webui.pageobject.logopage.login
Suite Setup   openbrow     http://www.ccym88.com
Suite Teardown     closebrow
*** Test Cases ***
登录成功--ui00001
    find_element    css      img[src*='7f220071.png']+div>div:nth-child(2)
    sleep     2
    find_element    css      .board-toScan>img:nth-child(1)
    sleep     2
    send_user     13262849250
    send_password     test123456
    click_login
    sleep    3                   
    should be Equal     checkusername      13262849250

检查登录后页面显示--ui00002
    ${getelementstext}     checklefttext
    ${getelementstext}         checkmidtext
    run keyword if   ${getelementstext}=="首页,数据概览,活码工具,二维码工具,消息中心,会员中心"  and  ${getelementstext}=='活码管理,创建活码,二维码管理,生成二维码'
    ...  log to console       页面内容显示正确


