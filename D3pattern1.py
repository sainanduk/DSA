n = int(input("enter"))
for i in range(1,n*n+1):
   if i%n==0:
      print(i,"\n")
   else:
      print(i,end="*")