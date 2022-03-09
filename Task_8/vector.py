import numpy as n
vector=n.array([])
s=int(input("Enter first number:"))
e=int(input("Enter second number:"))
for i in range(s,e):
    vector=n.append(vector,float(i))
    for j in range(5):
        vector=n.append(vector,0.0)
vector=n.append(vector,e)
print(vector)

    
