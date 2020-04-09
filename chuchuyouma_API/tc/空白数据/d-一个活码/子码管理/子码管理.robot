*** Settings ***
Library  pylib.API.Api_web
Variables   cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，这在里来引入用variables
Test Setup     run keywords    login    13774351025   test123456      AND    delete_all_code   AND
                 ...    createAdminCode   -1    0    我在用robot创建活码       0      2020-03-31     ${dictdata}


*** Test Cases ***
增加一个子码-api00020
    [Tags]      冒烟测试
    [Documentation]    新建子码
    ${codelist}    getcodelist
    ${addchild}    addChildCode    ${codelist}[result][0][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    should be true    $addchild["code"]==200
    ${afterchildlist}     getChildList     ${codelist}[result][0][id]
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    [Teardown]    delete_childcode    ${codelist}[result][0][id]        ${afterchildlist}[result][0][id]

修改一个子码-api00021
    [Tags]      冒烟测试
    [Documentation]    修改子码
    ${codelist}    getcodelist
    ${addchild}   addChildCode    ${codelist}[result][0][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    should be true    $addchild["code"]==200
    ${afterchildlist}     getChildList     ${codelist}[result][0][id]
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    ${childcode}    addChildCode      ${codelist}[result][0][id]       ${afterchildlist}[result][0][id]        0       ji1251267     0       yttt67     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       29
    should be true       $childcode["code"]==200
    [Teardown]    delete_childcode    ${codelist}[result][0][id]        ${afterchildlist}[result][0][id]

删除一个子码-api00022
   [Tags]     冒烟测试
   [Documentation]      删除一个子码
    ${codelist}    getcodelist
    ${addchild}   addChildCode    ${codelist}[result][0][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    should be true    $addchild["code"]==200
    ${afterchildlist}     getChildList     ${codelist}[result][0][id]
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    delete_childcode       ${codelist}[result][0][id]        ${afterchildlist}[result][0][id]




