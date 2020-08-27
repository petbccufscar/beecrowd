# Problema:
System of a Download é uma famosa banda de Hacker Metal! Certa vez, eles criaram um dispositivo, com seis botões, numerados de 0 a 5, e colocaram nesse dispositivo os seus 11 maiores sucessos. Para tocar uma destas músicas, é preciso pressionar dois botões. Com isso, os números destes dois botões são somados, e então toca-se a música correspondente ao número da soma, conforme a relação abaixo:

0. PROXYCITY
1. P.Y.N.G.
2. DNSUEY!
3. SERVERS
4. HOST!
5. CRIPTONIZE
6. OFFLINE DAY
7. SALT
8. ANSWER!
9. RAR?
10. WIFI ANTENNAS

Escreva um programa que, dados os dois botões que forem pressionados, determine qual música irá tocar.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2582
 
# Resolução:
O exercício consiste em ler dois valores inteiros e com eles imprimir a música referente.

Primeiro instanciamos as variáveis necessárias, sendo elas: 4 `unsigned short` (`C` a quantidade de casos de teste; `X` e `Y` os valores dos botões; e `resultado` para a soma dos valores).
Começamos lendo a quantidade de casos de teste.

Obs: Como vamos ler um `unsigned short`, iremos ler utilizando `%hu`.

```c
	unsigned short C, X, Y, resultado;
	scanf("%hu", &C);
```
 
Agora iremos utilizar um `while(C--)` para passar por todas as músicas. Dentro dele iremos ler os valores de `X` e `Y`. Após ler os valores iremos soma-los em `resultado`. E por fim usamos um `switch (resultado)` para identificar cada música e imprimir seu nome.

```c
    while (C--)
	{

		scanf("%hu %hu", &X, &Y);

		resultado = X + Y;

		switch (resultado)
		{
		case 0:
			printf("PROXYCITY\n");
			break;
		case 1:
			printf("P.Y.N.G.\n");
			break;
		case 2:
			printf("DNSUEY!\n");
			break;
		case 3:
			printf("SERVERS\n");
			break;
		case 4:
			printf("HOST!\n");
			break;
		case 5:
			printf("CRIPTONIZE\n");
			break;
		case 6:
			printf("OFFLINE DAY\n");
			break;
		case 7:
			printf("SALT\n");
			break;
		case 8:
			printf("ANSWER!\n");
			break;
		case 9:
			printf("RAR?\n");
			break;
		case 10:
			printf("WIFI ANTENNAS\n");
			break;
		}
	}
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com



