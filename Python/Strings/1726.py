# Função para converter entrada em string de set()
def to_set(entrada: str):
    # Trocando os símbolos de união e intersecção
    # No python apenas a diferença tem o mesmo símbolo
    entrada = entrada.replace('+','|')\
                     .replace('*', '&')
    
    # A fim de não percorrer o alfabeto inteiro, trocamos apenas as
    # letras encontradas na entrada, tomando cuidado para não chamar
    # replace numa mesma letra várias vezes
    replaced_chars = set()
    for char in entrada:
        if char.isalpha() and char not in replaced_chars:
            replaced_chars.add(char)
            entrada = entrada.replace(char, f"'{char}',")
    
    # Removendo vírgulas adicionais, trocando símbolo de conjunto vazio
    return entrada.replace(",}", "}").replace("{}", "set()")\

# MAIN
entrada = input()
while entrada:
    # Transformar em set() do python
    entrada_set = to_set(entrada)
    solved_set = eval(entrada_set)
    solved_set = sorted(list(solved_set))

    # Imprimir no formato {ABCD}
    print("{", end='')
    for item in solved_set:
        print(item, end='')
    print("}")

    try:
        entrada = input()
    except:
        exit()