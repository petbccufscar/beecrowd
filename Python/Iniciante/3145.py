# Problema 3145 - Beecrowd - Iniciante - Nível 1

# Leitura dos números N e X, convertendo-os para float através da função map
N, X = map(float, input().split(' '))

# Cálculo dos dias que levarão para o grupo chegar até a Montanha Solitária
dias = X/(N+2)

# Exibição do resultado da divisão na tela, utilizando 2.f para exibir apenas
# dois dígitos decimais
print(f'{dias:.2f}')
