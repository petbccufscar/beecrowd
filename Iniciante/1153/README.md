# Problema:

Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1153

# Resolução:

O objetivo desse exercício é criar a operação de fatorial e responder o valor de N! (N fatorial). 

Para começar, criamos três variáveis do tipo `int`:
```c
    int i, x, N;
```
`N` é a variável mencionada no enunciado. `i` será usada durante o laço de repetição `for` e `x` vai guardar a resposta do exercício.

Precisamos ler o valor de `N`. Aqui vamos usar o `scanf` para ler o valor:
```c
    scanf("%d", &N);
```
Depois de ler esse valor, igualamos `x` a `N`. Como a operação fatorial é uma sequência de multiplicações, podemos multiplicar o valor em `x` sem alterar o valor lido:
```c
    x = N;
```
Para fazer as multiplicaões, usamos a estrutura `for` e, dentro dela, multiplicamos `x` pelo valor presente em `i`:
```c
    for (i=1;i<N;i++)
      x = x * i;
```
Dentro dos parênteses estão as informações iniciais do laço de repetição (`i=1`), condição de parada (`i<N`) e procedimento feito a cada repetição (`i++`). Sempre que a mesma variável aparece em ambos os lados de uma operação matemática, a variável da esquerda será atualizada com base no valor antigo dessa variável e assim atualizamos o valor de `x` a cada multiplicação.

Por fim, escrevemos na tela o resultado. O `\n` no fim serve para pular uma linha na tela depois de mostrar o texto:
```c
    printf("%d\n", x);
```

##### Para aprender um pouco mais sobre fatorial: [Fatorial](https://brasilescola.uol.com.br/matematica/fatorial-principio-fundamental-da-contagem.htm)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
