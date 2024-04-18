class Movie:
    plataform = "OneBitFilmes"
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Plataforma: {Movie.plataform}")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.totalEvaluation}")
        print(f"Total Avaliadores: {self.evaluators}")
        print(f"Duração Filme: {self.durationMinutes}")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name} é: {self.totalEvaluation / self.evaluators}") 
    
        
movie = Movie("Super Mario", 2023, False, 120)
movie2 = Movie("Sonic", 2022, False, 110)
movie.evaluate(8.5)
movie.evaluate(9.0)
movie.technical_sheet()
movie.average()
# Modificando plataforma
Movie.plataform = "OneBitCode Pro"
movie2.evaluate(10.0)
movie2.evaluate(9.5)
movie2.technical_sheet()
movie2.average()



"""
1 - O método de classe utliza o primeiro parâmetro cls referente a classe
2 - O método de classe pode acessar ou modificar o estado da classe 
3 - Usamos o decorator @classmethod em python para criar um método de classe
""" 
class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))

wiiU = Console.from_text("Meu video game é WiiU e o preço é 1000")
ps5 = Console.from_text("Meu video game é Ps5 e o preço é 5000")
xboxOne = Console.from_text("Meu video game é XboxOne e o preço é 4600")
print(wiiU.__dict__)
print(ps5.__dict__)
print(xboxOne.__dict__)


"""
1 - O método estático não possui o parâmetro self.
2 - O método de classe pode acessar mas não pode modificar o estado da classe 
3 - Usamos o decorator @staticmethod em python para criar um método estático
""" 

class Language:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
    
    @staticmethod
    def courses_trail(trail):
        if trail == 'Python Fundamentos':
            courses = ['Dominando o Python', 'Módulos e Pip', 'Orientação a Objetos']
        elif trail == 'Automação com Python':
            courses = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual']
        else:
            courses = ['A definir']
        return courses

print(Language.courses_trail('Python Fundamentos'))
print(Language.courses_trail('Automação com Python'))
print(Language.courses_trail('IA'))



class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.__salary}")
  
       # getter method
    def get_salary(self):
        return self.__salary

    # setter method
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.set_salary(40000)
fulano.show()
sicrano.show()

class Phone: 
    def __init__(self,brand,model_name,price):
        self._brand = brand
        self._model_name =  model_name
        self._price =  max(price,0)
        
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
    
    def __str__(self):
        return f"{self._brand}{self._model_name}"
    
    def discount(self):
        return self._price * 0.10
    
class SmartPhone(Phone): 
     def __init__(self,brand,model_name,price, ram, internal_memory, back_camera):  
        
        super().__init__(brand,model_name,price)  
        
        self.ram = ram
        self.internal_memory =  internal_memory
        self.back_camera = back_camera
        
     def discount(self):
        return self._price * 0.15
        
Moto =  Phone('Moto','G7',1000)
print(Moto)
Moto.make_a_call(232132)
print(f"Valor do {Moto._brand}{Moto._model_name} com desconto é {Moto.discount()}")
print(vars(Moto))

Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(32142342)
print(f"Valor do {Iphone._brand}{Iphone._model_name} com desconto é {Iphone.discount()}")
print(vars(Iphone))



class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
class Fish(Animal):
    race = ""
    
class Parrots(Animal):
    color = ""
    
class Zoo:
    def __init__(self):
        self.animals_dict = {}
        
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f"No nosso zoológico temos {result} quantidade de {category}"

zoo = Zoo()
peixe = Fish("Nemo", "mamíferos")
print(vars(peixe))
papagaio = Parrots("Louro", "aves")
print(vars(papagaio))
zoo.add_animal(peixe)
zoo.add_animal(papagaio)
print(zoo.total_of_category("aves"))
print(zoo.total_of_category("mamíferos"))