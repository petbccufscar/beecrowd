# Problema 2025 - Beecrowd - Strings - Nível 5

import re

for i in range(int(input())):
    # Para cada linha de entrada
    line = input()

    # O jeito mais fácil de especificar o que estamos procurando em cada linha
    # É utilizando regex. Vamos procurar strings que tenham algo no começo, 
    # oulupukk no meio, e mais alguma coisa no final
    # O regex equivalente é: .oulupukk. (. encontra qualquer caractere)

    # A função re.sub(Padrão, Substituição, String) substitui todas as substrings
    # da String que se encaixarem no Padrão pela string de Substituição.
    line = re.sub('.oulupukk.', 'Joulupukki', line)

    # E então imprimimos a nova linha
    print(line)
    
# Procure por sites que permitem visualizar regex (e.g https://regex101.com/)
# Para entender melhor o que acontece.