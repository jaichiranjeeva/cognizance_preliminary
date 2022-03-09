import numpy as n

a=n.array([])
b=n.array([])

print("Enter Array1 elements(Enter blank to stop):")
while True:
    s=input()
    if s=='':
        break
    a=n.append(a,int(s))

print("Enter Array2 elements(Enter blank to stop):")
while True:
    s=input()
    if s=='':
        break
    b=n.append(b,int(s))
x=0
for i in a:
    for j in b:
        if(i==j):
            print(x,end=",")
    x=x+1
            
