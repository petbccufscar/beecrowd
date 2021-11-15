# Problema 1117 - Beecrowd - Iniciante - Nível 1
# Laço que recebe nota1 na entrada e para apenas se o valor estiver no intervalo [0, 10]
while (nota1 := float(input())) < 0 or nota1 > 10: print('nota invalida')
# Laço que recebe nota2 na entrada e para apenas se o valor estiver no intervalo [0, 10]
while (nota2 := float(input())) < 0 or nota2 > 10: print('nota invalida')
# Mostrando resultado da média na tela
print(f'media = {(nota1+nota2)/2.0}')
