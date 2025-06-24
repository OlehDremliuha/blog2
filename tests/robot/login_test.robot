*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${URL}            http://localhost:8000/login/
${USERNAME}       testuser
${PASSWORD}       testpass123
${SUCCESS_URL}    http://localhost:8000/profile/

*** Test Cases ***
Login With Valid Credentials
    [Documentation]    Перевіряє, що користувач з правильними даними входить і потрапляє на сторінку профілю
    Open Browser       ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text         name=username     ${USERNAME}
    Input Text         name=password     ${PASSWORD}
    Click Button       css=button[type="submit"]
    Wait Until Location Is    ${SUCCESS_URL}    timeout=5s
    Close Browser