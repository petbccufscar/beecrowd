# Problema 2708 - URI - Iniciante - Nível 1

# Inicialização das variáveis que representam a quantidade de turistas e jipes
total_turistas = 0
total_jipes = 0
# Laço para efetuar a leitura de dados enquanto não for digitada a palavra "ABEND"
while (linha := input()) != 'ABEND':
    # Armazenando os valores da ação e da quantidade de turistas em suas
    # respectivas variáveis
    acao, turistas = linha.split()[0], int(linha.split()[1])
    # Caso a ação seja igual a "SALIDA", somar 1 no total de jipes e somar na
    # quantidade total a quantidade recebida na entrada de turistas que saíram
    if acao == 'SALIDA':
        total_jipes += 1
        total_turistas += turistas
    # Caso a ação seja igual a "VUELTA", subtrair 1 do total de jipes e subtrair
    # da quantidade total a quantidade recebida na entrada de turistas que voltaram
    elif acao == 'VUELTA':
        total_jipes -= 1
        total_turistas -= turistas
# Exibição da quantidade restante de turistas e jipes que ainda não voltaram
print(total_turistas)
print(total_jipes)
