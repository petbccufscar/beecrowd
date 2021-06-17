# Problema 2061 - URI - Iniciante - Nível 1

# Entrada de dados, primeiro o número de abas já abertas e o segundo o valor de ações feitas por Péricles
n_abas,n_acoes = map(int,input().split(" "))

for i in range(n_acoes):
    acao = input()
    if(acao=="fechou"):
        n_abas +=1
    elif(acao=="cliclou"):
        n_abas -=1
    print(n_abas)
print(n_abas)