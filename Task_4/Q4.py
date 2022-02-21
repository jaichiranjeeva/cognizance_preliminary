n=int(input("Number:"))
c=n
reversed=0
while c>0:
    temp=int(c%10)
    reversed=reversed*10+temp
    c=int(c/10)
if reversed==n:
    print("true")
else:
    print("false")
