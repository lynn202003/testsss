*** Settings ***
Library  pylib.API


*** Test Cases ***
新建子码-api00005
    [Tags]      冒烟测试
    [Documentation]    新建子码
    ${codelist}    getcodelist
    ${childlist}   getChildList
    addChildCode    ${codelist}[result][id]     -1     0       ji12512     0       yttt     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       23
    ${afterchildlist}     getChildList
    should be true    $afterchildlist["result"][0]["childTitle"]=="ji12512"
    [Teardown]    delete_childcode    ${codelist}[result][id]        ${afterchildlist}[result][0][id]
