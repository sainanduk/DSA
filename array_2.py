l1=[i for i in range(1,101) if i%2==0]
l2=[j for j in range(1,100) if j%2!=0]
l3=l1+l2
l4=["even"if i%2==0 else "odd" for i in l3  ]
#print(l4)
#print([i*5 if i%2==0 else i*3 for i in l3])
greet=lambda:"hello"
print(greet())
greet=lambda:"hi"
print(greet())
#greet =lambda str1,str2: str1.upper(); str2.lower()
#print(greet("hello world","hi"))
cube= lambda x,y:x*y
'''for i in range(1,10):
    print(cube(i))'''
print(list(map(lambda x,y:x+y,l1,l2)))
str3="aBcDEfghIJkl"
def convert(x):
    if x.isupper():
        return  x.lower()
    else:
       return x.upper()  
s="".join(map(convert,str3))
print(s)
cn=lambda x: x.upper() if x.islower() else x.lower()
s1="".join(map(cn,str3))
print(s1)