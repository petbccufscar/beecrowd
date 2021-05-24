# Problema:

O Kage Bunshin no Jutsu (ou a "técnica dos clones de sombra", para os lusofalantes) é uma técnica milenar bastante utilizada em batalhas ninja.

Quando utilizada, a técnica cria uma cópia idêntica de seu usuário. Desta forma, se um dado ninja usa a técnica, passam a existir dois destes ninjas (o original e a cópia).

A técnica sempre é executada por todos os ninjas existentes no momento. Desta forma, se a técnica for utilizada novamente, passam a existir quatro ninjas idênticos ao original (os dois anteriores e mais duas cópias), e assim por diante.

Há N cópias de um dado ninja (incluindo o original). Sua tarefa é determinar quantas vezes a técnica foi utilizada.


**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2544

# Resoluçāo:

Os números de ninja deste exercício são resultados de um expoente da base 2, e queremos achar o expoente em que ao ser elevado a 2 nos mostra a quantidade de vezes que a técnica foi utilizada. Para isso, é preciso calcular o [logaritmo](https://www.todamateria.com.br/logaritmo/) do número da entrada na base 2.

Primeiramente, é necessário declarar a biblioteca `math.h`, pois precisaremos trabalhar com uma função que calcula o logaritmo de num número na base 2.
```c
    #include<math.h>
```

Iremos declarar as variáveis que serão utilizadas neste problema.

```c
    int  x;
    long long int num;
```

O inteiro `x` armazenará o número de vezes que a técnica foi utilizada. Já `num` é o número de cópias de ninjas, ele é declarado como `long long int` pois a entrada pode ter números de tamanho que é superior ao que o tipo `int` consegue armazenar.

A partir disso, iremos ler `num`, como dito no exercício a entrada termina com `EOF`, por isso usaremos para ler até chegar ao final do arquivo.
 
```c
while (scanf("%lld", &num)!=EOF)
    {
        if (num==1) 
            printf("0\n");
        else{
            x = log2(num);
            printf("%d\n", x);       
        }
    }
```
A cada iteração verificamos, se `num` é igual 1 em caso afirmativo, a técnica ainda não foi usada, então imprimimos 0 na tela. Se não calculamos o logaritmo de `num` na base 2, utilizando a função `log2` da biblioteca `math.h`, que receberá `num` e retornará o resultado na variável `x`.

##### Para aprender um pouco mais sobre Loops: [Loops](https://sites.google.com/site/itabits/treinamento/introducao-a-programacao-em-c/comandos-de-repeticao)
##### Para aprender um pouco mais sobre a biblioteca `Math.h`: [`Math.h`](http://linguagemc.com.br/a-biblioteca-math-h/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
