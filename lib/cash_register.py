#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount= 0):
    self.discount = discount
    self.total=0
    self.items=[]
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self,value):
    if  isinstance(value, (int, float)) and 0 <= value <= 100 :
      self._discount =value
    else:
            raise ValueError("Discount must be a number between 0 and 100.")
  
  def add_item(self, item_name, price, quantity=1):
        self.items.append([item_name, price, quantity])
        self.total += price * quantity

  def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:    
            print("There is no discount to apply.")

  def get_total(self):
        return f"Total: ${self.total:.2f}"

  def get_items(self):
      return [item[0] for item in self.items] 
  
register = CashRegister(10)
register.add_item("eggs", 1.99)
register.add_item("tomato", 1.76)

print(register.get_items())
print(register.get_total())   