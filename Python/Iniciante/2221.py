# Problema 2221 - Beecrowd - Iniciante - Nível 2

#Função para fazer o cálculo do valor do golpe 
def golpe(x, bonus):
    ValorGolpe = float((x[0]+x[1])/2)
    if (x[2] % 2) == 0:
        ValorGolpe += bonus
    return ValorGolpe

#Recebe quantas vezes o código vai rodar
instancias = int(input())

#Cria um loop que decrementa a quantidade de instancias até chegar em zero
while instancias:
    instancias -= 1

    #Anota o buff que será utilizado no cálculo
    bonus = int(input())

    #Recebe os dados dos jogadores
    DadosDabriel = list(map(int,input().split()))
    DadosGuarte = list(map(int,input().split()))

    #Chama a função para fazer o cálculo
    ValorDabriel = golpe(DadosDabriel, bonus)
    ValorGuarte = golpe(DadosGuarte, bonus)

    #Compara o valor obtido para ver qual foi o ganhador
    if ValorDabriel > ValorGuarte:
        print('Dabriel')
    elif ValorGuarte > ValorDabriel:
        print('Guarte')
    else:
        print('Empate')
