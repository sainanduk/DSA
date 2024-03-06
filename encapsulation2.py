class salary:
    def __init__(self):
        self.__id=None
        self.__name=None
        self.__salary=None
        self.__expe=None
    def setter(self):
       self.__id=int(input("enter id"))
       self.__name=input("enter name")
       self.__salary=int(input("enter salry"))
       self.__expe=int(input("enter expe"))
    def getsalary(self):
       return self.__salary
    def getexp(self):
       return self.__expe
    def increment(self):
        self.setter()
        if self.getsalary()>25000 and self.getexp()>2:
            incrementsalary=self.getsalary()+((self.getsalary())*10//100)
            return incrementsalary
        else:
            return self.getsalary()
obj = salary()
print(obj.increment())