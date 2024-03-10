s1="abcde"
s2="bcdef"
if len(s1)>=len(s2):
    n=s1
    s=s2+" "*(len(s1)-len(s2))
else:
    n=s2
    s=s1+" "*(len(s2)-len(s1))
count=0
for i,a in enumerate(n):
    if a!=s[i]:
        count+=1
print(count)