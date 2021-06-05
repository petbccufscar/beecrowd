# Problema 1005 - URI - Iniciante - Nível 2

# Leitura dos valores de a e b
a = float(input())
b = float(input())

# Calculo da média
media = (3.5*a + 7.5*b) / 11

# Impressão dos dados usando f-string
#   Mais informações podem ser encontradas na documentação oficial - https://www.python.org/dev/peps/pep-0498/#no-binary-f-strings
print(f'MEDIA = {media:.5f}')