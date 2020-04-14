*** Settings ***
Library  pylib.API.Api_web

*** Test Cases ***
支付-api000040
     [Tags]    冒烟测试
     [Documentation]    支付
     ${user}   login  13774351025     test123456
     should be true   $user["result"]["phone"]=="13774351025"
     ${idinfo}     Calculation     4
     ${getpay}     GetPayOrder    1        &{idinfo}[result][money]       1        4
     ${payback}    PayBack     1     &{getpay}[result][orderNo]
     should be true      $payback["code"]==200
