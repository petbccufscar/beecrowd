# Problema

Timelimit: 1
Raul Seixas cantava que nasceu há 10 mil anos atrás e não tinha nada nesse mundo que ele não sabia demais. Os Mamomas Assassinas cantavam que mais de 10 mil anos "se passaram-se" [sic] quando eles repetiram a 5a série. Tantos eventos passados e o professor MC ficou curioso para saber em que ano tudo isso aconteceu.

Você deve escrever um programa que, dada uma série de número de anos transcorridos, mostre, para cada número, em que ano o evento aconteceu. Lembre-se de indicar se ele aconteceu A.C. (Antes de Cristo) ou D.C. (Depois de Cristo).


**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1962

# Resolução

Apesar do enunciado um tanto confuso, o exercício nos pede para, dado um número inteiro `T` retornemos o ano referente a 2015 - `T`, não esquecendo de informar se é A.C. ou D.C.

Nesse exercício, utilizamos a biblioteca `<stdlib.h>` para fazer uso da função `abs()` que retorna o valor absoluto (positivo) do que for passado como argumento (ex: abs(-3) = 3).

Começamos com a declaração de variáveis, `N` será quantos inteiros `T` receberemos, que por sua vez, é a quantidade de anos que iremos voltar partindo de 2015. `antes` é uma variável auxiliar, que determinará se estamos em um ano antes ou depois de cristo com um valor lógico, 1 para A.C. (_true_) ou 0 para D.C. (_false_)

```c
    int N, T, antes, i;
```

Assim, com as variáveis declaradas, podemos fazer a leitura de quantos `T` receberemos.

```c
    scanf("%d",&N);
``` 

Com essa lacuna preenchida, faremos um loop `for` de 0 a `N` (que não inclui `N`) para ler os valores de `T` e efetuar os cálculos, que são divididos em 2 passos.
* Verificamos se estamos com um valor de 2015 - `T` positivo, que indicará que a apresentação deve ser D.C. Caso seja negativo, então a apresentação é A.C
    * Caso a condição seja satisfeita, estamos lidando com um valor A.C. o que entra no quadro de um ano "negativo", portanto a variável `antes` se torna 1 (_true_)
    * Caso a condição não seja satisfeita, no `else` atribuimos `antes = 0` que nos guia a apresentação D.C.
* Após essa confirmação do valor lógico da variável `antes`, entramos em outra estrutura de decisão `if(antes)` que será o caso de `antes == 1`.
    * Caso o valor de `antes` seja 1, ou seja, Antes de Criso, escrevemos na tela o resultado absoluto de (2015 - `T`+1), utilizamos `T`+1 pois quando se trata de anos A.C. o ano 0 nunca existiu, portanto é representado como 1 A.C. (exemplo: 2015 anos antes de 2015 nos leva a 1A.C. e não no ano 0).
    * Caso o valor de `antes` seja 0, ou seja, Depois de Cristo, precisamos apenas escrever na tela o resultado de (2015 - `T`) pois por se tratar de um ano D.C. não precisaremos do valor absoluto, essa subtração sempre será positiva.


```c
   for(i=0;i<N;i++){
        scanf("%d",&T);
        if((2015-T) <= 0){
            antes = 1;
        }
        else{
            antes = 0;
        }
        if(antes){
            printf("%d A.C.\n",abs(2015-(T+1)));
        }
        else{
            printf("%d D.C.\n",(2015-T));
        }
    }
```


#### Revise sobre estruturas de decisão aqui: [If/else](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/#:~:text=Uma%20estrutura%20de%20decis%C3%A3o%20examina,estrutura%20de%20decis%C3%A3o%20muito%20utilizada.&text=Elaborar%20um%20programa%20em%20linguagem,valor%20da%20soma%20na%20tela.)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
