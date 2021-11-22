# Problema 1759 - Beecrowd - Iniciante - Nível 1

# Leitura do número de 'Ho'
N = int(input())

# Criamos uma lista com N Ho's
hos = ['Ho'] * N

# Usamos join para intercala-los com espaço
hos = ' '.join(hos)

# Printamos com ! no fim
print(f"{hos}!")