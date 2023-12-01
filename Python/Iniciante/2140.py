notas = [2, 5, 10, 20, 50, 100]

while (True):
    t1, t2 = map(int, input().split())
    if (t1 == 0 and t2 == 0):
        break
    troco = abs(t1 - t2)

    # Achar o maior troco possível com uma nota
    n1 = -1 # Primeira nota
    for i, n in enumerate(notas):
        if (troco - n >= 0):
            n1 = i
    troco -= notas[n1]
    if n1 == -1:
        # Temos um troco que não encaixa com nenhuma nota
        print("impossible")
        continue
    
    # Existem situações em que pegar o maior troco possível
    # já acaba com o troco, mas é possível dividir em duas
    # e.g o troco é 100 reais, ao invés de devolver 100 reais
    #     queremos devolver 2*50 reais
    # A solução abaixo procura generalizar para qualquer 
    # conjunto de notas essas situações.
    if (troco == 0 and n1 != 0):
        if (notas[n1-1]*2 == notas[n1]):
            print("possible")
            continue
    else:
        # Vamos tentar encaixar o que sobrou do troco então
        if troco in notas:
            print("possible")
            continue
        else:
            print("impossible")
            continue
