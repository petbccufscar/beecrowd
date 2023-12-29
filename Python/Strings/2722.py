# Problema 2722 - Beecrowd - Strings - Nível 3

# Input casos de teste
n = int(input())

# Loop dos casos de teste
for i in range(n):
    s1 = input()
    s2 = input()

    # Vamos transformar cada string em um iterador
    s_iters = [iter(s1), iter(s2)]

    # Essa variável vai indicar de qual linha estamos 
    # pegando os caracteres no momento
    iter_atual = 0

    # Armazenamos o resultado conforme ele é feito aqui
    resultado = ""

    while (True):
        # Enquanto no loop, definimos prox como os próximos 2 caracteres
        # Do iterador atual
        try:
            # Adicionamos os próximos dois caracteres ao resultado
            resultado += next(s_iters[iter_atual])
            resultado += next(s_iters[iter_atual])
            iter_atual = (iter_atual + 1) % 2 # E mudamos o iterador atual para a outra linha
        except:
            if (iter_atual == 1):
                # Saímos do loop se chegamos ao fim do iterador da segunda linha
                break
            else:
                # Senão, mudamos de iterador para pegar o resto da outra linha
                iter_atual = (iter_atual + 1) % 2
    
    print(resultado)
