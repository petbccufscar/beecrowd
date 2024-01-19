# Problema 1864 - Beecrowd - Iniciante - Nível 2

# Leitura da entrada que representa a quantidade de caracteres 
N = int(input())

# Decodificando o texto fornecido pelo enunciado do problema
# Seleciona-se somente os caracteres sublinhados do enunciado e duduz-se os espaços na citação de Søren Kierkegaard
citacao = [
    'L', 'I', 'F', 'E', ' ',
    'I', 'S', ' ',
    'N', 'O', 'T', ' ',
    'A', ' ',
    'P', 'R', 'O', 'B', 'L', 'E', 'M', ' ',
    'T', 'O', ' ',
    'B', 'E', ' ',
    'S', 'O', 'L', 'V', 'E', 'D'
]

# Juntando os N primeiros caracteres
n_primeiros_caracteres = "".join(citacao[:N])

# Imprimindo os N primeiros caracteres
print(n_primeiros_caracteres)