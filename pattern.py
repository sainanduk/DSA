n=15
for i in range(1,n+1):
    if i==1 or i==n:
        print("# "*n)
    else:
        print("# "+" "*(n*2-4)+"#")
