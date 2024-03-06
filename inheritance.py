class building:
    def __init__(self,name,floors):
        self.name = name
        self.floors = floors
    def display_info(self):
        return f"{self.name } has {self.floors} floors"

class House(building):
    def __init__(self,name, floors, bedrooms):
        super().__init__(name, floors)
        self.bedrooms = bedrooms
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} it's house with {self.bedrooms} bedrooms"

#instances of the derived class


h = House("nivasam",2,3)
k=House(" homes",2,3)
b =House("Villas",3,5)

print(h.display_info())
print(k.display_info())
print(b.display_info())