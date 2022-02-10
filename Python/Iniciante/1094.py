# Problema 1094 - Beecrowd - Iniciante - Nível 3

# Iniciamos com todos os resultados como 0
coelhos = ratos = sapos = total = 0

# Recebemos do usuário o número de entradas que iremos ter,
# inserindo como o número de iterações do FOR
for i in range(int(input())):

    # A cada iteração, separamos a 'quantidade' do 'animal'
    # somamos ao total de animais
    quantidade, animal = input().split(' ')
    total += int(quantidade)

    # Adicionamos também o valor ao respectivo resultado do 'animal'
    if animal == 'C':
        coelhos += int(quantidade)
    elif animal == 'R':
        ratos += int(quantidade)
    elif animal == 'S':
        sapos += int(quantidade)

# Após o final do FOR e de suas iterações, mostramos os resultados
# de acordo com a formatação desejada.
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {((100.0 / total) * coelhos):.2f} %")
print(f"Percentual de ratos: {((100.0 / total) * ratos):.2f} %")
print(f"Percentual de sapos: {((100.0 / total) * sapos):.2f} %")