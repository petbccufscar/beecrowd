# Problema 2753 - URI - Iniciante - Nível 1

# Mesmo que pedido, não iremos declarar 27 variáveis, iremos fazer apenas os prints da forma correta.

# Usaremos um contador de soma para em cada iteração, somar 1 a mais que o valor anterior.
contador_soma = 0

# Criaremos um loop de 97 a 97+26(123).
for i in range (97,123):
    # Exibimos a soma de i com o contador na forma inteira
    # Utilizando a função chr convertemos o número para um caractere da tabela ASCII.
    print(f'{i+contador_soma} e {chr(i+contador_soma)}')
    