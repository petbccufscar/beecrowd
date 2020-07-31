# Problema:    
Mariazinha quer resolver um problema interessante. Dadas as informações de população e a taxa de crescimento de duas cidades quaisquer (A e B), ela gostaria de saber quantos anos levará para que a cidade menor (sempre é a cidade A) ultrapasse a cidade B em população. Claro que ela quer saber apenas para as cidades cuja taxa de crescimento da cidade A é maior do que a taxa de crescimento da cidade B, portanto, previamente já separou para você apenas os casos de teste que tem a taxa de crescimento maior para a cidade A. Sua tarefa é construir um programa que apresente o tempo em anos para cada caso de teste.

Porém, em alguns casos o tempo pode ser muito grande, e Mariazinha não se interessa em saber exatamente o tempo para estes casos. Basta que você informe, nesta situação, a mensagem "Mais de 1 seculo.".

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1160


# Resolução:

Declaramos algumas variaveis que serão importantes durante a resolução do problema, respectivamente, `contador` utilizado dentro `for`, `T` que irá armazenar o número de casos de teste, `PA` e `PB` que receberão as populações das cidades A e B, e `anos` para armazenar a o tempo final necessário para que `PA` se torne maior que `PB`. Em seguida declaramos duas variaveis `G1` e `G2` do tipo `double` que irão receber os valores da taxa de crescimentos das cidades A e B respectivamente.
```c
int contador, T, PA, PB, anos;
double G1, G2;
```

Realizamos a primeira leitura, responsavel por determinar quantas iterações nosso programa irá realizar.
```c
scanf("%d", &T);
```

Iniciamos a nossa estrutura `for`, para cada iteração iremos realizar a leitura da população de A e B, juntamente com suas respectivas taxas de crescimento. Iniciamos a variavel `anos` com valor 0 em cada iteração pois iremos utiliza-la para contar o tempo que será necessário para que `PA` seja maior que `PB` a cada iteração.
```c
for(contador=0; contador<T; contador++){
  scanf("%d %d %lf %lf", &PA, &PB, &G1, &G2);
  anos = 0;
```

Tranformamos a taxa de crescimento `G1` e `G2` para sua forma em porcentagem, fazendo com que o código não repita a mesma operação no próximo laço de repetição, onde é usado a estrutura `while`
```c
G1 = (G1 / 100.0) + 1.0;
G2 = (G2 / 100.0) + 1.0;
```

Dentro da estrutura `while` definimos que enquanto `PA <= PB` será realizada a multiplicação entre a cidade e sua respectiva taxa de crescimento, armazenando o valor final na própria variável, o que faz com que na próxima iteração do laço `while` a multiplicação seja realizada com o valor atualizado. A cada repetição incrementamos a variável `anos` para ter um controle sobre o tempo que irá demorar
```c
while(PA <= PB){
  PA *= G1;
  PB *= G2;
  anos++;
```

Durante o `while` é feito a verificação para garantir que não demore muito tempo, assim como é proposto pelo problema, dessa forma, quando anos atinge um valor maior que "100", saimos do laço e imprimimos que o tempo necessário para que a população da cidade A seja maior que a população da cidade B será mais que 1 século.
```c
if (anos > 100){
  printf("Mais de 1 seculo.\n");
  break;
}
```

Caso não tenha estourado o limite de tempo, ao final do laço realizamos a impressão, retornando o valor, armazenado em `anos`, correspondente a quanto tempo levará para que a população da cidade A seja maior que a população da cidade B.
```c
if (anos <= 100)
	printf("%d anos.\n", anos);	
```

##### Para revisar sobre: [Operadores em C](http://linguagemc.com.br/operadores/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
