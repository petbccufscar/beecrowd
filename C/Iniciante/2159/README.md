# Problema:
Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos até n, para n ≥ 17. Esta quantidade é representada pela função (n) e a fórmula é mostrada abaixo.

<img src="https://resources.urionlinejudge.com.br/gallery/images/contests/931.png" />

Sua tarefa é, dado um natural n, calcular o mínimo e máximo do intervalo para o número aproximado de primos até n.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2159
 
 
# Resolução:
 
Para calcular o mínimo e máximo do intervalo para o número aproximado de primos até `n`, iremos importar a biblioteca `math.h` para utilizarmos a função `log()` e declarar uma variável `n`, do tipo `double`.
 
```c
double n ;
```

Em seguida, lemos `n`.

```c
scanf("%lf", &n);
```

Em seguida, vamos calcular e exibir o resultado, com uma casa decimal após a vírgula, obtido por substituição direta na fórmula fornecida pelo problema, utilizando a função `printf()` a seguir.

```c
printf("%.1lf %.1lf\n", n/log(n), (1.25506)*(n/log(n)));
```
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com