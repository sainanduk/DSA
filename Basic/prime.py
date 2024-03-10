####  prime numbers
'''n =int(input(" enter num"))
for i in range(2,n+1):
  count=0
  for j in range(2,i+1):
    if i%j==0:
      count+=1
  if(count<=1):
    print(i)'''
## prime  number
n =int(input("enter"))
l1=[]
for i in range(2,n+1):
    if i==2 or i==3 or i==5 or i==7:
        l1.append(i)
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
        continue
    else:
        l1.append(i)
l2=[]
count=-1
for i in l1:
    num1=n-i
    if num1 in l1:
        if num1 and i not in l2:
            print(num1,"+",i,"=",n)
            l2.append(num1)
            l2.append(i)
            count+=1
if count ==-1:
    print(count)
print("numofWays",count+1)
