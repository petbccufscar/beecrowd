#leitura da matring
matring = []
for i in range(4):
    linha_input = input()
    matring.append(linha_input)

#funcao para decodificar a mensagem
def decode(matring):
    #definindo o primeiro e o último numero
    linha_tam = len(matring[0])
    f = ''
    l = ''
    for i in range(4):
        f += matring[i][0]
        l += matring[i][linha_tam - 1]
    f = int(f)
    l = int(l)

    #decodificando a mensagem: Ci = (F * Mi + L) mod 257
    output = ''
    for i in range(1,linha_tam - 1):
        m = ''
        for j in range(4):
            m += matring[j][i]
        c = (f * int(m) + l) % 257
        output += chr(c)
    return output

print(decode(matring))
