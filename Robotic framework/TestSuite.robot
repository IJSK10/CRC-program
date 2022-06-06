*** Variables ***

@{Cor1}  ${1}  ${0}  ${0}  ${1}  ${0}  ${1}  ${1}  ${0}
@{Cor2}  ${1}  ${0}  ${0}  ${1}  ${0}  ${1}  ${1}  ${1}
@{div}   ${1}  ${0}  ${1}

*** Settings ***
Resource    keywords.resource
Resource    variables.resource
Library    Collections

*** Test Cases ***
Test Case 1
    @{GLOBAL_VAR}  Create List   ${1}  ${0}  ${0}  ${1}  ${0}  ${1}
    @{CODE}=  Find Code   ${GLOBAL_VAR}    ${div}
    Correct  ${CODE}  ${Cor1} 
Test Case 2
    @{GLOBAL_VAR}  Create List   ${1}  ${0}  ${0}  ${1}  ${0}  ${1}
    @{CODE}=  Find Code   ${GLOBAL_VAR}    ${div}
    Correct  ${CODE}  ${Cor2} 
Test case 3
    @{GLOBAL_VAR}  Create List   ${1}  ${0}  ${0}  ${1}  ${0}  ${1}
    @{CODE}=  Fico  ${GLOBAL_VAR}  ${div}
    Corr  ${CODE}  ${Cor1}
Test case 4
    @{GLOBAL_VAR}  Create List   ${1}  ${0}  ${0}  ${1}  ${0}  ${1}
    @{CODE}=  Fico  ${GLOBAL_VAR}  ${div}
    Corr  ${CODE}  ${Cor2}

