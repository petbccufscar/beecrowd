# Problema:

Por exemplo, se N = 2. A sequência correta seria 0 1 2 2, obtendo-se 4 digitos. Agora, se N = 3, o próximo número da sequência tem valor 3, então a quantidade total de número da sequência seria a quantidade de números com N = 2, que é 4, mais o valor do próximo número da sequência, neste caso 3, obtendo-se 7, já que a sequência correta para N = 3 é 0 1 2 2 3 3 3.

Sua tarefa é fazer um algoritmo que dado um número inteiro N, tenha como resposta a quantidade total de números dessa sequência e logo abaixo a sequência completa.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2028

# Resolução:

Para resolver esse problema, iremos receber um número N diversas vezes e, para cada número N, exibiremos a sequência de acordo com esse número. Por exemplo, se recebermos o número 3 exibiremos a sequência: 0 1 2 2 3 3 3.

Para começar, iremos declarar as variáveis. Teremos a que receberá o número N (`numero`), a variável que será o contador de cada caso (`caso`), a que exibirá a quantidade de números da sequência (`quantNumeros`) e as variáveis i e j, que irão iterar pelo laço de repetição `for`. Iniciamos a váriavel `caso` em 0, pois ela será incrementada, posteriormente, para cada número N testado.
```c
int i, j, numero, caso, quantNumeros;

caso = 0;
``` 

Depois, iniciamos o laço de repetição `while`, onde iremos receber um número N e exibir a sequência e a quantidade de números dessa sequência. Também, mostraremos um número de caso para cada vez que recebermos um número N. A condição de parada do laço possui o comando `scanf`, que fará a leitura da variável `numero` até que receba o [final de arquivo(EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição.
```c
while(scanf("%d", &numero)!= EOF){
``` 

Então, dentro do laço `while` iniciamos a variável `quantNumeros`, pois ela é calculada para cada número N que será testado, acrescentamos +1 para a variável caso. Assim, calculamos a quantidade de números que a sequência referente ao número N irá possuir (descrito de forma dissertativa no enunciado do problema).   
```c
quantNumeros = 1;
caso++;

quantNumeros += ((numero*(numero+1))/2);
``` 

Para podermos exibir a sequência, verificamos se o número N recebido é *igual* a 0. Se sim, exibimos a frase de saída no singular, caso contrário exibimos no plural.
```c
if(numero == 0)
	printf("Caso %d: %d numero\n", caso, quantNumeros);
else
	printf("Caso %d: %d numeros\n", caso, quantNumeros);
```

Com isso, podemos finalizar exibindo a sequência, que é iniciada com o 0. Utilizamos dois laços `for` de forma que o primeiro laço com a variável `i` vai guardar o número a ser exibido e o segundo laço com `j` irá mostrar esse número i vezes.
Por exemplo, se i=2, então o segundo `for` irá escrever: 2 2.
```c
for(i=1;i<=numero;i++){
	for(j=1; j<=i; j++)
		printf(" %d", i);
}
```

##### Para aprender um pouco mais sobre final de arquivo (EOF): [EOF](https://pt.wikipedia.org/wiki/EOF)

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com