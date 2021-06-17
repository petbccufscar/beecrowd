# Problema 1930 - URI - Iniciante - Nível 1

# Leitura das quantidade de tomadas de todas as réguas disponíveis
tomadas = list(map(int, input().split(' ')))

# Como sempre são 4 réguas, e estão ligadas uma na outra,
# 3 tomadas serão utilizadas nessas ligações
print(f'{sum(tomadas) - 3}')