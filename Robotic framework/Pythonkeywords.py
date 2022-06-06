def lib_keyword(string):
    print(string)

def fico(L1,L2):
    L3=L1
    for i in range(0, len(L2)):
        L1=L1+[0]
    for i in range(0, len(L1) - len(L2)+1):
        if L1[i] == 1:
            for j in range(0, len(L2)):
                if ((L1[i + j] == 1) and (L2[j] == 1)):
                    L1[i + j] = 0
                elif ((L1[i + j] == 1) and (L2[j] == 0)):
                    L1[i + j] = 1
                elif ((L1[i + j] == 0) and (L2[j] == 1)):
                    L1[i + j] = 1
                elif ((L1[i + j] == 0) and (L2[j] == 0)):
                    L1[i + j] = 0
    for i in range(len(L1) - len(L2)+1, len(L1)):
        L3 = L3 + [L1[i]]
        print(L3)
    return L3

def corr(L1,L2):
    if L1==L2:
        return True
    else:
        return False
