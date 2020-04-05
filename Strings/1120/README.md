# Problema 1120
Durante anos, todos os contratos da Associação de Contratos da Modernolândia
(ACM) foram datilografados em uma velha máquina de datilografia.

Recentemente Sr. Miranda, um dos contadores da ACM, percebeu que a máquina
apresentava falha em um, e apenas um, dos dígitos numéricos. Mais
especificamente, o dígito falho, quando datilografado, não é impresso na folha,
como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que
isso poderia ter alterado os valores numéricos representados nos contratos e,
preocupado com a contabilidade, quer saber, a partir dos valores originais
negociados nos contratos, que ele mantinha em anotações manuscritas, quais os
valores de fato representados nos contratos. Por exemplo, se a máquina
apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato como
100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor
numérico representado no contrato, ou seja, nessa mesma máquina, o número 5000
corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso).

# Resolução
Primeiramente deve-se receber a entrada para a primeira iteração, separando-a
em duas variáveis por um espaço:
```python
a, b = input().split()
```
Então filtramos os caracteres da string b que são diferentes de a e atribuímos
isso à l:
```python
l = list(filter(lambda x: x!=a, b))
```
Testamos se a lista l é vazia, se for imprimos zero, caso contrário percorremos
a lista retirando os zeros à esquerda, e mais uma vez se for vazia imprimimos
zero:
```
if l:
    result = "".join(dropwhile(lambda x: x=='0', l))
    print(result if result else 0)
else:
    print(0)
```
#### Requer a importação de dropwhile do módulo itertools
