import numpy as n


a=n.array([])
b=n.array([])


print("Enter array1 (blank to stop)")
while True:
    s=input()
    if s=='':
        break
    a=n.append(a,s)

print("Enter array2 (blank to stop)")
while True:
    s=input()
    if s=='':
        break
    b=n.append(b,s)


check=0
for i in range(len(a)):
    if (len(a) != len(b)):
        print("False")
        check=1
        break
    if(a[i]!=b[i]):
        print("False")
        check=1
        break
if check==0:
    print("True")
