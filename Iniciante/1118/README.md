# Problema:

Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1118

# Resolução:

A primeira parte do enunciado é igual ao do exercício 1117 do URI. Ela pede um programa que calcule a média entre duas notas, sendo que essas notas devem estar entre 0 e 10. Para isso você deve conferir se os dois valores escritos estão entre 0 e 10 antes de calcular a média. No entanto, o código desse exercício deve ser capaz de fazer um novo cálculo sempre que responder 1 depois da mensagem `novo calculo (1-sim 2-nao)`, ou seja, a repetição pode ocorrer quantas vezes o usuário quiser.

Existem inúmeras formas de fazer o exercício. No entanto, se o tempo de execução do código for muito extenso, resultará em `runtime error` e o seu código não será aceito. Então temos que fazer o código usando o menor número de laços de repetição e comparações possível.

Para começar, criaremos quatro variáveis, sendo três do tipo `double` e uma do tipo `int`:
```c
    double nota, media, nro_notas;
    int x;
```
Depois de criar as variáveis, iremos igualar `media` e `nro_notas` a 0. Isso será importante para algumas comparações a seguir.
```c
    media = 0;
    nro_notas = 0;
```
Agora, para iniciar a repetição que permitirá ao usuário fazer quantos cálculos quiser, usaremos a função `while`:
```c
    while(1) {
```
Esse `while` não possui condição alguma para sair do laço. Assim a repetição ocorre até que o programa seja encerrado com uma função como `return`, por exemplo. Isso é feito para evitar comparações sempre que um ciclo se encerra, cada comparação custa tempo para ser feito e precisamos criar um algoritmo rápido nesse exercício.

A primeira coisa a ser feita no ciclo é ler um valor usando a função `scanf`:
```c
      scanf("%lf", &nota);
```
Depois de ler a variável `nota`, vamos verificar se o valor é válido. Verificamos se o valor é menor que 0 (`nota < 0`) ou maior que 10 (`nota > 10`) usando a função `if`. Se a verificação for verdadeira, ele mostrará na tela a mensagem `nota invalida`:
```c
      if(nota < 0 || nota > 10)
         printf("nota invalida\n");
```
Caso a verificação for falsa, seguiremos no `else` e adicionaremos esse valor na variável `media` e somaremos 1 no valor da variável `nro_notas`:
```c
      else {
         media = media + nota;
         nro_notas++;
```
Nesse ponto, vemos o motivo de ter igualado essas duas variáveis a 0 no começo do código. Sem esse passo, não teríamos controle do valor dessas variáveis, já que toda vez que uma variável é criada, ela não possui valor e não conseguimos fazer qualquer operação com uma variável sem valor.

Em seguida, vamos verificar se temos as duas notas para calcular a média do aluno:
```c
        if(nro_notas == 2) {
```
Se `nro_notas` for igual a 2 (`nro_notas == 2`), quer dizer que já temos as 2 notas do aluno para calcular a média. Para isso faremos a operação a seguir:
```c
          media = media/2;
```
Aqui basta dividir por 2 o valor da `media` porque nas etapas anteriores somamos o valor das notas à variável (`media = media + nota`).

Para apresentar o valor obtido, escrevemos o resultado na tela utilizando a função `printf`:
```c
          printf("media = %0.2lf\n", media);
          printf("novo calculo (1-sim 2-nao)\n");
```
`%0.2lf` será substituido pelo valor contido em media. O `0.2` indica quantas casas decimais serão mostradas na tela, que no caso é uma. O `\n` no fim serve para pular uma linha na tela depois de mostrar o dado. Além da resposta, também mostramos na tela a opção de fazer um novo cálculo e dar continuidade ao programa.

Para saber se teremos um novo cálculo ou não, vamos criar outro `while(1)`, pois também precisamos verificar se a resposta para um novo cálculo é válida ou não. Dentro do laço vamos ler a variável `x`: 
```c
          while(1) {
            scanf("%d",&x);
```
Aqui as únicas respostas que podem ser aceitas são 1 ou 2. Qualquer outra deve resultar na repetição da pergunta. Temos que usar novamente a função `if` e `else` para verificar a resposta dada. No `if`, se `x` for igual a 1 (`x == 1`), significa que um novo cálculo vai ser feito. Para iniciar um novo cálculo, temos que igualar as variáveis `media` e `nro_notas` a 0 de novo e o código descrito acima irá se repetir. O `break` é um comando de parada que faz o código voltar ao começo do primeiro `while(1)` mais rápido:
```c
            if(x == 1) {
              media = 0;
              nro_notas = 0;
              break;
            }
```
Se a resposta obtida for 2 (`x == 2`), significa que um novo cálculo não será feito e o programa será encerrado. Para encerrar o programa usamos a função `return 0;`:
```c
            else if(x == 2)
              return 0;
```
Se a resposta presente em `x` não for válida, a pergunta vai aparecer novamente na tela e a variável será lida de novo:
```c
            else
              printf("novo calculo (1-sim 2-nao)\n");
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre operadores lógicos: [Operadores](http://linguagemc.com.br/operadores-logicos-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre a função break: [Break](http://linguagemc.com.br/o-comando-break/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
