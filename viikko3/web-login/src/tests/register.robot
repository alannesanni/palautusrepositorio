*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  oikea
    Set Password  oikea123
    Set Passwordconfirmation  oikea123
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  ly
    Set Password  lyhyt123
    Set Passwordconfirmation  lyhyt123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  oikeaa
    Set Password  oikeaoikea
    Set Passwordconfirmation  oikeaoikea
    Submit Credentials
    Register Should Fail With Message  Password can't only contain letters


Register With Nonmatching Password And Password Confirmation
    Set Username  oikeaaa
    Set Password  oikea1234
    Set Passwordconfirmation  oikeaoikea123
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Set Username  oik
    Set Password  oik12345
    Set Passwordconfirmation  oik12345
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  oik
    Set Password  oik12345
    Submit Credentials Login
    Login Should Succeed
    

Login After Failed Registration
    Set Username  vaara
    Set Password  vaara12345
    Set Passwordconfirmation  vaara1
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match
    Go To Login Page
    Set Username  vaara
    Set Password  vaara12345
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register 

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Passwordconfirmation
    [Arguments]  ${password_conf}
    Input Password  password_confirmation  ${password_conf}

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials Login
    Click Button  Login
