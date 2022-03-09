import pandas as p
import numpy as n
xx=n.array([])
print("Enter series elements(0 to stop):")
while True:
    s=input()
    if s=='0':
        break
    xx=n.append(xx,s)    
array = p.Series(xx)
for i in array:
    print(str.title(i),end=" ")

'''Or just
    
array=p.series(['aa','bb'...]) 
for i in array:
    print(str.title(i),end=" ")

for pre-defined Series elements'''

