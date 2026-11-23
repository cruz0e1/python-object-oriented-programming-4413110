import random

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

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

companies={
    "AAPL": "Apple", 
    "GOOGL": "Alphabet",
    "AMZN": "Amazon",
    "FB": "Facebook",
    "MSFT": "Microsoft"  
}  

s = [Stock(name, random.randint(100, 500), company) for name,  company in companies.items()]

print("Before sorting:")
for stock in s:
    print(f"{stock.company}: {stock.ticker}: {stock.price}") 
print("\nAfter sorting:")
s.sort()
for stock in s:
    print(f"{stock.company}: {stock.ticker}: {stock.price}") 
