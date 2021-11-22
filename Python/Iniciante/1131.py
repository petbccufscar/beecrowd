# Problema 1131 - Beecrowd - Iniciante - Nível 1
# Inicialização de contadores de placar
vitorias_gremio = 0
vitorias_inter = 0
empates = 0

# Entrada de placar de gols usando map
inter, gremio = map(int, input().split(' '))

# Verificação de qual time ganhou para ajustar contadores
if gremio > inter:
    vitorias_gremio += 1
elif gremio < inter:
    vitorias_inter += 1
else:
    empates += 1

# While verificando se o usuário digitou 1 ou 2
while (continua:= int(input('Novo grenal (1-sim 2-nao)\n'))) == 1:
    
    # Entrada de placar de gols usando map
    inter, gremio = map(int, input().split(' '))
    
    # Verificação de qual time ganhou para ajustar contadores
    if gremio > inter:
        vitorias_gremio += 1
    elif gremio < inter:
        vitorias_inter += 1
    else:
        empates += 1

# Exibição dos placares na saída de dados
print(f'{empates + vitorias_inter + vitorias_gremio} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'Empates:{empates}')

# Verificação de qual time ganhou mais e exibição de resultado
# Final na saída de dados
if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_inter < vitorias_gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
