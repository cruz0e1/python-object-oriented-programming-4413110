import types

class Dwarf:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a dwarf {self.name}"

    def get_age(self):
        return self.age

d = Dwarf("Gimli")
print(d)

def Born(self):
    self.age = 0

def Age(self, years = 1):
    self.age += years
    print(f"{self.name} got older!")
    
d.ToBorn = types.MethodType(Born, d)
d.ToAge = types.MethodType(Age, d)

#print(d.get_age())
#this returns error AttributeError: 'Dwarf' object has no attribute 'age'
#gimli needs to born first
d.ToBorn()
print(d.get_age())
d.ToAge()
print(d.get_age())
d.ToAge(5)
print(d.get_age())


  