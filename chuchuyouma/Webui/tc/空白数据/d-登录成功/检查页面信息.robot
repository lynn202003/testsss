
*** Settings ***
Library  SeleniumLibrary
Variables      Webui/pylib/getdriver.py
Library  Webui.pylib.base_page.basepage      ${getwebdriver}
Library  Webui.pageobject.loginoutpage.loginout       ${getwebdriver}
Library  Webui.pageobject.logopage.login          ${getwebdriver}
Library  Webui.pageobject.main_process
*** Test Cases ***

检查登录后页面显示--ui10001
    ${getlefttext}     checklefttext
    ${getmidtext}       checkmidtext
    run keyword if   $getlefttext=="首页,数据概览,活码工具,二维码工具,消息中心,会员中心" and $getmidtext=='活码管理,创建活码,二维码管理,生成二维码'
    ...  log to console       页面内容显示正确



#创建活码--ui10002
#    clickcreateadminlgo
#    clickelement      CSS=.create-bar>div:nth-child(1)
#    clickquelogo
#    sendkey_title      用unittest取活码页标题11
#    sendkey_name       我是备注11
#    clickadminlogo
#    sleep     2
#    uploadimg       r"d:\bbaidu.jpg"
#    clickdumber
#    clicksafe
#    clicklower
#    sendtitle       我是群聊名称11
#    clickqunma
#    sleep    2
#    uploadimg       r"d:\bbaidu.jpg"
#    clickqunimg
#    uploadimg       r"d:\bbaidu.jpg"
#    clearpinlv
#    sendpinlv       6
#    send_beizhu_text           我是备注，我是备注11
#    clicklower
#    clicklower
#    click_finish
