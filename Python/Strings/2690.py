# Problema 2690 - Beecrowd - Strings - Nível 3

# Criando o dicionário
conjunto = ['GQaku', 'ISblv', 'EOYcmw', 'FPZdnx', 'JTeoy', 'DNXfpz', 'AKUgq', 'CMWhr', 'BLVis', 'HRjt']
conversao = {' ': ''}
for i in range(10):
    conversao.update(dict.fromkeys(list(conjunto[i]), str(i)))

print(conversao)

# Loop de quantidade de senhas a serem trocadas
for _ in range(int(input())):
    senha = ''
    for c in input():
        try:
            senha += conversao[c]
        except KeyError:
            senha += ''
    print(senha[:12])