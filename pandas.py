"""
Funcionalidades de Series:
1-Armazenamento de Dados Unidimensionais
2-Utilizado em Operações Vetorizada
3-Focado em Dados Estruturados
"""
import pandas as pd

#1-Dados ds times e suas quantidades de títulos
dados = {
    'Real Madrid': 34,
    'Barcelona':26,
    'Liverpool':19,
    'Juventus':36,
    'Bayern Munich':30
}

#2-Criando a serie a partir de um dicionário
series_times = pd.Series(dados)
print(series_times)
print(type(series_times))

#3-Selecionar time por índice
print(series_times['Juventus'])
print(series_times.iloc[2])

#4-Selecionando por Fatiamento
print('\n')
print(series_times['Barcelona':'Juventus']) # inclusivo

#5-Selecionando por condição
print('\n')
print(series_times[series_times > 30])


#1-Dados ds times e suas quantidades de títulos
dados_titulos = {
    'Real Madrid': 34,
    'Barcelona':26,
    'Liverpool':19,
    'Juventus':36,
    'Bayern Munich':30
}
#2-Ano do título
dados_anos = {
    'Real Madrid': [1956, 1957, 1958, 1959, 1960],
    'Barcelona':[1992, 2006, 2009, 2011, 2015],
    'Liverpool':[1977, 1978, 1981, 1984, 2005],
    'Juventus':[1958, 1985, 1996, 2011, 2015],
    'Bayern Munich':[1974, 1975, 1976, 2001, 2013]
}

#3-Criando a Series
series_titulos = pd.Series(dados_titulos)
series_anos = pd.Series(dados_anos)

print(series_titulos)
print(series_anos)

#4-Criando Dataframe combinando as Series
data = {'Títulos': series_titulos, 'Anos':series_anos}
dataframe_times = pd.DataFrame(data)

#5-Exibindo o DataFrame
print(dataframe_times)

mais_titulos = dataframe_times['Títulos'].mean()
print(f"medias de tiulos:{mais_titulos}") 
nome_time = dataframe_times['Títulos'].idxmax()
print(f"o time com mais titulos é {nome_time}")
anos = dataframe_times['Anos'].explode()
ano_com_mais_titulo= anos.mode()[0]
print(anos)
print(f"ano_com_mais_titul { ano_com_mais_titulo}")

usuarios = {
    "nome":["henry","nathalia"],
    "salario":[1000,200],
    "idade":[17,17],
    "signo":["libras","libras"]
}

# new_table = pd.DataFrame(usuarios)
# new_table.to_excel('pessoas.xlsx',index=False)


#2-maior salario
ganha_mais = table_persons[table_persons['salario'] == table_persons['salario'].max()]
ganha_menos = table_persons[table_persons['salario'] == table_persons['salario'].min()]
print(ganha_mais)
print(ganha_menos)

#3-Distribuição de salários
print(table_persons['salario'].value_counts())

