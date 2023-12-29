# Problema 2049 - Beecrowd - String - Nível 4

# O operador "walrus" (:=), permite a gente colocar um valor dentro de
# uma variável, e comparar o valor atribuido ao mesmo tempo
# https://realpython.com/python-walrus-operator/
#
# A alternativa disso seria ter um input antes do while, comparar a variável
# e depois ter um outro input dentro do while.
instancia = 1
while (assinatura := input()) != "0":
    painel = input()

    # Gambiarra pra imprimir novas linhas entre cada instância
    # Colocar um print no final dá "Presentation error"
    if instancia != 1: print()

    print(f"Instancia {instancia}")

    if painel.find(assinatura) == -1:
        print("falsa")
    else:
        print("verdadeira")
    
    instancia += 1