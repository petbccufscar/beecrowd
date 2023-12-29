while True:
    try:
        # Leitura do valor N para o caso de teste
        valor = int(input())
        # Lista para armazenar os códigos dos livros
        numero = []

        # Loop para ler N códigos dos livros e adicioná-los à lista
        for i in range(valor):
            # Leitura do código do livro e adição à lista
            num = input()
            numero.append(num)

        # Ordena a lista de códigos
        ordenado = sorted(numero)

        # Imprime os códigos ordenados
        for i in range(valor):
            print(ordenado[i])
    except EOFError:
        # Se ocorrer EOFError, encerra o loop
        break
