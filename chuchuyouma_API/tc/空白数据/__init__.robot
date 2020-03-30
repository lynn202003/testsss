*** Settings ***
Library  pylib.API
Suite Setup      Run Keywords     login   |    13262849250  |    test123456
                   ...  AND    delete_all_code
