# Problema:  

Cinco patinhos foram passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, quá, quá. Mas só quatro patinhos voltaram de lá. Quatro patinhos foram passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, quá, quá. Mas só três patinhos voltaram de lá. Três patinhos foram passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, quá, quá. Mas só dois patinhos voltaram de lá. Dois patinhos foram passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, quá, quá. Mas só um patinho voltou de lá. Um patinho foi passear. Além das montanhas. Para brincar. A mamãe gritou: quá, quá, quá, quá. Mas nenhum patinho voltou de lá.

A mamãe patinha ficou tão triste naquele dia que resolveu pedir sua ajuda para procurar além das montanhas, na beira do mar, quantos patinhos não voltaram de lá.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2334

# Resolução:

Neste problema haverá vários casos de testes, a primeira linha de cada caso de teste contém um inteiro representando a quantidade total de patos, a saída por sua vez deverá conter a quantidade de patinhos que retornaram, o qual será sempre 1 a menos do que a quantidade inicial (exceto pelos casos que iremos tratar).

Iniciamos declarando a variável que irá armazenar a quantidade inicial de patinhos. Declaramos como long double pois dentro dos casos de testes existem valores maiores do que aqueles que uma variável do tipo inteiro suporta.
```c
long double qntPatinhos;
```


Iremos utilizar a estrutura `while` como o valor "1" para que fique em loop enquantos não obter como entrada o valor "-1".
```c
while (1){
	scanf("%LF", &qntPatinhos);
```


Dentro de nossa estrutura de repetição faremos a verificação se foi recebido o valor "-1", caso positivo realizamos um `break` o que faz com que saia do laço `while`
```c
if (qntPatinhos == -1)
	break;
```


Se não tiver entrado na condição anterior, iremos fazer uma nova verificação, esta irá verificar se o valor de entrar é igual a zero, caso positivo imprimimos "0". Caso contrário iremos retornar o valor que foi inserido subtraido de 1 unidade.
```c
if (qntPatinhos == 0)
	printf("0\n");
else
	printf("%.LF\n", --qntPatinhos);
```

##### Para revisar sobre o laço de repetição [while](http://linguagemc.com.br/o-comando-while-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
