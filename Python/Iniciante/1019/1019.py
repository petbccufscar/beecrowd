# -*- coding: utf-8 -*-

segundos = int(input()) #Obtenção de dados apartir da função input, com o caster de inteiro.

#Conversao de segundos para horas e minutos
horas = segundos/3600 
segundos = segundos%3600 #Uso do caracter '%' (resto), que calcula o resto da divisão entre segundos e 3600.
minutos = segundos/60
segundos = segundos%60
print("%d:%d:%d"%(horas,minutos,segundos))
