*** Settings ***
Library  pylib.API.Api_web
Variables   cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，这在里来引入用variables
#Test Setup     run keywords    login    13774351025   test123456      AND    delete_all_code   AND
#                 ...    createAdminCode   -1    0    我在用robot创建活码       0      2020-03-31     ${dictdata}

#Suite Setup     createAdminCode   -1    0    我在用robot创建活码       0      2020-03-31     &{dict}




