# Problema 1789 - Beecrowd - Iniciante - Nível 3

# A condição de parada para o programa é EOF, logo
# colocamos a condição dentro de um loop infinio.
while True:
    try:
        # Não necessitamos da primeira entrada, com a quantidade
        # de lesmas por grupo, utilizamos '_' para sinalizar isso.
        _ = int(input())

        # Separamos e transformamos a entrada a seguir
        # em um objeto 'map' de inteiros.
        grupoLesmas = map(int, input().split(' '))

        # Decobrimos o maior valor do 'grupoLesmas'
        turbo = max(grupoLesmas)
        
        # Categorizamos o valor de acordo com a tabela de velocidades
        if turbo < 10:
            resposta = '1'
        elif turbo < 20:
            resposta = '2'
        elif turbo >= 20:
            resposta = '3'

        # O resultado é informado na tela
        print(resposta)

    # Caso EOF seja encontrado, o loop infinito para, com o comando 'break'
    except EOFError:
        break