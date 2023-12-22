# Problema 2588 - Beecrowd - Strings - Nível 3

# Estamos tratando de anagramas aqui então basta verificarmos quantos pares de letras temos na palavra
# Uma palíndromo sempre vai ter x pares de letras e no máximo uma letra sem par.

# Loop de entrada do programa
try:
    while sequencia := input():
        # Vamos usar a função de ordenação do python para juntar letras iguais
        # Percorremos a string verificando se encontramos pares
        ultimaLetra = None
        nroPares = 0
        for letra in sorted(sequencia):
            if ultimaLetra == letra: 
                nroPares += 1
                ultimaLetra = None
            else: 
                ultimaLetra = letra
        
        # Cálculo do número de letras sem par
        semPar = len(sequencia) - nroPares*2
        # Se temos letras sem par, precisamos completar a sequẽncia com semPar-1 letras
        # (Lembrando que podemos deixar no máximo uma letra sem par, e queremos adicionar
        #  o mínimo de letras possíveis para tornar a sequẽncia um palíndromo)
        if semPar != 0: semPar -= 1
        print(semPar)
except:
    # No caso de EOF saímos do programa
    exit()