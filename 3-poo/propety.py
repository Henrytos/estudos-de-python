class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
             raise TypeError("Nome deve ser uma string")
        self._name = value

pessoa = Person("Fulano")
print(vars(pessoa))



class Circle:
    def __init__(self, radius):
        self._radius = radius  # Atributo privado

    

c = Circle(5)
print("Raio:", c.radius)  
c.radius = 7
print("Raio modificado:", c.radius)

print("Área do círculo:", c.area)
