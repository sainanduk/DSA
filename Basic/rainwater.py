arr=list(map(int,input("enter").split()))
l=0
r=len(arr)-1
lmax=rmax=0
left=0
right=0
ans=0
while l<r:
    if arr[l]>=lmax:
        lmax=arr[l]
        left=l
    if arr[r]>=rmax:
        rmax=arr[r]
        right=r
    l+=1
    r-=1
minnum=min(lmax,rmax)
while left<right:
    ans+= (minnum-arr[left])
    left+=1
print(ans)