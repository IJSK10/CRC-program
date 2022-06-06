*** Settings ***
Library    PythonKeywords

*** Keywords ***
Say Hello World
    Log To Console    Hello World

Call A Library Keyword
    Lib Keyword    Hello Robot
Find Code
    [Arguments]    ${GLOBAL_VAR1}  ${div}
    @{FINALCODE} =  Copy list   ${GLOBAL_VAR1}
    ${B}=  Get Length     ${div}
    ${N}=  Get Length    ${GLOBAL_VAR1}
    ${Z}=  Evaluate    ${N} + 0  


    FOR   ${C}   IN RANGE  ${B}-1
        Append To List    ${GLOBAL_VAR1}   ${0}
    END
    ${L}=  Get Length    ${GLOBAL_VAR1}
    FOR    ${i}  IN RANGE  ${Z}
        IF    ${GLOBAL_VAR1}[${i}] > 0
            FOR    ${j}  IN RANGE  ${B}
                ${Y}=  Evaluate    ${i} + ${j}
                IF    ${GLOBAL_VAR1}[${Y}] > 0 and ${div}[${j}] > 0
                    Set List Value  ${GLOBAL_VAR1}  ${Y}  ${0}
                ELSE IF    ${GLOBAL_VAR1}[${Y}] > 0 and ${div}[${j}] < 1
                    Set List Value  ${GLOBAL_VAR1}  ${Y}  ${1}
                ELSE IF    ${GLOBAL_VAR1}[${Y}] < 1 and ${div}[${j}] > 0
                    Set List Value  ${GLOBAL_VAR1}  ${Y}  ${1}
                ELSE IF    ${GLOBAL_VAR1}[${Y}] < 1 and ${div}[${j}] < 1
                    Set List Value  ${GLOBAL_VAR1}  ${Y}  ${0}
                END
            END
        END
    END

    ${P}=  Evaluate    ${L} - ${B} + 1
    FOR    ${i}  IN RANGE  ${P}  ${L}
        Log To Console    ${GLOBAL_VAR1}[${i}]
        Append To List    ${FINALCODE}   ${GLOBAL_VAR1}[${i}]
    END
    [Return]   @{FINALCODE}  

Correct 
    [Arguments]    ${CODE1}  ${CODE2}
    Should Be Equal    ${CODE1}    ${CODE2}
