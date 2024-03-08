names = ['henry','franz','ramos','arcaya']

print(names)
print(names[1:])
print(names[:2])
print(names[0])
print(names[-1])
# metodos de array
gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print(gamesList.index("Star Wars"))

# 3 - Adiciona item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()
#listaJogos.reverse()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Fifa23')
gamesReset.remove('Star Wars')
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)
