# Problema 1871 - Beecrowd - Iniciante - Nível 1

# Laço de repetição infinito para executar todos os casos de teste até a função quit() ser chamada
while True:

    # Leitura das variávies iniciais
    x, y = map(int,input().split())

    # Condição de parada caso ambas as variáveis forem nulas
    if x==0 and y==0:
        quit()

    # Soma
    soma = x+y

    # Transformando a soma em uma string e substituindo os caracteres 0 por caracteres nulos
    soma=int(str(soma).replace('0',''))

    # Imprimindo a soma sem zeros
    print(f'{soma}')


