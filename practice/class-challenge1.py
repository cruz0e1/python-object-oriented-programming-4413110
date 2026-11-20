from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price
        
    @abstractmethod    
    def get_description(self):
        pass
    
class Stock(Asset):
    def __init__(self, ticker, price, description):
        super().__init__(price)
        self.ticker = ticker
        self.description = description
       
    def get_description(self):        
        return f"{self.ticker}: {self.description} -- ${self.price}"

class Bond(Asset):
    def __init__(self, bondprice, bondname, duration, interest):
        super().__init__(bondprice)
        self.description = bondname
        self.duration = duration        
        self.interest = interest        
    def get_description(self):
        return f"{self.description}: {self.duration} : ${self.price} : {self.interest}%"


# Create instances of Stock and Bond
s = Stock("MSFT", 342.0, "Microsoft Corp")
b = Bond(95.31, "30 Year US Treasury", 30, 4.38)

# Call get_description() and print the results
print(s.get_description())
print(b.get_description())

