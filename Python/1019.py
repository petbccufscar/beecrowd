# Problema 1019 - URI - Iniciante - Nível 1

#Entrada de dados
segundos = int(input())

#Conversao de segundos para horas e minutos
horas = segundos/3600 
segundos = segundos%3600 
minutos = segundos/60
segundos = segundos%60

#Saída de dados
print("%d:%d:%d"%(horas,minutos,segundos))
