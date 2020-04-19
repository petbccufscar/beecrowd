# Problema:

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela.

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

## Entrada

A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

## Saída

Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme o exemplo.

# Resolução:

Para resolver o exercício precisamos criar 3 variáveis, sendo duas do tipo flutuante e uma do tipo inteiro:
```c
        float salario, reajuste;
        int pct;
```
No enunciado do problema, está escrito para ler o salário, imprimir o novo salário, reajuste e percentual ganho(pct).

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler as variáveis, usa-se scanf:
```c
        scanf("%f", &salario);
```
Para ler um valor flutuante é utilizado um %f. Durante a execução do programa, usamos . para separar o valor decimal do inteiro.

Agora verificaremos qual será o percentual de reajuste de acordo com o salário dado. O aumento é de 15% se o salário é menor ou igual a 400, de 12% se o salário está entre 400.01 e 800, de 10% se o salário está entre 800.01 e 1200, de 7% se o salário está entre 1200.01 e 2000, e de 4% se o salário for maior que 2000:
```c
        if (salario <= 400)
            pct = 15;
        else if (salario <= 800)
            pct = 12;
        else if (salario <= 1200)
            pct = 10;
        else if (salario <= 2000)
            pct = 7;
        else
            pct = 4;
```
Para facilitar as comparações numéricas, usamos "else if" para representar que tal comparação só será feita se as comparações anteriores forem falsas.

##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Como sabemos a porcentagem de reajuste, é preciso calcular quanto será ganho de reajuste. Para isso calculamos o salário pela porcentagem e dividimos por 100:
```c
        reajuste = salario * pct / 100;
```
Em seguida, precisamos calcular o novo salário somando o reajuste ao salário antigo:
```c
        salario = salario + reajuste;
```
Aqui é utilizado a variável salario em ambos os lados, isso é realizado para atualizar a variável, já que o valor antigo não será mais necessário para concluir o exercício.

E por fim, escrevemos o resultado na tela utilizando a função printf:
```c
        printf("Novo salario: %0.2f\nReajuste ganho: %0.2f\nEm percentual: %d %%\n", salario, reajuste, pct);
```
O primeiro %0.2f será substituído pelo valor contido em salario. O segundo %0.2f será substituído pelo valor contido em reajuste. O 0.2 indica quantas casas decimais serão mostradas na tela, que no caso são duas. O %d representa o percentual de reajuste ganho. O \n presente na linha serve para pular uma linha na tela depois de mostrar o dado. Para poder escrever "%" na tela é preciso escrever %% para que não seja confundido com os % usados para escrita de dados. Sendo assim irá mostrar na tela:
```c
        Novo salario: 0.00
        Reajuste ganho: 0.00
        Em percentual: 0 %        
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

###### Todas as funções utilizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
