class Product:
  def __init__(self,name,price):
    self.name= name
    self.price= float(price)
  
  def __str__(self) -> str:
    return f"Produto:{self.name} Preço:{self.price}"
  
  def apply_discount(self,discount):
    discount_price = self.price - (self.price * discount/100)
    print(f"R${self.price} -> R${discount_price}")
  
smartphone = Product("Smartphone",100)
smartphone.apply_discount(20)
print(smartphone)