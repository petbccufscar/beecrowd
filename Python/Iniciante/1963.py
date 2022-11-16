# Problema 1963 - Beecrowd - Iniciante - Nível 2

#Recebe a entrada e já a divide em 2 partes para serem armazenadas
num1, num2 = map(float, input('').split())

#Calcula a porcentagem de aumento de preço do novo ingresso
x = ((num2 * 100)/num1) - 100

#Imprime a porcentagem obtida
print(f'{x:.2f}%')