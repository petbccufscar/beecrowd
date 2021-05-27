#Laço de repetição que lê números e os coloca em uma lista
#Este for é feito em uma linha e é usado para formar listas
nums = [(float(input())) for i in range(1,7)]

#Outro for usado para iterar sobre a lista num e montar uma
#lista apenas com os números positivos.
#Usa-se a função len para obter-se a quantidades de número positivos
positivos = len([ i for i in nums if i > 0])

#Saída de dados
print(positivos, 'valores positivos')

#Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
#[Facebook](https://www.facebook.com/petbcc/),
#[Instagram](https://www.instagram.com/petbcc.ufscar/)
#ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

