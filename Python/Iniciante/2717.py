# Problema 2717 - Beecrowd - Iniciante - Nível 1

# Leitura da quantidade de horas de trabalho que restam para produzir os dois itens
faltam = int(input())
# Leitura da quantidade de tempo necessário para produzir cada item (A e B)
A, B = map(int, input().split(' '))
# Se a soma das horas dos itens A e B ultrapassarem a quantidade de horas que
# faltam para terminar o expediente do duende, exibir a seguinte mensagem na tela
if A + B > faltam:
    print('Deixa para amanha!')
# Caso contrário, exibir a seguinte mensagem
else:
    print('Farei hoje!')
