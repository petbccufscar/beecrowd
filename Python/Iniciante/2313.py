# Problema 2313 - Beecrowd - Iniciante - Nível 3

# Conhecimento necessário:
#  Um triângulo é válido se a soma de dois lados é maior do que o terceiro lado.
#  Um triângulo isóceles tem dois lados iguais, um equilátero tem todos os lados iguais
#  Um triângulo retângulo tem seu maior lado = C seguindo a equação C² = A² + B² (Teorema de Pitágoras)

# Input dos dados do problema, dividimos a string em uma lista, e convertemos cada elemento para um inteiro
lados = list(map(int, input().split()))

if (lados[0] == lados[1] == lados[2]):
    # Se o triângulo é equilátero ele é sempre válido, e já podemos dar a resposta
    # Nenhum triângulo equilátero é retângulo
    print("Valido-Equilatero")
    print("Retangulo: N")
    exit() # Saimos do programa imediatamente

# Vamos fazer 3 checagens no total, uma para cada lado
valido = True
isoceles = False
maior_lado = [0, 0, 0]
for i in range(3):
    # Vamos usar o operador de módulo para obter em cada iteração
    # Um dos lados, e os outros dois nas variáveis abaixo.
    l1, l2, l3 = [lados[i], lados[(i+1)%3], lados[(i+2)%3]]

    # Tire o comentário abaixo para ver como funciona
    # print("Verificando os lados nessa ordem:", l1, l2, l3)

    # Verificamos se é inválido
    if (l1 >= l2 + l3):
        valido = False
        break # Saimos do loop imediatamente
    if (l1 == l2):
        # Marcamos como isoceles
        isoceles = True
    if (l1 > maior_lado[0]):
        # Aproveitamos o loop para conseguir o maior
        # lado do triângulo, guardamos numa lista
        # com o maior lado na primeira posição
        maior_lado = [l1, l2, l3]

# Fora do loop verificamos se o triângulo é válido
if (valido):
    # E depois se é isoceles
    if (isoceles):
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    
    # Também verificamos se é retângulo
    if (maior_lado[0]**2 == maior_lado[1]**2 + maior_lado[2]**2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")

