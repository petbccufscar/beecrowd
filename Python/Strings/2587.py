# Função para descobrir se duas palavras correspondem ao padrão incompleto fornecido
def descobrir_palavra(palavra1, palavra2, incompleta):
    t1 = []  # Lista para armazenar caracteres de palavra1 que correspondem a '_' em incompleta
    t2 = []  # Lista para armazenar caracteres de palavra2 que correspondem a '_' em incompleta
    i = 1

    # Itera por cada caractere em incompleta
    for e in incompleta:
        if e == '_':
            t1.append(palavra1[i - 1])  # Adiciona o caractere correspondente de palavra1 a t1
            t2.append(palavra2[i - 1])  # Adiciona o caractere correspondente de palavra2 a t2
        i += 1

    # Verifica várias condições para determinar se as palavras correspondem ao padrão
    if (t1[0] == t1[1] or t2[0] == t2[1]
            or (t1[0] == t2[1] and t1[1] != t2[0])
            or (t1[1] == t2[0] and t1[0] != t2[1])
            or (t1[1] == t2[0] and t1[0] == t2[1])
            or (t1[0] == t2[0] and t1[1] == t2[1])):
        return 'Y'  # Retorna 'Y' se as condições forem atendidas
    else:
        return 'N'  # Retorna 'N' caso contrário

# Função principal
def main():
    num_iteracoes = int(input())  # Número de iterações

    # Itera por cada caso de teste
    for _ in range(num_iteracoes):
        palavra1 = input()  # Primeira palavra
        palavra2 = input()  # Segunda palavra
        incompleta = input()  # Padrão incompleto
        resultado = descobrir_palavra(palavra1, palavra2, incompleta)  # Chama a função
        print(resultado)  # Imprime o resultado

# Verifica se o script está sendo executado como programa principal
if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado diretamente
