*** Settings ***
Library  pylib.API.Api_web
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


创建活码-api00004
    [Tags]    冒烟测试
    [Documentation]     创建活码
    ${dict}    create dictionary      noRepeat=False    administrator=False      safeTip=True       customerService= ""
    ${createcode}    createAdminCode    -1     0    我在用robot创建活码，能成功吗?        0          2020-03-31         ${dict}
    should be true     $createcode["code"]==200
    ${codelist}    getcodelist
    ${relt}   evaluate   $codelist["result"][0]
    should be true   $relt["id"]==$createcode["result"]["id"]
    [Teardown]    deletecode      ${createcode}[result][id]


