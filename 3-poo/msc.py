
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

