*** Settings ***
Library  SeleniumLibrary
Variables      Webui/pylib/getdriver.py
Variables  Webui/cfg.py
Library  Webui.pylib.base_page.basepage      ${getwebdriver}
Library  Webui.pageobject.main_process
Suite Setup   Webui.pageobject.main_process.logincusess    ${user_name}      ${pass_word}     ${url_path}      ${getwebdriver}
#Suite Teardown     Webui.pylib.base_page.basepage.closebrow