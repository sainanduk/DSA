#Entry control loops
#while loop :
a= 10
while(a>1):
    print(a)
    if a==9:
        a=1
    a-=1
print("_____________")
#while with else:
b=10
while b>5:
    print(b)
    b-=1
else:
    print("b=",b)
print("***************")

#while using break:
c=10
while c>0:
    if c==5:
        break
    print(" c" ,c)
    c-=1
else:
    print("c is breaked")
print('----------------')

#Even numbers from 8 to 100
n=8
while(n<=100):
    if n%2 ==0:
        print(n)
    n+=1