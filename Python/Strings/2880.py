mensagem = input()
crib = input()
crib_tam = len(crib)
possiveis_posicoes = 0

#o iterador percorrerá a mensagem enquanto houver espaço para a crib
for i in range(len(mensagem) - len(crib) + 1):
    igual = False
    j = 0
    #enquanto não achar uma letra igual, percorre a substring
    #da mensagem que tem o mesmo tamanho de crib
    while not igual and j < crib_tam:
        if mensagem[i + j] == crib[j]:
            igual = True
        j += 1
    #se não encontrou nenhum caracter igual, é uma possivel posição
    if not igual:
        possiveis_posicoes += 1

print(possiveis_posicoes)    
        