# Problema:
Dados dois números inteiros, n e m, quantos dígitos tem n ^ m ?

Exemplos:

2 e 10 - 210 = 1024 - 4 dígitos

3 e 9 - 39 = 19683 - 5 dígitos

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2867

# Resolução:

A ideia do exercício é que você mostre na tela quantos dígitos tem n elevado a m. Isso pode ser calculado usando a fórmula `log10(n ^ m) + 1`.

Nesse exercício vamos declarar quatro variáveis do tipo `int`:
```c
  int C, N, M, i;
```
`C` irá guardar o número de casos de teste. `N` é número da base da potência, `M` representa o expoente. `i` é uma variável auxiliar para o `for`.

Pra começar o exercício fazemos a leitura do `C` no `scanf` para determinar quantas potências serão calculadas:
```c
  scanf("%d", &C);
```
Sabendo o número de testes, fazemos um `for` para ler os números envolvidos na potência e responder quantos dígitos tem a potência resultante:
```c
  for(i = 0; i < C; i++) {
    scanf("%d %d", &N, &M);
    printf("%.f\n", (floor(M * log10(N))) + 1);
  }
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Nesse caso lemos a base `N` e o expoente `M`. Para poder aplicar a fórmula `log10(n ^ m) + 1`, simplificamos ela usando uma das [propriedades do logaritmo](https://www.infoescola.com/matematica/definicao-e-propriedades-dos-logaritmos/). Essa propriedade mostra que `log10(b ^ c)` equivale a `c * log10(b)`. Sabendo disso vamos usar o `printf` para mostrar o número inteiro resultante da fórmula `(M * log10(N)) + 1`.

Para mostrar o resultado inteiro, usamos a função `floor` da biblioteca `math.h`. Ela vai retornar apenas o valor inteiro de um número, sem fazer aproximações. Além disso, dentro do `printf` usamos `%.f` para que nenhuma casa decimal seja mostrada.

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a biblioteca math.h: [math.h](http://linguagemc.com.br/a-biblioteca-math-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
