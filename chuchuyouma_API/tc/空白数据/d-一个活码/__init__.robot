*** Variables ***
&{dict}     Create Dictionary       noRepeat=False    administrator=False      safeTip=True     customerService=""

*** Settings ***
Library  pylib.API
Suite Setup     createAdminCode      0    我在用robot创建活码       0      2020-03-31     &{dict}
Library  pylib.API
Suite Setup      Run Keywords     login   |    13262849250  |    test123456
                   ...  AND    delete_all_code    AND   createAdminCode |0     |    "我在用创建活码，能成功吗11"    |       0     |      "2020-03-29"     |      &{dict}



