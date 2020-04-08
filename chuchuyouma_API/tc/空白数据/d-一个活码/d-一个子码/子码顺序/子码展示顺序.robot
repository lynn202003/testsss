*** Settings ***
Library  pylib.API

*** Test Cases ***
获取某个活码的子码展示模式--000010
     ${getlist}       getcodelist
     ${childlist}     getChildList       ${getlist}[result][id]
     ${adminshowtype}    getAdminShowType     ${childlist}[result][id]
     run keyword if     ${adminshowtype}[result][adminShowType]==1   or    ${adminshowtype}[result][adminShowType]==0
      ...   log to console    成功获取子码展示模式


修改某个活码的子码展示模式--000011
     ${getlist}       getcodelist
     ${childlist}     getChildList       ${getlist}[result][id]
     ${adminshowtype}    getAdminShowType     ${childlist}[result][id]

获取分日数据----api00009
    [Documentation]     获取分日数据
    ${getcodecounts}      getAdminCodeCounts
    should be true      $getcodecounts["code"]==200
