# Problema:
O professor está te ensinando sobre sensores. Este é um elemento muito importante em diversas aplicações. Para aprender melhor os conceitos de precisão o professor pediu para realizar uma montagem prática do sensor Termo Ind v4.0 no novo laboratório de Automação.

Para realizar o teste você ficou H horas fazendo testes, e a cada M minutos você verificou o valor X da temperatura entregue pelo sensor. Faça um programa que entregue a precisão do sensor.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2774

# Resolução:

A ideia do exercício é que você mostre na tela o resultado da fórmula presente no enunciado com os dados obtidos.

Nesse exercício vamos declarar quatro variáveis do tipo `int`:
```c
  int H, M, QT, i;
```
`H` irá guardar o número de horas que você ficou fazendo testes. `M` é o intervalo em minutos entre cada teste, `QT` representa o número de testes feitos. `i` é uma variável auxiliar para o `for`.

Também precisaremos de cinco variáveis do tipo `double`:
```c
  double X[1000000], xMedio, soma, somatorio, sigma;
```
`X` é um vetor que representa os testes realizados. `xMedio` é valor que indica o valor médio dos testes feitos. `soma` e `somatorio` são variáveis que representam o numerador da fórmula, sendo `soma` o valor dentro do Σ e `somatorio` o resultado após o Σ. `sigma` é o resultado final da fórmula de precisão do sensor.

O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `H` e `M` no `scanf` dentro do `while`:
```c
  while (scanf("%d %d", &H, &M) != EOF) {
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`).

Agora, descobrimos quantos testes serão feitos e colocamos o valor em `QT`:
```c
    QT = (int)(H*60)/M;
```
Se sabemos que um teste será feito a cada `M` minutos e vamos ficar `H` horas fazendo os testes, então multiplicamos o número de horas por 60 e dividimos pelo tempo de intervalo para saber quantos testes foram feitos. O `(int)` converte o resultado da divisão do tipo `double` para o tipo `int`.

Para poder aplicar a fórmula, vamos usar `soma` e `somatorio`. Aqui igualamos elas a 0 para poder fazer os cálculos seguintes:
```c
    soma = 0;
    somatorio = 0;
```
Aqui criamos um `for` para repetição. Dentro dele lemos os testes feitos usando `scanf` e somamos o valor obtido à variável `soma`:
```c
    for (i = 0; i < QT; i++) {
      scanf("%lf", &X[i]);
      soma += X[i];
    }
```
Agora temos que descobrir o valor de xMedio. Esse valor será a média aritmética dos testes realizados:
```c
    xMedio = soma / QT; 
```
Vamos criar outro laço de repetição. Aqui começamos a calcular o numerador da fórmula descrita no enunciado:
```c
    for (i = 0; i < QT; i++) {
      soma = (X[i]-xMedio);
      soma *= soma;
      somatorio += soma;
    }
```
Na fórmula, subtraímos o valor do teste `X[i]` por `xMedio` (`X[i]-xMedio`), multiplicamos o resultado obtido por ele mesmo (`soma *= soma`) e somamos o valor a `somatorio`. Isso vai ser repetido para todos os testes.

Por fim, descobrimos o resultado da fórmula. `sigma` será a raíz quadrada da divisão entre `somatorio` e `QT - 1`:
```c
    sigma = sqrt((somatorio / (QT-1)));
```
A função `sqrt()` está presente na biblioteca [math.h](http://linguagemc.com.br/a-biblioteca-math-h/). Essa função vai obter a raìz quadrada do valor entre parênteses.

Agora que temos o resultado, precisamos mostrar esse valor na tela usando `printf`:
```c
    printf("%.5lf\n", sigma);
  }
```
Usamos `.5lf` para mostrar na tela apenas as primeiras 5 primeiras casas decimais na tela.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre double: [Tipos de dados](http://linguagemc.com.br/tipos-de-dados-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
