# Problema 1154 - Beecrowd - Iniciante - Nível 1

# Começamos lendo a primeira idade (já convertendo para float, já que a média pode ser ponto flutuante)
idade = float(input())

# A soma das idades começa em 0 pois podemos não ter nenhuma entrada.
soma = 0

# Também utilizaremos um contador, para saber quantas idades estamos lidando para a média.
i = 0

# Enquanto a idade for maior que 0, continuaremos lendo idades para o cálculo da média.
while(idade >= 0):

    # Durante o loop, apenas somamos as idades e recebemos a próxima.
    soma += idade
    idade = float(input())
    i = i + 1

# Por fim, calculamos e imprimimos a média (soma das idades/quantidade de idades)
media = float(soma/i)

# Limitamos 
print(f'{media:.2f}')