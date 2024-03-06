'''dic={}
n=int(input("enter no of elements"))
for i in range(n):
    rollno=int(input("enter roll no"))
    name=input("enter name of the student")
    dic.update({rollno:name})
print(dic)'''
'''n=int(input("enter no of students"))
student={}
for i in range(n):
  rollno=int(input("enter roll no"))
  marks=list(map(int,input("enter marks of 3 subs").split()) )
  student.update({rollno:sum(marks)})
topper=max(zip(student.values(),student.keys()))
print("topper is ",topper[1],"marks are ",topper[0])'''
'''n=int(input("enter number"))
v=input("enter vovel")
l2=[]
l3=[]
dic={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
while n>0:
    rem=n%10
    n=n//10
    l2.append(rem)
l2.reverse()
for i in l2:
    val=dic.get(i)
    if v in val:
        continue
    else:
        print(dic.get(i),end=" ")
'''
'''n=input("enter number")
v=input("enter vovel")
dic={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for i in n:
    if v not in dic[int(i)]:
        print(i,end="")'''
'''n=input("enter binary")
count=0
'''
'''for i in n: 
    if i=="0":
        count+=1
    elif i=='1':
        maxcount=count
        count=0
print(maxcount)'''
#print(len(max(input("enter number").split("1"))))
'''dic={}
n=input("enter string")
for i in n:
    dic.update({i:dic.setdefault(i,0)+1})
print(dic)
'''
'''n=int(input("enter number"))
temp=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==temp:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    temp-=1
    print()'''
n = int(input())
l1 = [*range(1, n + 1)]
print(l1)
l = 0
r = len(l1) - 1
temp = l1[r] - 1

while l <= r:
    if l == r:
        print((l) * "  ", l1[l])
    else:
        print((l) * " ", l1[l], " " * (temp - l), l1[r])
    temp -= 1
    l += 1
    r -= 1

mid = len(l1) // 2
l = mid
r=mid

while l > 0 and r < len(l1):
    print(" " * l, l1[l], " " * (r - l), l1[r])
    l -= 1
    r += 1