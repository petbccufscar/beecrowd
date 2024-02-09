# Problema 1664 - Beecrowd - Strings - Nível 7
import re
from fractions import Fraction

# palavras = []
entrada = ''

while True:
    try:
        linha = input()
    except EOFError:
        break;

    if linha == '':
        break
    else:
        entrada += f" {linha}"

# Dividindo por jogo
original = entrada
jogos = entrada.count("BULLSHIT")
entrada = entrada.split("BULLSHIT")[:jogos] # Removemos o último jogo se ele não estiver completo!

# Transformando cada jogo numa lista de palavras
entrada = [re.findall(r'[a-zA-Z]+', jogo.lower()) for jogo in entrada]
# Percorrendo jogos
palavras_diferentes = 0
for jogo in entrada:
    palavras = set()
    for palavra in jogo:
        if palavra not in palavras:
            palavras.add(palavra)
            palavras_diferentes += 1 

result = Fraction(palavras_diferentes, jogos)
print(f"{result.numerator} / {result.denominator}")