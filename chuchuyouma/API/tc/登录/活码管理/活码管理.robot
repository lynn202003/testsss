*** Settings ***
Library  API.pylib.API.Api_web
Variables   API/cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，这在里来引入用variables

*** Test Cases ***
创建一个群聊码----api000011
    [Tags]    冒烟测试
    [Documentation]      创建一个群聊码
    ${beforecodelist}     createAdminCode     -1       0      我在用创建活码，能成功吗11       0       2020-03-29        ${dictdata}
    should be true     $beforecodelist["code"]==200
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    [Teardown]      deletecode    ${beforecodelist}[result][id]




创建一个客服码----api000012
    [Tags]    冒烟测试
    [Documentation]      创建一个客服码
    ${beforecodelist}     createAdminCode    -1      1        我在用创建活码，能成功吗11       1       2020-03-29            ${dictdata}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    [Teardown]      deletecode    ${beforecodelist}[result][id]


修改一个群聊码----api000013
    [Tags]    冒烟测试
    [Documentation]      修改一个群聊码
    ${beforecodelist}     createAdminCode      -1     0    我在用创建活码，能成功吗11       1       2020-03-20            ${dictdata}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    createAdminCode       ${beforecodelist}[result][id]       0       我在用修改活码，能成功吗11        0      2020-03-29            ${dictdata}
    [Teardown]      deletecode    ${beforecodelist}[result][id]

修改一个客服码----api000014
    [Tags]    冒烟测试
    [Documentation]      修改一个客服码
    ${beforecodelist}     createAdminCode      -1     1    我在用创建活码，能成功吗11       1       2020-03-20            ${dictdata}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    createAdminCode       ${beforecodelist}[result][id]       0       我在用修改客服码，能成功吗11        0      2020-03-29            ${dictdata}
    [Teardown]      deletecode    ${beforecodelist}[result][id]

删除一个客服码----api000015
    [Tags]    冒烟测试
    [Documentation]      删除一个客服码
    ${beforecodelist}     createAdminCode    -1      1        我在用创建活码，能成功吗11       1       2020-03-29           ${dictdata}
    ${aftercodelist}      getcodelist
    should be true      $aftercodelist["result"][0]["id"]==$beforecodelist["result"]["id"]
    deletecode    ${beforecodelist}[result][id]