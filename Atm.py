class ATM:
  def __init__(self):
    self.balance=10000
    self.mini_statement=[]
  def Withdraw(self):
    amount =int(input("\namount should be Multiples of 100"))
    if(amount%100==0):
      flag=True
    else:
      flag=False
    if flag:
      if amount>10000:
        otp=input("\nenter otp")
        if len(otp)!=4:
          print("\ninvalid OTP")
        else:
          if self.balance<=amount:
            self.balance-=amount
            self.mini_statement.append(-amount)
          else:
            print("\ninsufficient balance")
      else:
        if self.balance>=amount:
          self.balance-=amount
          self.mini_statement.append(-amount)
        else:
          print("\ninsufficient amount")
    else:
      print("\nenter valid amount")
  def deposite(self):
    
    denomination=int(input("\n100/200/500"))
    deposite_amount=int(input("\nenter amount"))
    if deposite_amount//denomination >200:
      print("\ninvalid amount")
    else:
      self.balance+=deposite_amount
      self.mini_statement.append(deposite_amount)
      print("\ninserted")
  def ministatement(self):
    l=len(self.mini_statement)
    if l>5:
        s=l-5
        print(self.mini_statement[s:])
    else:
      print(self.mini_statement)
obj=ATM()
while True:
  choice=int(input("\nenter choice \n 1.Withdraw \n 2.deposite \n 3.ministatement\n 4.exit"))
  if choice ==1:
    obj.Withdraw()
  elif choice==2:
    obj.deposite()
  elif choice==3:
    obj.ministatement()
  elif choice==4:
    print("\nexiting")
    break
  else:
    print("\ninvalid input")
    break
  

  
        