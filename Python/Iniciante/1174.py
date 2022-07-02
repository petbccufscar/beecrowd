# Problema 1174 - Beecrowd - Iniciante - Nível 3

# Leitura dos 100 números iniciais
A = []
for i in range(100):
    A.append(float(input()))

# Imprimindo todos os números menores ou iguais a 10
for i in range(100):
    if A[i]<=10:
        print(f'A[{i}] = {A[i]:.1f}') 

