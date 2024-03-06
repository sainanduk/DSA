class Employee:
  def __init__(self):
    self.id=int(input("enter id "))
    self.name=input("enter name")
    self.salary=int(input("enter salary"))
    self.exp=int(input("enter experience"))
  def increment(self):
    if self.salary>25000 and self.exp>2:
      self.salary=self.salary+((self.salary)*10)//100
      return self.salary
    else:
      return self.salary
e1=Employee()
print(e1.increment())