'''
Recebemos o valor de entrada, já utilizando a função int para convertê-lo, já que em python todo input retorna uma string.
Em seguida, criamos um loop for de 2 (primeiro par) a N+1 (para englobar também o valor N como solicitado pelo problema) e passo 2, que nos garante que em todas iterações, a variável par será efetivamente par.
Com isso, atribuimos o resultado de "par ** 2" a variável quadrado.
'''

N = int(input())

for par in range(2,N+1,2):
    quadrado = par ** 2
    print(f'{par}^2 = {quadrado}')


'''
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
'''