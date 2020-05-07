*** Settings ***
Library  API.pylib.API.Api_web
Variables   API/cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，这在里来引入用variables
Suite Setup      run keywords    createAdminCode   -1    0    我在用robot创建活码       0      2020-04-29      ${dictdata}      AND       suite_delallchild




