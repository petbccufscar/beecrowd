# Problema:

Para esconder do malvado Grinch onde será a festa, ela resolveu ultilizar o sistema de reuniões dos Duendes, que funciona assim: cada duende tem um identificador numérico único e, quando haverá uma reunião, é escolhida a casa de um dos duendes para sediar o encontro. Mas ao invés de escrever o número do duende anfitrião no mural da fábrica do Papai Noel, onde todos podem ver, é escrito o identificador de exatamente todos os duendes com números menores que o dele e que são coprimos ao dele. Esse método é também uma forma de dizer que esses duendes do mural devem levar as comidas e bebidas para a reunião.

Dada a carta que os duendes receberam, determine na casa de qual Duende será a festa de aniversário de Giovana.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2845

# Resolução:

A ideia do exercício é que você mostre na tela qual o número de identificação duende que vai disponibilizar a casa para fazer a festa. O número sempre será um valor maior que o maior número listado na carta.

Nesse exercício vamos declarar quatro variáveis do tipo `int`:
```c
  int N, A[10000], maior, i;
```
`N` irá armazenar quantos números estão escritos na carta. `A` é um vetor que representa a lista de números escritos na carta, `maior` é uma variável que vai guardar o valor do maior número e `i` é uma variável auxiliar que vai ser usada no `for`.

Precisamos saber quantos números serão escritos. Para isso lemos um valor usando o `scanf`:
```c
  scanf("%d", &N);
```
Agora, vamos ler os dados. Criamos um laço de repetição `for` e, dentro dele, lemos os números de identificação correspondentes a cada duende e guardamos o valor no vetor `A`. Ao iniciar esse laço de repetição, usamos `scanf` para ler os dados:
```c
  for(i=0;i<N;i++)
    scanf("%d", &A[i]);
```
Com os valores obtidos, vamos descobrir qual o maior valor do vetor. Primeiro guardamos o primeiro valor do vetor (`A[0]`) na variável `maior`:
```c
  maior = A[0];
```
Aqui novamente usamos um `for` para repetição. Caso outro número do vetor seja maior que o valor de `maior` (`maior < A[i]`), atualizamos o valor da variável com o número guardado na posição `i` do vetor:
```c
  for (i=0;i<N;i++)
    if (maior < A[i])
      maior = A[i];
```
Depois de passar por todos o valores do vetor, mostramos na tela o valor que foi pedido no enunciado. A resposta sempre será o valor da variável `maior` mais 1:
```c
  printf("%d\n", maior+1);
```

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre if: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
