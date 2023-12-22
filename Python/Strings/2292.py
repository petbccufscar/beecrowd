# Problema 2292 - Beecrowd - Strings - Nível 6

# Como cada lâmpada só pode estar desligada ou ligada vamos representar o painel
# Usando uma lista de booleanos

# Escrevemos algumas funções auxiliares para a conversão entre strings e a lista

def paraBool(strPainel):
    # Montamos uma lista, cada item é o resultado da comparação
    # lampada == 'X', para cada caractere no painel (e.g XXOOX)
    return [lampada == 'O' for lampada in strPainel]

def paraStr(boolPainel):
    # Montamos uma lista, cada item é X se lampada for verdadeiro, O se 
    # for falso. Para converter a lista para string, usamos join em uma 
    # string vazia.
    return ''.join(['O' if lampada else 'X' for lampada in boolPainel])

# Criamos então uma função para calcular o novo painel após N iterações
# Note que a abordagem iterativa (i.e calcular o novo painel a cada iteração)
# é muito lento para os padrões do beecrowd, e recebe timeout.
def alterna(boolPainel, n):
    resultado = []
    for i in boolPainel:
        resultado.append(not i if n%2 != 0 else i)
        n = (int(i) + n) // 2 # Falso + alterna / 2
    return resultado

# Com as funções feitas basta implementar a leitura e execução das funções.
for i in range(int(input())):
    strPainel, num = input().split(' ')
    boolPainel = paraBool(strPainel)
    num = int(num)

    boolPainel = alterna(boolPainel, num)

    print(paraStr(boolPainel))

# Alternativas às funções paraBool e paraStr
'''
def paraBool(strPainel: str) -> List[bool]:
    boolPainel = []
    for lampada in strPainel:
        if lampada == 'O':
            boolPainel.append(True)
        elif lampada == 'X':
            boolPainel.append(False)
        else:
            print("Erro, formato incorreto do strPainel")
            return []
    return boolPainel

def paraStr(boolPainel):
    strPainel = ""
    for lampada in boolPainel:
        if lampada:
            strPainel += 'O'
        else:
            strPainel += 'X'
    return strPainel
'''