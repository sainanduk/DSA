from linkedlist import *
def mergesortedLL():
    obj1=LL()
    obj2=LL()
    n1=int(input("enter number of nodes in LL1"))
    while n1>0:
        obj1.insertnode()
        n1-=1
    n2=int(input("enter number of nodes in LL2"))
    while n2>0:
        obj2.insertnode()
        n2-=1
    if  n1!= n2:
        return "NO"
    temp1=obj1.head
    temp2=obj2.head
    while temp1:
        if temp1.data!=temp2.data:
            return "NO"
        temp1=temp1.next
        temp2=temp2.next
    return 'YES'
print(mergesortedLL())