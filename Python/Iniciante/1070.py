# Leitura do valor de x
x = int(input())

# Calculo do menor ímpar maior ou igual à x
#   x%2 retorna 1 se x é ímpar
#   (x+1)%2 retorna 1 se x é par
#   se somamos 1 a um x par, ele se torna ímpar
x += (x+1)%2

# Loop para imprimir os seis valores
for i in range(6):
    print(x)
    x += 2

# Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
# Facebook  - https://www.facebook.com/petbcc/
# Instagram - https://www.instagram.com/petbcc.ufscar/
# Ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com