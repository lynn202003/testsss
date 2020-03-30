*** Variables ***
&{dict}    noRepeat=False    administrator=False      safeTip=True     customerService=""

*** Settings ***
Library  pylib.API
Suite Setup     createAdminCode      0    我在用robot创建活码       0      2020-03-31     &{dict}




