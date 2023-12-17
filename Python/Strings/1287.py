while True:
    try:
        string = input()
        deu_erro = 0
        if string != '':
            number = ''
            #realizando as devidas substituições
            for char in string:
                if char.isdigit():
                    number += char
                else:
                    if char.lower() == "o":
                        number += '0'
                    elif char == "l":
                        number += '1'
                    elif char!= ',' and char != ' ':
                        print("error")
                        deu_erro = 1
                        break
            #se não printou erro já
            if deu_erro == 0:
                #caso a string não seja vazia, mas não tenha nenhum número
                if not number:
                    print("error")
                else:
                    #caso o número seja maior que o limite
                    try:
                        number = int(number)
                        if number > 2147483647:
                            print("error")
                        else:
                            print(number)
                    except ValueError:
                        print("error")
        #caso a string seja vazia, já retorna erro
        else:
            print("error")
    except EOFError:
        break
