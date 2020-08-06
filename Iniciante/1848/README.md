# Problema:

 A sua tarefa é fazer um programa para interpretar o sonho de Bran e calcular o resultado da loteria.

Durante o sonho, o corvo pisca diversas vezes e grita apenas 3 vezes. A cada grito um número do resultado da loteria é calculado.

Cada piscada do corvo comunica um número em binário. Um olho aberto significa 1 e um olho fechado significa 0. O olho da esquerda é o mais significativo e o da direita é o menos significativo. A cada piscada, este número deve ser somado, e quando o corvo grita, essa soma é um resultado.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1848

# Resolução:
Para resolvermos o problema iremos verificar cada linha de entrada, e exibiremos a soma das piscadas do corvo depois de cada uma das 3 vezes que o ele gritar.

Para iniciar, iremos representar o grito ou as piscadas, a quantide de gritos e a soma das picasdas do corvo declarando as seguintes variaveis:
```c
char entrada[10]; // grito ou piscadas
int grito = 3, piscada = 0; //quantidade de gritos e soma das piscadas
```

* As variaveis ja foram inicializadas na declaração, pois elas vão/podem ser utilizadas no código sem uma operação prévia para definir seu valor.

Depois iniciamos um laço `while` que irá parar após as 3 vezes que o corvo gritar, ou seja, quando o valor da variável grito for igual a 0(falso). 
```c
while(grito){
	/*
	restante do código omitido.
	*/
}
```

Recebemos o grito ou a sequencia de piscadas do corvo com o comando `fgets`, que é similar ao comando `scanf`, com a diferença que pode receber espaços em branco. O que é necessário para ler o grito(caw caw) e não causar conflito na proxima leitura.
```c
	fgets(entrada, sizeof(entrada), stdin);
```

Agora podemos começar o sorteio dentro do laço `while`, primeiro verificamos se o corvo gritou analisando se a primeira linha de entrada é 'c' (inicio do grito 'caw caw'):
```c
	if(entrada[0]=='c'){
		printf("%d\n", piscada);
		piscada = 0;
		grito--;
	}
```
* Se o corvo gritou imprimimos a soma do sorteio, reiniciamos essa soma e a contagem de gritos descresce em 1.

Se o corvo piscou, verificamos cada um dos 3 olhos começando pelo mais a esquerda, se ele estiver aberto(*) somamos o valor da variável piscada de acordo com o binario a posição do olho representa.
```c
else{
	 if(entrada[0] == '*')
		piscada += 4;
	if(entrada[1] == '*')
		piscada += 2;
	if(entrada[2] == '*')
		piscada += 1;
}
```
Com isso, após o terceiro grito do corvo o sorteio é encerrado. 

##### Para aprender um pouco mais sobre números binários: [Binarios](https://brasilescola.uol.com.br/matematica/sistema-numeracao-binaria.htm)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com