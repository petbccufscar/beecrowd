import re

# União +
# Intersecção *
# Diferença -
# Intersecção vem antes de união e diferença

# Vamos usar regex para encontrar as expressões com parênteses mais internas
# Resolvemos essas primeiro, substituindo na string original

import re

def calcular_parenteses(input_str: str):
    # Exemplo: ({A}+{B})+{C}
    match = re.search(r"\(([^()]+)\)", input_str)

    if not match:
        return None

    # "({A}+{B})" -> é o que, no final do cálculo, vamos substituir
    parenteses = match.group(0) 
    
    # {A}+{B} -> Apenas a expressão que queremos calcular
    expressao = string_para_lista(match.group(1))
    resultado = lista_para_string(calcula(expressao))
    return input_str.replace(parenteses, resultado)

def calcula(expressao):
    if len(expressao) == 1:
        return expressao

    if len(expressao) > 3:
        # Temos mais de uma operação
        expressao = expressao[0:2] + [calcula(expressao[2:])]
    
    # Nesse ponto, expressão contém somente {?} op {?}
    # Primeiro pegamos qual a operação
    operacao = expressao[1]
    if operacao == '+':
        return list(set(expressao[0]).union(set(expressao[2])))
    elif operacao == '-':
        return list(set(expressao[0]).difference(set(expressao[2])))
    elif operacao == '*':
        return list(set(expressao[0]).intersection(set(expressao[2])))

def string_para_lista(input_str: str):
    resultado = []
    grupo_atual = []

    for char in input_str:
        if char == "{":
            continue
        elif char == "}":
            resultado.append(grupo_atual)
            grupo_atual = []
        elif char.isalpha():
            grupo_atual.append(char)
        else:
            resultado.append(char)
    
    return resultado

def lista_para_string(lista):
    # print(lista)
    if len(lista) <= 1:
        if not isinstance(lista[0], list):
            return "{" + lista[0] + "}"
        lista = lista[0]
    lista = [lista]
    resultado = ""

    for item in lista:
        if isinstance(item, list):
            resultado += "{" + "".join(item) + "}"
        else:
            resultado += item
    
    return resultado

def resolve(conjunto):
    resultado = calcular_parenteses(conjunto)
    while resultado is not None:
        conjunto = resultado
        resultado = calcular_parenteses(conjunto)

    conjunto = calcula(string_para_lista(conjunto))
    conjunto.sort()
    conjunto = lista_para_string(conjunto)

    return conjunto

# MAIN
conjunto = input()
while conjunto:
    print(resolve(conjunto))
    try: 
        conjunto = input()
    except EOFError:
        break