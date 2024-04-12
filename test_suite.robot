*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open google.com
    [Documentation]    Test case to open Open google.com
    Open Browser				 browser=chrome
    Go To				 url=https://google.com
