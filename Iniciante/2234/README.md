# Problema:
Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

O restaurante Nathan’s Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. Eles produzem deliciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não são tão bons. Eles desejam ser listados no Livro de Recordes do Guinness, mas para isso devem preencher um formulário descrevendo os fatos básicos da competição. Em particular, eles devem informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.

Você pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos cachorros-quentes. Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição, você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2234


# Resolução:
Para a resolução deste exercício, basta que realizemos a divisão destes dois valores fornecidos para obtermos a média de consumo.  

Primeiramente, declaramos as variáveis `H` e `P` do tipo inteiro, como solicitado pelo enunciado, para armazenarem a quantidade de cachorros-quentes e de participantes. Além disso, a variável de ponto flutuante, `media`, é importante para guardar o resultado obtido.  

```c
int H, P;
float media;
```  

Em seguida, efetuamos a leitura dos dados utilizando a função `scanf()`.  

```c
scanf("%d %d",&H, &P);
```  

Tendo conhecimento de tais valores, podemos, então, realizar o cálculo que define a média de cachorros-quentes consumidos. Este consiste em dividir a quantia consumida pelo número de competidores. Em virtude destes dados terem sido declarados como inteiros enquanto o resultado corresponde a um número racional, é fundamental aplicarmos o operador cast `(float)` para que a conta possa ser efetuada corretamente. Desse modo, realizamos a conversão da solução obtida em `int` para o tipo `float`, armazenando-a na variável `media` que será exibida na tela.  

```c
media = (float) H/P;

printf("%.2f\n",media);
```

##### Para aprender um pouco mais sobre operador cast: [Operador cast](https://www.vivaolinux.com.br/dica/Operador-cast)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
