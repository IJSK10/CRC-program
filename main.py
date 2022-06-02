
print("CRC program")

print("1.Sender")
print("2.Reciever")
c=int(input("Enter the choice"))
if (c==1):


    A = input("Enter the code:")
    C = A
    B = input("Enter the divisor:")

    for i in range(0, len(B) - 1):
        A = A + '0'

    L = []
    for i in A:
        L = L + [i]
    Z = []
    for i in B:
        Z = Z + [i]

    for i in range(0, len(L) - len(B)+1):
        if L[i] == '1':
            for j in range(0, len(B)):
                if ((L[i + j] == '1') and (Z[j] == '1')):
                    L[i + j] = '0'
                elif ((L[i + j] == '1') and (Z[j] == '0')):
                    L[i + j] = '1'
                elif ((L[i + j] == '0') and (Z[j] == '1')):
                    L[i + j] = '1'
                elif ((L[i + j] == '0') and (Z[j] == '0')):
                    L[i + j] = '0'
    for i in range(len(L) - len(B)+1, len(L)):
        C = C + L[i]
    print("The output code is " + C)
elif(c==2):
    A = input("Enter the code:")
    C = A
    B = input("Enter the divisor:")
    L = []
    for i in A:
        L = L + [i]
    Z = []
    for i in B:
        Z = Z + [i]
    for i in range(0, len(L) - len(B) + 1):
        if L[i] == '1':
            for j in range(0, len(B)):
                if ((L[i + j] == '1') and (Z[j] == '1')):
                    L[i + j] = '0'
                elif ((L[i + j] == '1') and (Z[j] == '0')):
                    L[i + j] = '1'
                elif ((L[i + j] == '0') and (Z[j] == '1')):
                    L[i + j] = '1'
                elif ((L[i + j] == '0') and (Z[j] == '0')):
                    L[i + j] = '0'
    m=0
    for i in range(len(L) - len(B), len(L)):
        print(L[i])
        if L[i]=='1':
            m=1
    if(m==1):
        print("There is a error")
    else:
        print("There is no error")
