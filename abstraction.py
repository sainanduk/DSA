from abc import ABC,abstractmethod
class television(ABC):
  def __init__(self ,brand):
    self.brand = brand
    self.powered_on = False
    
    
    #@abstractmethod
  def turn_on(self):
    pass
    
    #@abstractmethod
  def turn__off(self):
    pass
  
  def chanage_channel(self,channel):
    pass
  
class smarttv(television):
  def turn_on(self):
    self.powered_on = True
    print(f"{self.brand} smarttv is on.")  
    
    
  def turn_off(self):
    self.powered_on = False
    print(f"{self.brand} smarttv is off.")  
    
    
  def chanage_channel(self,channel):
    if self.powered_on:
      print(f"{self.brand} smarttv is now on channel {channel}.")  
    else:
      print("cannot change channel.tv is off")  
      
      
    self.powered_on = True
    print(f"{self.brand} smarttv is on.")
tv=smarttv(brand="Apple")
tv.turn_on()
tv.chanage_channel(25)
tv.turn__off()