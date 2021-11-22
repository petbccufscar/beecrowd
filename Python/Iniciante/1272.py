# Problema 1272 - URI - Iniciante - Nível 3

# Quantidade de casos teste que serão
# recebidos na entrada padrão
casosTeste = int(input())

for i in range(casosTeste):
    # Mensagem informada na entrada padrão
    mensagem = input()

    # String que irá armazenar a mensagem oculta
    mensagemOculta = ""

    # Itera sobre cada palavra
    for palavra in mensagem.split():
        # Concatena com a inicial da palavra
        mensagemOculta += palavra[0]

    print(mensagemOculta)
