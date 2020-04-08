*** Settings ***
Library  pylib.API


*** Test Cases ***
增加一个子码-api00005
    [Tags]      冒烟测试
    [Documentation]    新建子码
    ${codelist}    getcodelist
    ${childlist}   getChildList
    addChildCode    ${codelist}[result][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    ${afterchildlist}     getChildList
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    [Teardown]    delete_childcode    ${codelist}[result][id]        ${afterchildlist}[result][0][id]

修改一个子码-api00006
    [Tags]      冒烟测试
    [Documentation]    修改子码
    ${codelist}    getcodelist
    ${childlist}   getChildList
    addChildCode    ${codelist}[result][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    ${afterchildlist}     getChildList
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    ${childcode}    addChildCode      ${codelist}[result][id]       ${afterchildlist}[result][0][id]        0       ji1251267     0       yttt67     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       29
    should be true       $childcode["code"]==200
    [Teardown]    delete_childcode    ${codelist}[result][id]        ${afterchildlist}[result][0][id]

删除一个子码-api00007
   [Tags]     冒烟测试
   [Documentation]      删除一个子码
    ${codelist}    getcodelist
    ${childlist}   getChildList
    addChildCode    ${codelist}[result][id]     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
    ${afterchildlist}     getChildList
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji1251266"
    delete_childcode       ${codelist}[result][id]        ${afterchildlist}[result][0][id]




