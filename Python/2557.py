# Problema 2557 - Beecrowd - Strings - Nível 2
from gettext import find
from sys import stdin
import re # Vamos usar regex para remover os números de dentro das strings que vamos receber

# Vamos ler do stdin até acabar
for linha in stdin:
    # Queremos pegar todos os números das strings, então:
    # "3+8=J" Vira [3, 8]
    # "5+L=5" Vira [5, 5]
    # "R+7=5" Vira [7, 5]
    # re.findall() Acha tudo que se encaixa no regex
    # Usamos r'\d+' que significa: "Encontre uma substring composta de um ou mais números"
    numeros = [int(x) for x in re.findall(r'\d+', linha)]
    # Se a string original tiver 'J', significa que temos que somar os dois números que extraimos
    if linha.find('J') != -1:
        print(numeros[0] + numeros[1])
    # Mas nos outros dois casos, 'R' e 'L", só precisamos pegar o número da direita (J) e subtrair o da esquerda 
    # que vai sempre estar na primeira posição numeros[0] (R ou L, a operação é a mesma)
    else:
        print(numeros[1] - numeros[0])

    
    # Exemplo
    # numeros[0]
    # |   numeros[1]
    # |   |
    # 3 + 8 = J
    # Fazemos a soma normal, numeros[0] + numeros[1] = J

    # numeros[0]
    #     |   numeros[1]
    #     |   |
    # R + 7 = 5
    # Fazemos a subtração R = 5 - 7, R = numeros[1] - numeros[0]
    # Mas se fosse 5 + L = 7, faríamos L = 5 - 7, L = numeros[1] - numeros[0]
    # A posição dos números continuaria a mesma