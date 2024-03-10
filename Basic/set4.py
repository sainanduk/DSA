n=input("enter string").split()
flag=True
for i in n:
    if len(i)!=len(set(i)):
        flag=False
        break
print(flag)