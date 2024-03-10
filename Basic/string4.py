s1="the sun rises in the east"
##eht snu sesir ni eht stea
l1=s1.split()
l2=[]
vov=["a","e","i","o","u"]
def vovels(n):
    vo=""
    for i in n:
        if i in vov:
            vo+=i
    return vo
def conso(n):
    con=""
    for i in n:
        if i not in vov:
            con+=i
    return con  
for i,a in enumerate(l1):
    if (i+1)%2==0:
        l2.append(conso(a)+vovels(a))
    else:
        l2.append(a[::-1])
print(" ".join(l2))

