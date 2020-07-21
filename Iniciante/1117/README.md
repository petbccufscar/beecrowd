# Problema:

Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

# Resolução:

O enunciado do problema pede um programa que calcule a média entre duas notas, sendo que essas notas devem estar entre 0 e 10. Para isso você deve conferir se os dois valores escritos estão entre 0 e 10 antes de calcular a média.

Para começar o exercício, primeiro instanciamos três variáveis do tipo `double`, sendo duas delas as notas do aluno e a última o valor da média que será calculada:
```c
    double nota1, nota2, media;
```
Como está escrito no enunciado, iremos ler a primeira nota do aluno e verificar se é uma nota válida:
```c
    do {
        scanf("%lf", &nota1);
        if (nota1 < 0 || nota1 > 10)
            printf("nota invalida\n");
    } while (nota1 < 0 || nota1 > 10);
```
Para que seja possível escrever um novo valor caso o anterior seja inválido, fizemos um `do... while()` para criar um laço de repetição e dentro dos parênteses está a condição para que o processo se repita. No caso, está escrito `nota1 < 0 || nota1 > 10`, que significa que será preciso ler e verificar o dado de novo se a nota for menor que 0 ou maior que 10.

Dentro da repetição estamos lendo a variável `nota1` usando a função `scanf` e, em seguida, verificamos se o valor é menor que 0 ou maior que 10 usando a função `if`. Se a verificação for verdadeira, ele mostrará na tela a mensagem `nota invalida`.

A variável `nota2` passará pelo mesmo processo:
```c
    do {
        scanf("%lf", &nota2);
        if (nota2 < 0 || nota2 > 10)
            printf("nota invalida\n");
    } while (nota2 < 0 || nota1 > 10);
```
Caso as duas notas sejam válidas, resta apenas calcular a média do aluno e guardar o valor na variável `media`. A média do aluno será a soma das duas notas dividido por 2:
```c
    media = (nota1 + nota2)/2;
```
E por fim, escrevemos o resultado na tela utilizando a função `printf`:
```c
    printf("media = %0.2lf\n", media);
```
O `%lf` será substituído pelo valor contido em `media`,  o `0.2` indica quantas casas decimais serão mostradas na tela, que no caso são duas. O `\n` no fim serve para pular uma linha na tela depois de mostrar o dado.

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre operadores lógicos: [Operadores](http://linguagemc.com.br/operadores-logicos-em-c/)
##### Para aprender um pouco mais sobre a estrutura do.. while: [Do... While](http://linguagemc.com.br/comando-do-while/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
