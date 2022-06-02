# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("CRC program")

A=input("Enter the code:")
C=A
B=input("Enter the divisor:")

for i in range(0,len(B)-1):
    A=A+'0'

L=[]
for i in A:
    L=L+[i]
Z=[]
for i in B:
    Z=Z+[i]

print(len(L))
for i in range(0,len(L)-len(B)+1):
    if L[i]=='1':
        for j in range(0,len(B)):
            if ((L[i+j]=='1') and (Z[j]=='1')):
                L[i+j]='0'
            elif ((L[i+j]=='1') and (Z[j]=='0')):
                L[i+j]='1'
            elif ((L[i+j]=='0') and (Z[j]=='1')):
                L[i+j]='1'
            elif ((L[i+j]=='0') and (Z[j]=='0')):
                L[i+j]='0'
for i in range(len(L)-len(B),len(L)):
    C=C+L[i]
print("The output code is "+C)