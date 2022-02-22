# Problema 2150 - Beecrowd - String - Nível 4

# Leitura até o fim do arquivo
while True:
    try:
        # Leitura do alfabeto alienígena
        alfabeto = input()

        # Leitura da frase
        frase = input()

        # Iniciando o contador
        total = 0

        # Contando as ocorrências 
        for letra in alfabeto:
            total += frase.count(letra)

        # Imprimindo o resultado
        print(total)
        
    # Caso chegue no fim do arquivo (EOF), o loop para
    except EOFError:
        break
