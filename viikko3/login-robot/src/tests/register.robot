*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  moikka  moikka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle12345
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  mo  moikka12345
    Output Should Contain  Username too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  moikka123  moikka12345
    Output Should Contain  Username can only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  moikka  moi1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  moikka  moimoimoi
    Output Should Contain  Password can't only contain letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
    
