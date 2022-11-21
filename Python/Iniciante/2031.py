# Problema 2031 - Beecrowd - Iniciante - Nível 2

# sexto 24
n = int(input())

# Possíveis respostas
r = {
    "1": "Jogador 1 venceu", 
    "2": "Jogador 2 venceu", 
    "ambos": "Ambos venceram", 
    "sem": "Sem ganhador", 
    "mutua": "Aniquilacao mutua"
}
r_key = "" # Chave da resposta a ser impressa

for i in range(n):
    jogo = [input(), input()];
    
    # Jogador 1 usou...
    match jogo[0]:
        # ...ataque
        case 'ataque':
            # Jogador 2 usou...
            match jogo[1]:
                # ...ataque
                case 'ataque':
                    r_key = "mutua"
                # ...pedra
                case 'pedra':

                # ...papel
                case 'papel':
        # ...pedra
        case 'pedra':
            # Jogador 2 usou...
            match jogo[1]:
                # ...ataque
                case 'ataque':
                    
                # ...pedra
                case 'pedra':

                # ...papel
                case 'papel':
        # ...papel
        case 'papel':
            # Jogador 2 usou...
            match jogo[1]:
                # ...ataque
                case 'ataque':
                    
                # ...pedra
                case 'pedra':

                # ...papel
                case 'papel':

    print(r[r_ind])
    # Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
    # Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
    # Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
    # Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
    # Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
    # Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.

    # a - a = aniquilação
    # p - p = sem ganhador
    # pa - pa = ambos vencem

    # pa - a = a ganha
    # p - pa = pedra ganha
    # a - p = a ganha