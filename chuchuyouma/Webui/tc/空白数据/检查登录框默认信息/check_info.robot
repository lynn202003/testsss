*** Settings ***
Variables  Webui/pylib/getdriver.py
Variables  Webui/cfg.py
Library  SeleniumLibrary
Library  Collections
Library  Webui.pylib.base_page.basepage       ${getwebdriver}
Library  Webui.pageobject.logopage.login      ${getwebdriver}
Test Setup    Webui.pageobject.logopage.login.openbrow      ${url_path}
#Suite Teardown     closebrow
*** Test Cases ***
检查登录框用户名默认文字----ui300001
    click_denglu
    sleep     2
    click_ringlogin
    sleep     2
    ${uservalue}     get_username
    should be true    $uservalue      请输入您的手机号/神手云账号

检查登录框密码默认文字----ui00002
    click_denglu
    sleep     2
    click_ringlogin
    sleep     2
    ${passwordvalue}     get_password
    should be true    $passwordvalue      请输入您的密码


