string1 = input("enter string ")
string2=[]
for i in string1:
    if i!="#":
        string2.append(i)
    elif len(string2)>0:
        string2.pop()
print("".join(string2))
