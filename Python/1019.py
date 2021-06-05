# Problema 1019 - URI - Iniciante - Nível 1

#Entrada de dados
segundos = int(input())

#Conversao de segundos para horas e minutos
horas = int(segundos/3600) 
segundos = segundos%3600 
minutos = int(segundos/60)
segundos = segundos%60

#Saída de dados
print(f'{horas}:{minutos}:{segundos}')
