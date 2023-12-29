# Este loop executa continuamente até ser interrompido explicitamente
while True:
    try:
        # Lê uma linha de entrada e divide as palavras usando '-' como delimitador
        texto = input().split('-')

        # Inicializa uma variável para armazenar o acrônimo COBOL
        cobol = ''

        # Itera sobre cada palavra na lista 'texto'
        for palavra in texto:
            # Converte o primeiro e último caracteres da palavra para minúsculo
            i = palavra[0].lower()
            f = palavra[len(palavra) - 1].lower()

            # Verifica se a palavra forma parte do acrônimo COBOL
            if len(cobol) == 0 and (i == 'c' or f == 'c'):
                cobol += 'c'
            elif len(cobol) == 1 and (i == 'o' or f == 'o'):
                cobol += 'o'
            elif len(cobol) == 2 and (i == 'b' or f == 'b'):
                cobol += 'b'
            elif len(cobol) == 3 and (i == 'o' or f == 'o'):
                cobol += 'o'
            elif len(cobol) == 4 and (i == 'l' or f == 'l'):
                cobol += 'l'

        # Verifica se o acrônimo COBOL foi formado
        if cobol == 'cobol':
            print('GRACE HOPPER')
        else:
            print('BUG')

    # Captura a exceção EOFError para encerrar o loop quando atingir o final do arquivo de entrada
    except EOFError:
        break
