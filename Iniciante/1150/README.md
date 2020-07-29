# Problema:

Faça um programa que leia dois inteiros: X e Z (devem ser lidos tantos valores para Z quantos necessários, até que seja digitado um valor maior do que X para ele). Conte quantos números inteiros devem ser somados em sequência (considerando o X nesta soma) para que a soma ultrapasse a Z o mínimo possível. Escreva o valor final da contagem.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1150

# Resolução:

Nesse exercício, devemos ler dois números e contar quantos números foram somados a X (incluindo X) até ultrapassar o valor de Z. A cada soma, o número somado a X aumenta em 1.

Vamos precisar de 4 variáveis do tipo `int` nesse exercício:
```c
    int X, Z, soma, res;
```
As primeiras variáveis `X` e `Z` representam os inteiros que serão lidos no exercício. `soma` representa o resultado das somas feitas no valor `X` e `res` indica a quantidade de números que foram somados a `X`.

Para começar o algoritmo, vamos igualar `res` a 1:
```c
    res = 1;
```

Temos que obter o valor `X`. Usaremos `scanf` para ler um valor:
```c
    scanf("%d", &X);
```
No início, igualamos `res` a 1 porque a variável `X` representa um número da soma que será feita para ultrapassar `Z`. Para ler a próxima variável precisamos usar a estrutura `do... while`:
```c
    do {
      scanf("%d", &Z);
    } while (Z <= X);
```
O laço de repetição é necessário para garantir que `Z` seja maior que `X`. Essa comparação é feita dentro do parênteses pela operação `Z <= X` e, caso seja verdadeira, a leitura da variável será feita novamente.

Pra descobrir quando a soma vai ultrapassar `Z`, igualamos `soma` à variável `X`:
```c
    soma = X;
```
Agora temos que somar a variável `soma` até que o valor dela seja maior que `Z`. Como não sabemos quantas somas serão necessárias, faremos um laço de repetição com `while`:
```c
    while (soma <= Z) {
```
Dentro dessa repetição, a primeira coisa a se fazer é incrementar o valor `X`, pois o valor original dessa variável já foi somada à variável `soma`:
```c
      X++;
```
Em seguida, devemos somar o novo `X` na soma:
```c
      soma = soma + X;
```
Sempre que a mesma variável aparece em ambos os lados de uma operação matemática, a variável da esquerda será atualizada com base no valor antigo dessa variável. Como um número foi adicionado na `soma`, atualizamos o valor de `res`:
```c
      res++;
    }
```
A cada número somado, aumentamos em 1 o valor da variável. As mudanças em `X`, `soma` e `res` vão se repetir enquanto o valor da `soma` for menor ou igual a `Z`. Quando for maior, a repetição acaba e escrevemos na tela quantos números foram necessários para ultrapassar o valor de `Z`. Para isso usamos `printf`:
```c
    printf("%d\n", res);
```
O `\n` no fim serve para pular uma linha na tela depois de mostrar o texto.

##### Para aprender um pouco mais sobre a estrutura do.. while: [Do... While](http://linguagemc.com.br/comando-do-while/)
##### Para aprender um pouco mais sobre a estrutura while:[While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre o operador ++: [Auto-incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
