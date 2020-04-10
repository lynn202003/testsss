*** Settings ***
Library  pylib.API.Api_web

*** Test Cases ***
支付-api000040
     [Tags]    冒烟测试
     [Documentation]    支付
     ${user}   login  13774351025     test123456
     should be true   $user["result"]["phone"]=="13774351025"
#     判断用户等级
