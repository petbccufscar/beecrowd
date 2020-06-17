# Problema:

Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

# Resolução:

O problema pede 3 três notas, cada uma tem um peso específico para calcular a nota final. A ideia da resolução é multiplicar as notas A, B e C pelos seus pesos e depois dividir a soma dos resultados obtidos por 10.

Para ler três variáveis e inserir o resultado em uma quarta variável, é necessário criar quatro variáveis do tipo _double_, variável que representa um número real:
```c
        double a, b, c, media;
```
No enunciado do problema, está escrito para ler três valores _a_, _b_, e _c_ e para imprimir a variável _media_.

Para ler as três variáveis, usa-se _scanf_:
```c
        scanf("%lf%lf%lf", &a, &b, &c);
```
É possível inserir mais de um dado dentro do mesmo scanf usando vários %lf, que é utilizado para ler uma variável do tipo _double_. Durante a execução do programa, usamos . para separar o valor decimal do inteiro.

Em seguida, atribuímos o valor da média. O enunciado diz que a nota A tem peso 2, a B tem peso 3 e a C tem peso 5, sendo assim:
```c
        media = (2*a + 3*b + 5*c)/10;
```
Como a soma dos pesos resulta em 10, dividimos a soma das notas por 10 para obter a média ponderada.

E por fim, escrevemos o resultado na tela utilizando a função _printf_:
```c
        printf("MEDIA = %0.1lf\n", media);
```
%0.1lf será substituido pelo valor contido em _media_. O 0.1 indica quantas casas decimais serão mostradas na tela, que no caso é uma. O \n no fim serve para pular uma linha na tela depois de mostrar o dado.
##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
