from collections import Counter , namedtuple,deque
from operator import itemgetter

#contador de elementos 
fruits = ['apple', 'orange', 'apple', 'banana', 'apple', 'banana', 'orange', 'apple', 'banana']
print(fruits)
print(Counter(fruits))


#tupla nomeada
game = namedtuple("game",['name','ano'])


g1 = game('fortinite','2017')
g2 = game('gtav','2013')

print(g1)
print(g2)

#ordenar dicionarios

amigos = {"henry":10,"fulano":9,"ciclano":8} 
print(amigos)
a = sorted(amigos.items(),key=itemgetter(0))
print(a)

#lista 
lista = deque([1,2,3,4,5])
print(lista)
lista.append(6)
lista.appendleft(0)
lista.pop()
lista.popleft()
print(lista)
