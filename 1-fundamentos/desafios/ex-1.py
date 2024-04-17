'''
Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.

Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses núm
'''

number = int(input("digite um numero:\n"))
print(f"o antecessor é {number - 1}  e sucessor é {number + 1}")


note_one = int(input("digite sua primeira nota:\n"))
note_two = int(input("digite sua segunda nota:\n"))
note_three = int(input("digite sua terceira nota:\n"))
note_four = int(input("digite sua quarta nota:\n"))

average_grade = (note_one + note_two + note_three + note_four) / 4

print(f"sua nota media foi {average_grade}")
