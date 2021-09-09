# Problema 1629 - URI - Strings - Nível 3

# Recebendo o número de casos teste, e apenas para quando o casos teste ser 0.
numTeste = int(input())

while (numTeste != 0):

    # Recebendo linha por visitante
    for i in range(numTeste):
        linha = input()
        zeros = 0
        uns = 0

        # A lógica do programa se baseia que as números em posição pares são a quantidade de uns
        # no arquivo, já as unidades em posição impares são as quantidades de zeros, assim armazenando
        # em variáveis adequadas.
        for i in range(len(linha)):
            if (i % 2 == 0):
                uns += int(linha[i])
            else:
                zeros += int(linha[i])
        
        # O digito é a soma dos algarismos das variávies zeros e uns. Por exemplo: se zeros e uns
        # são 10 e 12, respectivamente. Então será a soma 1 + 0 + 1 + 2 = 4. A soma dos algarismos
        # pode ser feita pela função "map()" dentro da função "sum()". Que se separa os números de uma
        # string e soma todos eles.
        digito = sum(map(int, str(uns)))
        digito += sum(map(int, str(zeros)))
        print(f"{digito}")
    
    # Pega mais um número de testes que será feito.
    numTeste = int(input())
