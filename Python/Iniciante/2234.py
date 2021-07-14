# Problema 2234 - URI - Iniciante - Nível 1
# Problema 2234 - URI - Iniciante - Nível 1
# Inicializa as variáveis a serem utilizadas
# na resolução e atribui os valores nelas
# por meio do uso da entrada padrão
H, P = [int(i) for i in input().split()]

# Imprime o resultado da divisão
# e especifica na formatação da string
# para inprimir com duas casas decimais,
# sendo que o número 2 em {:.2f} está indicando
# a quantidade de casas decimais e o f diz
# que o número passado é do tipo ponto flutuante
print("{:.2f}".format(H/P))
