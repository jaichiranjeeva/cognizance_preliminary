s=4
for i in range(5):
    for k in range(s):
        print("",end=" ")
    for j in range(i+1):
        print("* ",end="")
    s=s-1
    print()
