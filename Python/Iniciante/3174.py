# Problema 3174 - Beecrowd - Iniciante - Nível 1
# Quantidade de horas necessárias para
# produzir um por presente em uma
# determinada equipe
bonecos = 8
arquitetos = 4
musicos = 6
desenhistas = 12

# Variáveis que irão contabilizar quantas
# horas contabilizam cada grupo em um dia,
# baseado na soma dos horários de cada elfo
bonecosHoras = 0
arquitetosHoras = 0
musicosHoras = 0
desenhistasHoras = 0

# Quantidade de elfos contratados pelo
# Papai Noel é um valor inteiro e,
# portanto, elfos recebe um valor
# inteiro da entrada padrão
elfos = int(input())



for i in range(elfos):
    E, G, H = input().split()

    if G == "bonecos":
        bonecosHoras = bonecosHoras + int(H)
    if G == "arquitetos":
        arquitetosHoras = arquitetosHoras + int(H)
    if G == "musicos":
        musicosHoras = musicosHoras + int(H)
    if G == "desenhistas":
        desenhistasHoras = desenhistasHoras + int(H)

# Inicializa a variável que irá contabilizar
# a quantidade de presentes produzidos por dia
presentes = int(bonecosHoras/bonecos) +\
        int(arquitetosHoras/arquitetos) +\
        int(musicosHoras/musicos) +\
        int(desenhistasHoras/desenhistas)

print(presentes)
