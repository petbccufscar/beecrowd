# Problema 2670 - Beecrowd - Iniciante - Nível 3

# Lista para armazenar os funcionários em cada andar.
listFuncAndar = []

# Recebe três valores e coloca na lista de funcionários por andar.
for i in range(3):
    listFuncAndar.append(int(input()))

# Calcular o melhor andar para se colocar a cafeteira, é preciso notar que
# se o andar que possui o maior número de funcionários, for maior que a soma
# dos outros andares, ele recebe a cafeteira, caso contrário o segundo andar é o
# mais apropriado para colocar a cafeteira.
maxFuncionarios = max(listFuncAndar)
andarCafeteira = listFuncAndar.index(maxFuncionarios)

# Remove o maior valor da lista para fazer a soma e fazer o teste do melhor andar
# para se colocar a cafeteira.
listFuncAndar.remove(maxFuncionarios)

# Se o melhor andar para colocar a cafeteira seja o segundo, reinsere o valor de maior
# número de funcionários e ajusta o andar da cafeteira para o segundo andar, que na lista
# refere-se ao indice 1.
if sum(listFuncAndar) > maxFuncionarios:
    listFuncAndar.insert(andarCafeteira, maxFuncionarios)
    andarCafeteira = 1
else:
    listFuncAndar.insert(andarCafeteira, maxFuncionarios)


# Calculando qual o total de minutos gastos pelos funcionários para pegar café.
# Sabendo que a cafeteira está no andar que possue maior número de funcionários.
totalMinutos = 0
for i in range(3):
    fim = andarCafeteira
    inicio = i

    if i > andarCafeteira:
        fim = i
        inicio = andarCafeteira

    # Calcular a distância (final - inicial) que os andares estão da cafeteira e assim aumentar
    # o número dos minutos em relação aos números de funcionários daquele andar, lembre-se
    # se um funcionário sobe ou desce para pegar o café, ele deve descer ou subir novamente
    # para trabalhar, por isso a necessidade de multiplicar por 2, os valores.
    totalMinutos += 2 * (fim - inicio) * listFuncAndar[i]

# Apresentação do valor total de minutos.
print(f"{totalMinutos}")
