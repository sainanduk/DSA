l1 =input().split()
l2=[]
# 5 4 31 2 1
for i in range(0,len(l1)):
    count=0
    for j in range (i+1,len(l1)):
        if len(l1[i])==len(l1[j]):
            count+=1
    l2.append(count)
print(l2)