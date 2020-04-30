*** Settings ***
Library  API.pylib.API.Api_web
Variables   API/cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，在这里来引入用variables

*** Test Cases ***
获取某个活码的子码展示模式--api000030
     ${getlist}       getcodelist
     ${adminshowtype}    getAdminShowType     ${getlist}[result][0][id]
     run keyword if     ${adminshowtype}[result][adminShowType]==1   or    ${adminshowtype}[result][adminShowType]==0
      ...   log to console    成功获取子码展示模式


修改某个活码的子码展示模式--api000031
     ${getlist}       getcodelist
#     ${childlist}     getChildList       ${getlist}[result][0][id]
     ${adminshowtype}    getAdminShowType     ${getlist}[result][0][id]
     ${setshowtype}   setAdminShowType     ${getlist}[result][0][id]
     should be true    $setshowtype["code"]==200


获取分日数据----api000032
    [Documentation]     获取分日数据
    ${getlist}       getcodelist
    ${getcodecounts}      getAdminCodeCounts     ${getlist}[result][0][id]
    should be true      $getcodecounts["code"]==200
