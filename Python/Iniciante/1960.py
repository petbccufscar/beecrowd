# Problema 1960 - Beecrowd - Iniciante - Nível 2

#Função para determinar qual letra representa o maior algarismo do numero
def romano(n):
    if n == 1000: return 'M'
    if n ==  900: return 'CM'
    if n ==  500: return 'D'
    if n ==  400: return 'CD'
    if n ==  100: return 'C'
    if n ==   90: return 'XC'
    if n ==   50: return 'L'
    if n ==   40: return 'XL'
    if n ==   10: return 'X'
    if n ==    9: return 'IX'
    if n ==    5: return 'V'
    if n ==    4: return 'IV'
    if n ==    1: return 'I'

#Recebe a entrada do numero
numero = int(input())

#Faz um loop para todos os casos possíveis de conversão
for i in 1000,900,500,400,100,90,50,40,10,9,5,4,1:
    while numero >= i:

        #Anota a letra que representa o maior algarismo da lista
        print(romano(i),end='')

        #Subtrai o numero inicial pelo numero que já foi convertido em algarismo romano e permanece no loop
        numero -= i

#Imprime todas as letras que estavam acumuladas no buffer
print()


