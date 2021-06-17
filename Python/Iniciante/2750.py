# Problema 2750 - URI - Iniciante - Nível 1

# No Python, a impressão de valores OCTAL e HEXADECIMAL tem formatações específicas
# que impedem a impressão de forma correta, logo, foram criadas 3 listas, cada uma com os valores
# em suas respecitivas bases
numerosD = list(range(16))
numerosO = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17]
numerosH = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

# Impressão do cabeçalho da tabela
print("---------------------------------------")
print("|  decimal  |  octal  |  Hexadecimal  |")
print("---------------------------------------")

# FOR responsável pela impressão da tabela formatada
# ':^N' alinha a variável de forma centralizada ocupando N casas.
for x in range(16):
    print(f'|  {numerosD[x]:^9}|{numerosO[x]:^9}|{numerosH[x]:^15}|')

# Impressão do rodapé da tabela
print("---------------------------------------")