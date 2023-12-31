import pandas as pd


#1- importando dados
data = pd.read_excel("data/VendaCarros.xlsx") 

print(data)

#2- Lista primeiros registros
print(data.head())

#3- Lista os primeiros registros
print(data.tail())

#4- Contagem de valores por fabricante

print(data["Fabricante"].value_counts)