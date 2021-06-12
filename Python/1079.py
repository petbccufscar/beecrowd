 # Problema 1079 - URI - Iniciante - Nível 1

#Leitura da variavel 'n' que será número de vezes que será calculada a média ponderada
n = int(input())

#Loop que lerá 'n' vezes as notas dos alunos
for i in range(n):

 # Leitura das três notas
 a, b, c = map(float, input().split(' '))

 # Cálculo da média ponderada
 media_ponderada = (a*2 + b*3 + c*5)/10

 # Print da média ponderada
 print(f'{media_ponderada:.1f}')
