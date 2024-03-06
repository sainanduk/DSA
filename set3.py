'''n=list(map(int,input().split()))
array={input("enter num n").split()}
a=set(map(int,input("enter num a ").split()))
b=set(map(int,input("enter num b ").split()))'''

array={2,3,4,1,2}
a={2,3,1}
b={5,4,6}
print((len(array.intersection(a))-(len(array.intersection(b)))))
