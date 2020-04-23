*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  Webui.pylib.web_ui
Test Setup    openbrow
Test Teardown     closebrow
*** Test Cases ***
检查打开的网址是否正确----00001
     ${value}     get text     css=img[src*='7f220071.png']+div>div:nth-child(2)
     log to console       ${value}
     should be Equal      ${value}     登录
     log to console      "成功进入处处有码官网"


登录网页--00002
     login    13262849250     test123456
     ${value}     get text    css='.admin-board>div:nth-child(1) .account-name'
     should be true    ${value}    13262849250



检查登录框用户名默认文字----00003
   ${value}    get text     css:img[src*='7f220071.png']+div>div:nth-child(2)
   ${username}     get element       css:[.board>div:nth-child(4)>div:nth-child(1) input]
   ${uservalue}     get text     ${username}
   should be true    ${uservalue}      请输入您的手机号/神手云账号

检查登录框密码默认文字----00004
   ${password}      get element      css=(.board>div:nth-child(4)>div:nth-child(2) input)
   ${uservalue}     get text      ${password}
   should be true    ${uservalue}      请输入您的密码
