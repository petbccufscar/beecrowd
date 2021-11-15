# Problema 2061 - Beecrowd - Iniciante - Nível 1

# Entrada de dados, primeiro o número de abas já abertas e o segundo o valor de ações feitas por Péricles
n_abas,n_acoes = map(int,input().split(" "))

# Recebendo quais ações foram feitas
for i in range(n_acoes):
    acao = input()
    if(acao=="fechou"):
        n_abas +=1
    elif(acao=="clicou"):
        n_abas -=1

# Apresentando o número de abas final
print(n_abas)