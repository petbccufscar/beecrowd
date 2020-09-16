# Problema:   
Após uma aula muito boa de história - sucedendo uma aula muito ruim de matemática - alguns alunos de uma determinada escola estão com dúvidas em um simples problema. A professora pediu que eles informassem o valor numérico (por simplicidade deve ser em decimal e em algarismos arábicos) do século de um determinado ano, mas como poucos alunos estavam acertando ela decidiu pedir sua ajuda para criar um programa que fizesse exatamente isso a fins educativos.

Para quem não se lembra desta aula de história, o século 1, por exemplo, compreende os anos entre 1 e 100, o século 2 os anos entre 101 e 200, o século 3 os anos entre 201 e 300 e assim por diante.  

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3076

# Resolução:

Para a resolução deste problema iniciaremos incluindo a biblioteca `math.h` pois ela possui a função `ceil` que, quando usada, caso o valor seja um numero com casas decimais, ela arredonda este valor para cima, por exemplo caso tivermos um valor "1.1" e usarmos a função `ceil`, teremos como resultado o valor "2". 
```c
#include <math.h>
```

Declaramos a variável que iremos realizar a leitura do ano que será passado para calcularmos a qual seculo este pertence, para isso iremos declarar um variável `ano` do tipo `double` pois iremos realizar divisões com casas decimais
```c
double ano;
```

Após declarada a variável em que será armazenada o ano que será passado, iremos realizar a leitura, para isso enquanto não acabar os casos de testes iremos continuar lendo através da função `scanf`, para isso iremos utilizar o parâmetro `~scanf("%lf", &ano)` dentro de nosso laço de repetição `while`. Essa operação é igual a `while (scanf("%lf", &ano) != EOF)` onde buscamos pelo final do arquivo para encerrar o laço de repetição
```c
while (~scanf("%lf", &ano)){
	...
}
```

Por final, a cada iteração de nosso laço de repetição, já com o valor lido, realizamo a divisão deste por "100.0" e o resultado usamos como parâmetro na função `ceil` que foi incluída no inicio de nosso programa através da biblioteca `math.h`, com isso teremos como resultado o valor da divisão acrescentado de "1", fazemos isso pois o século 1 vai do ano 0 até 99. Ao imprimir o valor final utilizamos `%.lf` para imprimir um valor sem casas decimais, apenas o inteiro.
```c
printf("%.lf\n", ceil(ano / 100.0));
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com