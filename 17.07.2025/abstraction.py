from abc import ABC, abstractmethod

# Abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class: CreditCard
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Concrete class: UPI
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Instantiate and call pay() to demonstrate abstraction
payment1 = CreditCard()
payment2 = UPI()

payment1.pay(1500)
payment2.pay(750)
