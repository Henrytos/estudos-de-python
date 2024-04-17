import random

list = ['a', 'b', 'c', 'd', 'e']
str = "henry franz"
a = random.randint(0,10)
print(a)

random_item = random.choice(list)
print(random_item)

random_items = random.sample(list,2)
print(random_items)

caracter = random.choice(str)
print(caracter)
caracters = random.sample(str,2)
print(caracters)


