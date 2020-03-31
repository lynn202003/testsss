*** Settings ***
Library  SeleniumLibrary
Library  pylib.newmerchant
Library  BuiltIn
#Library  pylib.merchant.log      13262849250          a123321       http://47.96.83.35:5001
Test Setup      deleteall
Test Teardown         deleteall
*** Variables ***
&{userinfo}      username=13262849250     password=a123321      port=http://47.96.83.35:5001
@{addgoodsinfo}      http://47.96.83.35:5001          娃哈哈     100ml      12      8     20     2    http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg       娃哈哈很好喝     非常喜欢喝娃哈哈

*** Test Cases ***

检查商品是否添加成功-tc00001
     [Documentation]     检查商品
     [Tags]         主流程测试
     [Setup]          deleteall
     [Teardown]         deleteall
     ${tokenid}   login      &{userinfo}[username]     &{userinfo}[password]       &{userinfo}[port]
     addgoods      ${tokenid}        @{addgoodsinfo}[0]        @{addgoodsinfo}[1]     @{addgoodsinfo}[2]       @{addgoodsinfo}[3]      @{addgoodsinfo}[4]     @{addgoodsinfo}[5]      @{addgoodsinfo}[6]     @{addgoodsinfo}[7]        @{addgoodsinfo}[8]      @{addgoodsinfo}[9]
     ${goodslist}     listgoods     ${tokenid}          http://47.96.83.35:5001
     :FOR   ${goods}    IN     @{goodslist}
    #    \     log to console      ${goods['GoodsName']}
     #   \     log to console      &{goods}[GoodsName]
      \     should be equal       &{goods}[GoodsName]         娃哈哈
      \     log to console       添加成功


更新商品-tc00002
     ${tokenid}   login      13262849250     a123321      http://47.96.83.35:5001
     addgoods      ${tokenid}        http://47.96.83.35:5001          娃哈哈     100ml      12      8     20     2    http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg       娃哈哈很好喝     非常喜欢喝娃哈哈
     ${goodslist}     listgoods     ${tokenid}          http://47.96.83.35:5001
     exit for loop if     ${goodslist}==[]
     updategoods       ${tokenid}    http://47.96.83.35:5001       ${goodslist[0]["GoodsId"]}    娃哈哈更新     100ml      12      8     20     2    http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg       娃哈哈很好喝更新     非常喜欢喝娃哈哈
     ${goodslist}     listgoods     ${tokenid}          http://47.96.83.35:5001
     :FOR   ${goods}    IN     @{goodslist}
      \     should be equal       &{goods}[GoodsName]         娃哈哈更新
      \     log to console       添加成功

删除商品-tc00003
       ${tokenid}   login      13262849250     a123321      http://47.96.83.35:5001
       addgoods      ${tokenid}        http://47.96.83.35:5001          娃哈哈     100ml      12      8     20     2    http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg       娃哈哈很好喝     非常喜欢喝娃哈哈
       ${goodslist}     listgoods     ${tokenid}          http://47.96.83.35:5001
       checkdelete      ${tokenid}     ${goodslist}        ${goodsid}
       ${goodsid}     ${goodslist}     listgoods     ${tokenid}          http://47.96.83.35:5001
        exit for loop if          ${goodslist}==[]




#检查左页面是否正确
#       ${ret}       pagechecked
#       ${str}=      set variable       主页|商户管理|优惠券管理|活动管理|小区申请|广告管理|招聘管理|日志管理
#      should be equal    ${ret}       ${str}
#       log to console    ${ret}





