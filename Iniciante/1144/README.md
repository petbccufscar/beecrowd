# Problema:
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.


**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1144


# Resolução:
O exercício resume-se a decifrar a relação (ou padrão) entre a entrada e saída exemplificada e, então, ler um valor inteiro N e reproduzir tal padrão N vezes.

Analisando os valores fornecidos (entrada x saída), é possível notar que, sendo `i` um valor inteiro, o padrão de saída é composto por duas linhas:

`i i² i³`
`i i²+1 i³+1`

Sendo o valor inicial de `i = 1` e, ao fim de cada 2 linhas, `i` é acrescido em 1. 
Por conta do padrão conter potências, iremos importar a biblioteca `math.h`, para utilizarmos a função de potência `pow(base, expoente)`.

Para realizar isso, depois de importar a bibliotaca `math.h`, declara-se as variáveis inteiras `N`, `i`. Além disso, declara-se também duas variáveis inteiras `num1` e `num2`, pois o retorno da função matemática `pow()` é do tipo `double` e, como o enunciado exige que o número apresentado na tela seja inteiro e não decimal, é preciso converter o valor de double para inteiro. 

```c
int N;
int i;
int num1;
int num2;
```
Em seguida, lê-se o valor de `N`, por meio da função `scanf()`.

```c
scanf("%d",&N);
```

Em seguida, vamos utilizar a estrutura de repetição `for` para reproduzir N linhas de saída, conforme o padrão decifrado.

A cada iteração do laço de repetição:
- Calculamos `i²`, `i³` e armazenamos o resultado em `num1` e `num2`;
- Exibimos os valores `i num1 num2`;
- Exibimos os valores `i num1+1 num2+1`;
- Incrementamos o valor de `i` através do laço `for` (ao fim de cada iteração do laço).

```c
for(i = 1; i <= N; i++)	{
    num1 = pow(i,2);
    num2 = pow(i,3); 
    printf("%d %d %d \n", i, num1, num2);
    printf("%d %d %d\n", i, num1 + 1, num2 + 1);
  }
```

##### Para revisar a função pow(): [pow, powf, powl](https://docs.microsoft.com/pt-br/cpp/c-runtime-library/reference/pow-powf-powl?view=vs-2019)
##### Para aprender um pouco mais sobre a estrutura for: [O que é e como usar o laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
