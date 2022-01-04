# Problema 1277 - Beecrowd - Strings - Nível 6

# Leitura de quantos casos serão feitos
t = int(input())

# Realiza T casos de teste
for i in range(t):
    # Quantos Nomes e Frequências serão lidas
    n = int(input())

    # Lista de reprovados
    reprovados = []

    # Lemos os nomes
    nomes = input().split(' ')

    # Lemos as frequências
    frequencias = input().split(' ')

    # Para cada aluno
    for nome, frequencia in zip(nomes, frequencias):
        # Contamos quantas presenças, faltas e atestados o aluno tem
        p = frequencia.count('P')
        a = frequencia.count('A')
        m = frequencia.count('M')

        # Cálculo da frequência, caso for inferir há 75% o aluno é adicionado à lista dos reprovados
        if(p / (p + a) < 0.75):
            reprovados.append(nome)

    # Imprimindo os reprovados
    print(' '.join(reprovados))
