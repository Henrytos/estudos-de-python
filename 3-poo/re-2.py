class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produto: {self.name} - R$ {self.price} reais"

    def discount(self, perc_discount):
        valorDiscount = (self.price/100) *perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)
    
xbox = Product("Xbox One", 4000)
print(xbox)
print(xbox.discount(20))
iphone = Product("Iphone 14", 8000)
print(iphone)
print(iphone.discount(10))