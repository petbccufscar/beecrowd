'''
Recebemos o valor de entrada, já utilizando a função int para convertê-lo, já que em python todo input retorna uma string.
Em seguida, criamos um loop for de 1 a 11 (para multiplicador assumir valores de 1 a 10)
Para cada iteração, exibimos a mensagem como solicitado, montado uma tabuada do valor de entrada.
'''

N = int(input())

for multiplicador in range(1,11):    
    print(f'{multiplicador} x {N} = {multiplicador * N}')


'''
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
'''