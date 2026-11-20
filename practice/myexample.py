from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.durability = 100

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def wear(self, amount):
        pass

    def get_value(self):  
        return self.value

class Weapon(Item):
    def __init__(self, name, value, damage):
        super().__init__(name, value)
        self.damage = damage

    def get_name(self):
        return f"{self.name} ({'Broken Weapon' if self.durability < 50 else 'Fine Weapon'})"


    def wear(self, amount):
        self.durability -= amount
        if self.durability < 0:
            self.durability = 0
    
class Armor(Item):
    def __init__(self, name, value, defense):
        super().__init__(name, value)
        self.defense = defense

    def get_name(self):
        return f"{self.name} ({'Worn Armor' if self.durability < 20 else 'Pristine Armor'})"

    def wear(self, amount):
        self.durability -= amount
        if self.durability < 0:
            self.durability = 0     

a = Armor("Steel Armor", 150, 50)
w = Weapon("Iron Sword", 100, 25)

print(a.get_name())
a.wear(85)
print(a.get_name())   
print(w.get_name())
w.wear(60)
print(w.get_name())

   
  