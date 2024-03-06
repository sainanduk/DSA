# Nodes address
class node:
  def __init__(self,num=0):
    self.data = num
    self.next = None
# Operations for the nodes
class LL:
  def __init__(self):
    self.head = None
    self.temp = None
    self.__count = 0
  def insertnode(self,num=0):
    newnode = node()
    newnode.data = int(input("Enter the new node value: "))
    if self.head == None:
      # List is empty
      self.head = newnode
      self.temp = newnode
      self.__count += 1
    else:
      # list is present(not empty)
      self.temp = self.head
      while(self.temp.next != None): #last node
        self.temp = self.temp.next
      self.temp.next = newnode
      self.__count += 1
  def printList(self):
    print("List is: ")
    self.temp = self.head
    while(self.temp != None):
      print(self.temp.data,end="->")
      
      self.temp = self.temp.next
    print("None\n")
  def lenghthList(self):
    print("length of LL is : " ,self.__count)
