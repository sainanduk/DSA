'''def order(str1):
    return "".join(sorted(str1))
s="hello"
print(order(s))'''
'''s1="ooxX"
def XO(s1):
    o=x=0
    flag=False
    for i in s1:
        if i=='o' or i=='O':
            o+=1
        elif i=='x' or i=='X':
            x+=1
    if o==x and o!=0:
        flag=True
    return flag
print(XO(s1))'''
def XO():
    n=input("enter string")
    n.lower()
    x=n.count('x')
    