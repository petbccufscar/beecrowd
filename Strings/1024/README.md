# Problema
Solicitaram para que você construisse um programa simples de criptografia. Este
programa deve possibilitar enviar mensagens codificadas sem que alguém consiga
lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e
maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela
ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e
assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na
terceira e última passada, todo e qualquer caractere a partir da metade em
diante (truncada) devem ser deslocados uma posição para a esquerda na tabela
ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta
entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento
inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos
caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# Resolução

Antes de tudo definos uma função auxiliar para a primeira rodada pela string:
```python
def first_run(letter):
    if letter in ascii_letters:
        letter = chr(ord(letter) + 3)
    return letter
```
Basicamente ela nos diz se for um caractere alfabético então deve-se movimentar
três unidades para a direita, caso contrário mantém o mesmo valor. Então
passamos ao loop principal do programa; lemos a primeira linha que nos diz
quantas entradas teremos:
```python
n = int(input())
i = 0
#### Para aprender mais sobre entrada e saída em Python: [Entrada e saída](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)

```
Então nós lemos a string, calculamos e calculamos o seu ponto médio:
```python
word = input()
mid = len(word) // 2
```
Rodamos então a função em todos os caracteres da palavra e revertemos a posição
de todos os caracteres:
```python
aux = list(map(first_run, word))[::-1]
```
#### Para comprender um pouco sobre fatiamento de listas em Python: [Fatiamento em Python](https://pythonhelp.wordpress.com/2011/11/12/fatiamento-slicing-de-strings-em-python/)
#### Para comprender um pouco sobre programação funcional em Python: [Programação Funcional](https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/)
Dividimos então a string em duas partes, do começo até sua metade, e de sua
metade até o final, mas já alterando o final com a terceira passada por meio de
uma função anônima:
```python
a = aux[:mid]
b = list(map(lambda x: chr(ord(x)-1), aux[mid:]))
```
Finalmente, juntamos a palavra, imprimos e incrementamos o contador:
```python
print("".join(a+b))
i += 1
```
