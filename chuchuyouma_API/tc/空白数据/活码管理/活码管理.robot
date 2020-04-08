*** Settings ***
Library  pylib.API.Api_web
Test Setup     run keywords    login    13774351025   test123456      AND    delete_all_code

*** Variables ***
&{dict}           noRepeat=False    administrator=False      safeTip=True     customerService=""

# Create Dictionary

*** Test Cases ***
创建一个群聊码----api000011
    [Tags]    冒烟测试
    [Documentation]      创建一个群聊码
    ${beforecodelist}     createAdminCode     -1       0         我在用创建活码，能成功吗11       0       2020-03-29        ${dict}
    should be true     $beforecodelist["code"]==200
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    [Teardown]      deletecode    ${beforecodelist}[result][id]




创建一个客服码----api000012
    [Tags]    冒烟测试
    [Documentation]      创建一个客服码
    ${beforecodelist}     createAdminCode    -1      1        我在用创建活码，能成功吗11       1       2020-03-29            &{dict}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    [Teardown]      deletecode    ${beforecodelist}[result][id]


修改一个群聊码----api000013
    [Tags]    冒烟测试
    [Documentation]      修改一个群聊码
    ${beforecodelist}     createAdminCode      -1     0    我在用创建活码，能成功吗11       1       2020-03-20            &{dict}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    createAdminCode       ${beforecodelist}[result][id]       0       我在用修改活码，能成功吗11        0      2020-03-29            &{dict}
    [Teardown]      deletecode    ${beforecodelist}[result][id]

修改一个客服码----api000014
    [Tags]    冒烟测试
    [Documentation]      修改一个客服码
    ${beforecodelist}     createAdminCode      -1     1    我在用创建活码，能成功吗11       1       2020-03-20            &{dict}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    createAdminCode       ${beforecodelist}[result][id]       0       我在用修改客服码，能成功吗11        0      2020-03-29            &{dict}
    [Teardown]      deletecode    ${beforecodelist}[result][id]

删除一个客服码----api000015
    [Tags]    冒烟测试
    [Documentation]      删除一个客服码
    ${beforecodelist}     createAdminCode    -1      1        我在用创建活码，能成功吗11       1       2020-03-29            &{dict}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    deletecode    ${beforecodelist}[result][id]