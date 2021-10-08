lista_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    try:
        entrada = input()
        nova_entrada = ''
        for i in entrada:
            if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')):
                nova_entrada += i
                continue

            if (i.islower()):
                pos = lista_min.index(i)
                if (pos <= 12):
                    nova_entrada += lista_min[pos + 13]
                else:
                    nova_pos = 12 - (25 - pos)
                    nova_entrada += lista_min[nova_pos]

            else:
                pos = lista_mai.index(i)
                if (pos <= 12):
                    nova_entrada += lista_mai[pos + 13]
                else:
                    nova_pos = 12 - (25 - pos)
                    nova_entrada += lista_mai[nova_pos]
        print(nova_entrada)
    except EOFError:
        break

