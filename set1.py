s=set()
n=int(input("enter number number of elements"))
for i in range(n):
    s.add(int(input("enter elemnt")))

s.update({1,3,5,8,9})
print(s)
s.remove(10)#will raise error if the element is not present
s.discard(11)#will not raise error if element is not present 