# Problema 2031 - Beecrowd - Iniciante - Nível 2

# Recebe número de casos de teste
n = int(input())

# Possíveis respostas
# Representado com um dicionário só para facilitar a mudança das frases caso
# necessário, outra solução é imprimir as frases diretamente dentro dos ifs 
# abaixo.
r = {
    "1": "Jogador 1 venceu", 
    "2": "Jogador 2 venceu", 
    "ambos": "Ambos venceram", 
    "sem": "Sem ganhador", 
    "mutua": "Aniquilacao mutua"
}
r_key = "" # Chave da resposta a ser impressa

# Pra cada caso de teste
for i in range(n):
    # Recebe duas linhas e coloca numa lista
    jogo = [input(), input()];
    
    # Os ifs externos verificam o que o jogador 1 usou
    if jogo[0] == 'ataque':
        # Os ifs internos verificam o que o jogador 2 usou
        if jogo[1] == 'ataque':
            r_key = "mutua" # ataque - ataque
        else:
            r_key = "1" # ataque - outro
    elif jogo[0] == 'pedra':
        if jogo[1] == 'ataque':
            r_key = "2" # pedra - ataque
        elif jogo[1] == 'pedra':
            r_key = "sem" # pedra - pedra
        else:
            r_key = "1" # pedra - papel
    else:
        if jogo[1] == 'papel':
            r_key = "ambos" # papel - papel
        # Casos em que existe repetição são colocados no else
        # Aqui se o jogador 1 jogou papel, se o jogador 2 
        # jogar qualquer coisa se não papel, ele ganha
        else:
            r_key = "2" # papel - outro
    
    # Imprime a frase correspondente ao final de tudo
    print(r[r_key])