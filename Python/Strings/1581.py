# Problema 1581 - Beecrowd - Strings - Nível 2

# Entrada de número de casos de teste.
numTest = int(input())

# Vetor para guardar a idioma que deve ser falado a cada caso de teste.
respostas = []

# For loop, para receber informações sobre os casos.
for i in range(numTest):
    numPessoas = int(input())
    
    # Pausa o loop se o número de pessoas for muito pequeno, ou inválido.
    if (numPessoas<2):
        break

    # Recebe o primeiro idioma, para comparar com as próximos idioma das pessoas.
    idioma1 = input()

    # Variável de teste para ver se os idiomas são iguais.
    idiomaIgual = True

    # Loop para receber qual a idioma nativo cada um fala, -1 pois já foi obtido na
    # função "input()" do "idioma1".
    for j in range(numPessoas - 1):
        idiomaAux = input()

        # Se os idiomas forem diferentes, a variável de controle idiomaIgual é false.
        if (idioma1 != idiomaAux):
            idiomaIgual = False
    
    # Testando a variável de teste, para decidir qual idioma deve ser falado, se false,
    # então há mais de 1 idioma nativo entre as pessoas, assim o idioma a ser falado deve ser o inglês.
    if (idiomaIgual == False):
        respostas.append("ingles")
    else:
        respostas.append(idioma1)

# For loop para mostrar as respostas para cada caso de teste.
for i in range(numTest):
    print(respostas[i])
