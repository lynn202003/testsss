*** Settings ***
Library  API.pylib.API.Api_web
*** Test Cases ***
正确的手机号和密码-api00001
     [Tags]    冒烟测试
     [Documentation]    输入正常的手机号和密码
     ${user}   login  13774351025     test123456
     should be true   $user["result"]["phone"]=="13774351025"

手机号为中文-api00002
     [Documentation]    手机号为中文
     ${user}   login   中国加油     test123456
 #    should be true   $user["result"]==null
     should be true   $user["code"]==300

手机号为特殊字符-api00003
     [Documentation]    手机号为特殊字符
     ${user}   login   ￥%%…………&     test123456
 #    should be true   $user["result"]==null
     should be true   $user["code"]==300




