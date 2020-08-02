# Problema:

Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

# Resolução:

No problema está descrito para ler 3 valores: 2 valores inteiros, número que identifica o funcionário e horas trabalhadas, respectivamente; e 1 valor com duas casas decimais que representa o valor que o funcionário recebe por hora. Para representar esses valores em nosso programa, fazemos: 

```c
    int numero, horasTrabalhadas;
    float valorPorHora;
````

Para leitura dos valores, usamos a função `scanf`:

````c
    scanf("%d %d %f", &numero, &horasTrabalhadas, &valorPorHora);
````

Utilizamos `%d` para os valores inteiros e `%f` para o valor que tem casas decimais. 

Com o `scanf` é possível ler mais de um valor, cada `%`(tipodavariavel) representa um valor a ser lido. Os valores lidos serão atribuídos às varíaveis que aparecem depois das "", na respectiva ordem.    

Agora apresentamos na tela o numero da forma que foi especificada no enunciado do problema com a função printf:

```c
    printf("NUMBER = %d\n", numero);
```

E por fim, apresentamos também o salário, que é calculado através do produto das horas trabalhadas e o valor recebido por hora. 

```c
    printf("SALARY = U$ %.2f\n", horasTrabalhadas*valorPorHora);
```

Usamos `%.2f` pois queremos apresentar o valor com duas casas decimais, caso fossem três casas decimais seria `%.3f` e assim por diante. Note que é possível realizar o cálculo dentro do `printf`.


###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com