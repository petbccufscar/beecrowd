# Problema:

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela.

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

# Resolução:

Com base na tabela presente no problema, a ideia do exercício é verificar em qual situação da tabela o empregado se encaixa de acordo com seu salário e, com isso, saber o quanto vai aumentar após o reajuste e qual será o novo salário desse funcionário.

Para resolver o exercício precisamos criar 3 variáveis, sendo duas do tipo _float_ e uma do tipo _int_:
```c
        float salario, reajuste;
        int pct;
```
No enunciado do problema, está escrito para ler o salário, imprimir o novo salário, reajuste e percentual ganho(_pct_).

Para ler as variáveis, usa-se _scanf_:
```c
        scanf("%f", &salario);
```
Para ler um valor _float_ é utilizado um %f. Durante a execução do programa, usamos . para separar o valor decimal do inteiro.

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
Para facilitar as comparações numéricas, usamos _else if_ para representar que tal comparação só será feita se as comparações anteriores forem falsas.

Como sabemos a porcentagem de reajuste (_pct_), é preciso calcular quanto será ganho de reajuste. Para isso calculamos o salário pela porcentagem e dividimos por 100:
```c
        reajuste = salario * pct / 100;
```
Em seguida, precisamos calcular o novo salário somando o _reajuste_ ao salário antigo:
```c
        salario = salario + reajuste;
```
Aqui é utilizado a variável _salario_ em ambos os lados, isso é realizado para atualizar a variável, já que o valor antigo não será mais necessário para concluir o exercício.

E por fim, escrevemos o resultado na tela utilizando a função _printf_:
```c
        printf("Novo salario: %0.2f\nReajuste ganho: %0.2f\nEm percentual: %d %%\n", salario, reajuste, pct);
```
O primeiro %0.2f será substituído pelo valor contido em _salario_. O segundo %0.2f será substituído pelo valor contido em _reajuste_. O 0.2 indica quantas casas decimais serão mostradas na tela, que no caso são duas. O %d representa o percentual de reajuste ganho. O \n presente na linha serve para pular uma linha na tela depois de mostrar o dado. Para poder escrever "%" na tela é preciso escrever %% para que não seja confundido com os % usados para escrita de dados. Sendo assim irá mostrar na tela:
```c
        Novo salario: 0.00
        Reajuste ganho: 0.00
        Em percentual: 0 %        
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
