# OPERAÇÔES COM STRINGS
first_name = 'henry '
last_name = 'franz'
menssage = """
olá isso é um texto
multilinea
"""

full_name = first_name + last_name
print(full_name)
print(first_name*5)
print(first_name in full_name)

print(menssage)


# SUBSTRINGS
# var[inicio,fim,base]
# por default base é 1 o fim = size -1 oo inicio será 0 como array
print(full_name[::])
print(full_name[0:5])
# par
print(full_name[::2])
# inpar
print(full_name[1::2])
# inverter
print(full_name[::-1])

