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