shop={}
while True:
  choice=int(input("enter choice 1.add\n 2.exit"))
  
  if choice==1:
    name=input("enter product name")
    price=int(input("enter price"))
    brand=input("brand")
    shop.update({name:{brand,price}})
  else:
    break
res=0 
for key,val in shop.items():
  brand,price=list(val)
  res+=int(price)
print(f"total price:{res}")