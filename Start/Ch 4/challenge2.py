# Python code​​​​​‌​​​​‌​‌​‌​‌‌​‌​​​​​‌​​​‌​ below
# Use print("messages...") to debug your solution.
from dataclasses import dataclass

@dataclass
class Asset:
    price: float
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
    
@dataclass
class Stock(Asset):
    ticker: str
    company: str


@dataclass
class Bond(Asset):
    description: str
    duration: int
    interest: float

b1 = Bond(95.31, "30 Year US Treasury", 30, 4.38)
b2 = Bond(96.70, "10 Year US Treasury", 10, 4.28)
s1 = Stock(342.0, "MSFT", "Microsoft Corp") 
s2 = Stock(135.0, "GOOG", "Google Inc")

print(b1 < b2)  # True
print(s1 > s2)  # True

