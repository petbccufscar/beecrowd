# Problema 1020 - Beecrowd - Iniciante - Nível 2

# Vamos ler o número de dias e converter o valor para inteiro
dias = int(input())

# Começamos calculando o número de anos
anos = dias//365
dias = dias%365

# Depois o número de meses
meses = dias//30
dias  = dias%30

# Então printamos todos os valores
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
