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
        return f"{base_info} it's office with {self.bedrooms} rooms"
class office(House):
    def __init__(self,name,floors,bedrooms,cabins):
        super().__init__(name,floors,bedrooms)
        self.cabins=cabins
    def display_info(self):
        base_info2=super().display_info()
        return f"{base_info2} its  floor {self.cabins} cabins"
h=office("vishwak",5,6,20)
print(h.display_info())
