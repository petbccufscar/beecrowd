# Problema:

A fórmula de Binet é uma forma de calcular números de Fibonacci.

![Fibonacci](https://resources.urionlinejudge.com.br/gallery/images/contests/944.png)

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2164

# Resolução

O exercício em suma é transcrever essa fórmula para o código.

Como a fórmula matemática apresenta muitas funções tais como raíz quadrada e exponencial, precisamos utilizar a biblioteca math para facilitar nossa vida:

```c
        #include <math.h>
```

Iniciamos declarando as variáveis que serão utilizadas:

```c
        double part1, part2, part3, potencia1, potencia2;
        double n;
```
A excolha do tipo `double` é devido as funções da `math.h` muita das vezes aceitar só esse tipo de variável e também o exercício te limita a apenas utilizar números naturais, portanto não negativo. `part1, part2, part3, potencia1, potencia2` são variáveis que foram criadas apenas para facilitar o entendimento do exercíco, elas serão usadas para repartir em etapas a função dada acima e `n` é o número do caso que ele deseja verificar o resultado.

Fazemos a leitura de `n` usando `scanf`:

```c
        scanf("%lf", &n);
```

Cada parte da função matemática transcrita segue separada, sendo a `part3` a junção final. `sqrt` é a função que calcula a raíz quadrada e `pow` é usado para calcular potência x^y.

```c
        part1 = (1+sqrt(5))/2;
        part2 = (1-sqrt(5))/2;
        potencia1 = pow(part1, n);
        potencia2 = pow(part2, n);
        part3 = ((potencia1 - potencia2)/sqrt(5));
```
Finalizamos printando o resultado da expressão, observe que a saída exigida pelo Uri possui apenas uma casa após a vírgula e para garantirmos isso usamos `.1lf`:

```c
        printf("%.1lf\n", part3); 
```

##### Para aprender um pouco mais sobre a biblioteca math.h: [Math.h](http://linguagemc.com.br/a-biblioteca-math-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com