# Problema 1239 - URI - Strings - Nível 3

# Flags de Sinalização
italico = False
negrito = False

# Todas as entradas são lidas até receber EOF
while True:
    try:
        fraseInicial = input()
        fraseFinal = ""
        
        # Para cada letra da frase, é feita uma verificação
        for x in fraseInicial:

            # Se for _ e a flag de italico estiver False, é substituido por <i> na fraseFinal
            # então, a flag é alterada para True
            if (x == '_') and not italico:
                fraseFinal += "<i>"
                italico = True

            # Se for _ e a flag de italico estiver True, é substituido por </i> na fraseFinal
            # então, a flag é alterada para False
            elif (x == '_') and italico:
                fraseFinal += "</i>"
                italico = False

            # Se for * e a flag de italico estiver False, é substituido por <b> na fraseFinal
            # então, a flag é alterada para True
            elif (x == '*') and not negrito:
                fraseFinal += "<b>"
                negrito = True

            # Se for * e a flag de italico estiver True, é substituido por </b> na fraseFinal
            # então, a flag é alterada para False
            elif (x == '*') and negrito:
                fraseFinal += "</b>"
                negrito = False
                
            # Caso não seja nenhum caractere especial, a letra somente é copiada
            else:
                fraseFinal += x
        
        # Impressão da frase resultante na tela
        print(fraseFinal)
    except EOFError:
        break
