*** Settings ***
Library  pylib.API.Api_web
Variables   cfg.py   #因此用例中要多次用到固定的字典，故将设为变量放在配置文件中，这在里来引入用variables
Test Setup     run keywords    login    13774351025   test123456      AND    delete_all_code   AND
                 ...    createAdminCode   -1    0    我在用robot创建活码       0      2020-03-31     ${dictdata}    AND
                 ...    suitesetup     -1     0       ji1251266     0       yttt66     http://qiniu.shenshoukeji.net/0326113958timg.jpg      http://qiniu.shenshoukeji.net/0305163619group-default.png       28
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
