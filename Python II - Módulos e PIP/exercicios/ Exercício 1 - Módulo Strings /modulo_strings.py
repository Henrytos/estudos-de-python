#
#Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:
#Inverter uma string de trás pra frente.
#Retornar apenas letras com índice par.
#Retornar apenas letras com índice ímpar.

def reverse_text(text=""):
  return text[::-1]

def even_letters(text=""):
  return text[::2]


def odd_letters(text=""):
  return text[1::2]