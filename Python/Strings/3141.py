# Problema 3141 - Beecrowd - Strings - Nível 5

# Leitura dos valores
nome = input()
dia_atual, mes_atual, ano_atual = map(int, input().split('/'))
dia_aniv, mes_aniv, ano_aniv = map(int, input().split('/'))

# Checagem de aniversário
if dia_aniv == dia_atual and mes_aniv == mes_atual:
    print("Feliz aniversario!")

# Calculando idade
# Primeiro verificar se no ano atual já fez aniversário
if mes_aniv < mes_atual or (mes_atual == mes_aniv and dia_aniv <= dia_atual):
    idade = ano_atual - ano_aniv
else:
    idade = ano_atual - ano_aniv - 1

print(f"Voce tem {idade} anos {nome}.")