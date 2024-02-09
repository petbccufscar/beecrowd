while True:
    try:    
        #leitura das 3 linhas:
        #tag a ser substituida eh case insensitive
        tag = input().lower()
        #tag number que substituirá a tag
        tag_num = input()
        #linha contendo as taqs
        line = input()
        #dividindo a linha em palavras  de acordo com as tags
        words = line.replace('<', '.<').replace('>', '>.').split('.')
        #texto novo
        new_line = ''

        #substituindo as tags dentro de <>
        for word in words:
            if word != '':
                if word[0] == '<':
                    new_line += word.lower().replace(tag, tag_num)
                else:
                    new_line += word

        #a partir deste ponto, as tags foram substituídas, porém, o texto está todo em minúsculo
        #agora, devemos retornar as palavras que não são tags para maiúsculo
        palavras_originais = line.split(' ')
        palavras_alteradas = new_line.split(' ')
        new_line = ''
        for i in range(len(palavras_alteradas)):
            if palavras_originais[i].lower() == palavras_alteradas[i]:
                new_line += palavras_originais[i] + ' '
            else:
                new_line += palavras_alteradas[i] + ' '

        #é necessário tirar a caracter de quebra de linha, se não, o beecrowd aponta 'formatação errada'
        print (new_line[0:len(new_line) - 1])
    except EOFError:
        break
