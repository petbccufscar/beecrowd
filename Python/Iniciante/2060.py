# Problema 2060 - Beecrowd - Iniciante - Nível 1

# Entrada de dados, a primeira linha um número inteiro e a segunda é a lista
qtd_numeros = int(input())
lista_nums = input().split(" ")

# Declaração de variáveis auxiliares
mlt_2 = 0
mlt_3 = 0
mlt_4 = 0
mlt_5 = 0

# Calculos dos múltiplos
for i in range(qtd_numeros):
    if(int(lista_nums[i])%2==0):
        mlt_2 +=1 
    if(int(lista_nums[i])%3==0):
        mlt_3 +=1
    if(int(lista_nums[i])%4==0):
        mlt_4 +=1
    if(int(lista_nums[i])%5==0):
        mlt_5 +=1

# Apresentação da saída
print(f"{mlt_2} Multiplo(s) de 2\n{mlt_3} Multiplo(s) de 3\n{mlt_4} Multiplo(s) de 4\n{mlt_5} Multiplo(s) de 5")