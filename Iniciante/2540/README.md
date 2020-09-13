# Problema:
Analógimôn Go! é um jogo bastante popular. Os jogadores são divididos em três grandes times: Valor, Instinto e Místico. Naturalmente, você faz parte de um desses times!

O líder do seu time está sendo acusado de infringir as regras do jogo por gerenciar incorretamente os doces recebidos do Professor que são destinados ao time. Isto criou uma grande polêmica dentro da equipe: alguns jogadores defendem que o líder realmente agiu incorretamente e deve sofrer um impeachment e ser afastado de seu cargo, enquanto outros defendem que ele não infringiu as regras, que a acusação é inverídica e que ele deve continuar no cargo.

Para resolver a situação, uma votação será realizada entre todos os N jogadores do seu time. Cada jogador deverá votar se o impeachment deve ou não ocorrer. Se o número de votos favoráveis ao impeachment foi maior ou igual a 2/3 (dois terços) do total de jogadores, o líder será afastado. Caso contrário, a acusação é arquivada e ele continuará no cargo.
Dados os votos de todos os jogadores, determine o resultado da votação.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2540
 
# Resolução:
 
O exercício consiste em ler o número de jogadores depois seus respectivos votos e ficar repetindo isso até que acabe as votações.
 
Primeiro definimos as variáveis necessárias, sendo elas: 4 `int` (`i` para o `for()` que será utilizado; `N` para o número de jogadores; `v` para ler o voto, sendo `1` a favor e `0` contra; e `soma` para somar os votos).
 
```c
           	int N, v, i, soma;
```
 
Utilizaremos um `while()` para ler o número de jogadores e verificar se chegamos ao final de todos os casos (sendo ele quando for lido o `EOF`). Lembrando de definir a soma como `0` pois estamos começando uma nova votação.
 
```c
	while (scanf("%i", &N) != EOF){
    	soma = 0;
 
    	//code
	}
```
 
Dentro do `while()` utilizaremos um `for()` para ler os votos dos jogadores (tendo em vista que o número de jogadores já foi definido no `scanf` do `while`) e adicionar eles a `soma`.
 
```c
	for (i = 0; i < N; i++)
    	{
            scanf("%i", &v);
        	soma += v;
    	}
```
 
Depois de ler todos os votos vamos verificar se o número de votos favoráveis foi maior ou igual a 2/3 de todos os jogadores, em outras palavras o valor de `soma` deve ser maior ou igual ao número de jogadores dividido por 2/3, sendo que esse deve ser tratado como um `float`, para fazer essa divisão de forma fácil basta inverter o divisor com o dividendo e ao invés de dividir vamos multiplicar. Assim a expressão fica da seguinte forma: `N / (3 * 1.0f) * 2`, para transformar um `int` em um `float` basta multiplica ele por `1.0f`.

##### Exemplo:

![imagem](https://www.wikihow.com/images/thumb/6/68/Divide-Fractions-by-a-Whole-Number-Step-3-Version-3.jpg/v4-728px-Divide-Fractions-by-a-Whole-Number-Step-3-Version-3.jpg.webp)


Com o resultado imprimimos se houve impeachment ou se a acusação foi arquivada.
 
```c
if(soma >= (N / (3 * 1.0f)) * 2){
            printf("impeachment\n");
    	}else{
            printf("acusacao arquivada\n");
    	}
```
 
 
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

