rec=[]

#Appending values into the list
#rec.append([101,'Ramesh',99])
#rec.append([102,'Suresh',89])
#rec.append([103,'Mukesh',79])
#rec.append([104,'Rajesh',69])

def check():
    choice=input(("Do you want to add one more record?(y/n)"))
    return choice

print("Enter the records seperated by spaces:")
s=input()
rec.append(s.split())
while True:
    choice=check()
    if choice=='y' or choice=='Y':
        s=input()
        rec.append(s.split())
    elif choice=='n' or choice=='N':
        break
    else:
        print("Invalid option")
#Printing the Records Available in the list
print("Records in the list:")

for i in range(len(rec)):
    for j in range(len(rec[i])):
        print(rec[i][j],end="\t")
    print()

print("\nSecond record in the list:")
#Printing the Second Record from the list
#Alternative: 'print(rec[1])'

for j in range(len(rec[1])):
    print(rec[1][j],end="\t")


