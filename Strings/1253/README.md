#Problema 1253
Júlio César usava um sistema de criptografia, agora conhecido como Cifra de
César, que trocava cada letra pelo equivalente em duas posições à Esquerda no
alfabeto (por exemplo, 'C' vira 'A', 'T' vira 'R', etc.). Ao começo do alfabeto
nós voltamos para o fim, isto é 'A' vira 'Y'. Nós podemos, é claro, tentar
trocar as letras com quaisquer número de posições.

#Resolução
Para resolver esse problema antes de tudo definimos uma função auxiliar para
realizar a cifra de césar em uma letra:
```python
def caesar(letter, rot):
    return chr(((ord(letter) - ord('A') - rot) % 26) + ord('A'))
```
Ou seja, pega a letra e desloca ela até um intevalo entre 0 e 26, isso é
necessário caso contrário a maneira em que ocorre a operação modular não é
correta. Depois subtrai-se o valor da rotação e força-se o resultado no
intervalo, e depois coloca-se a letra em um intervalo ascii imprimível.

Então basta cria o loop principal, toma-se o número de entradas e cria-se o
loop:
```python
n = int(input())
for _ in range(n):
```
Então basta ler a entrada, a palavra e a rotação:
```python
word = input()
rot = int(input())
```
E por fim mapear a função para cada elemento da palavra e retornar a palavra
cifrada:
```python
print("".join(list(map(partial(caesar, rot=rot), word))))
```
O uso da função partial aqui é feita para realizar a aplicação parcial da
função, ou seja aplicar a função a um argumento, nesse caso rot, criando uma
nova função. Também é possível fazer isso com um outro estilo de código em
Python chamado closure, entretanto não tão semântico e expressivo 
como utilizando a função partial.

#### É necessário importar a função partial de functools
