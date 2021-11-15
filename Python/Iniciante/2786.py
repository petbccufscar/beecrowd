# Problema 2786 - Beecrowd - Iniciante - Nível 1

# Leitura das variáveis de entrada
largura = int(input())
comprimento = int(input())

# Cálculo de ambos os pisos, dado que cada piso do tipo 1 tem 0.5 metros quadrados, e os do tipo 2 metade desse valor

piso_2 = (largura-1)*2 + (comprimento-1)*2

piso_1 = (largura*comprimento -(0.5*piso_2/2) -0.5)/0.5

# Printando as saídas
print(f'{int(piso_1)}')
print(f'{int(piso_2)}')
