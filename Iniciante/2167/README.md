# Problema:

Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre ocorria uma queda quando as medidas eram feitas em intervalos de 10 ms. Mas esta queda acontecia em medidas diferentes a cada novo teste do motor.

Zé ficou curioso com essa falta de padrão e quer saber, para cada teste do motor, qual a primeira medida em que ocorre uma queda de velocidade.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2167

# Resolução:

O objetivo desse exercício é ler vários testes de motor e descobrir quando ocorreu uma redução de velocidade. Isso vai ocorrer quando um valor for menor que o dado anterior e devemos responder em qual teste isso ocorreu.

Nesse exercício vamos declarar três variáveis do tipo `int`:
```c
    int N, R[100], i;
```
`N` irá armazenar o número de testes do motor. `R` é um vetor que representa a lista de testes e `i` é uma variável auxiliar que vai ser usada no `for`.

Precisamos saber quantos testes serão feitos. Para isso lemos um valor usando o `scanf`:
```c
    scanf("%d", &N);
```
Agora vamos ler os testes. Criamos um laço de repetição e, dentro dele, lemos os valores correspondentes a cada teste e guardamos o valor no vetor `R`. Ao iniciar o laço de repetição, usamos `scanf` para ler os dados:
```c
    for(i=0;i<N;i++)
      scanf("%d", &R[i]);
```
Com os valores dentro de um vetor, vamos comparar um valor com o seu dado anterior e, se for menor (`R[i-1] > R[i]`), isso indicará queda de velocidade, então mostramos na tela qual foi o teste que mostrou essa queda usando `printf`:
```c
    for(i=1;i<N;i++) {
      if (R[i-1] > R[i]) {
        printf("%d\n", i+1);
        return 0;
      }
    }
```
Aqui novamente usamos um `for` para repetição. Caso uma das comparações resulte no resultado que estamos procurando, mostramos o valor de `i+1` porque um vetor sempre começa na posição 0. Isso quer dizer que o teste 1 está na posição 0 do vetor e assim em diante. Depois de mostrar o valor na tela, encerramos o programa com `return 0`, o mesmo usado normalmente no fim do código.

Caso não tenha nenhuma queda de velocidade, mostramos `0` na tela e encerramos o programa:
```c
    printf("0\n");
```
##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre if: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
