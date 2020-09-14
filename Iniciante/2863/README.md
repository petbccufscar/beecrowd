# Problema:

Umil Bolt é um excelente corredor. Sua especialidade é a prova dos 100 metros rasos. Todos os dias, ele faz uma bateria de tentativas de correr esta prova em um tempo cada vez menor. Pode se perceber que, dependendo da quantidade de tentativas, o seu desempenho melhora ou piora. Sobre isso, ele pede a sua ajuda para calcular a tentativa mais rápida de cada bateria diária.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2863

# Resolução

Nesse exercício, iremos receber um número de tentativas e analisá-las para escolher a melhor entre elas, isto é, a que possuir menor valor.

Declaração das variáveis usadas:

```c
    	int T, i;
		float numero, menor;
```

`T` representa o número de tentativas, `i` variável de iteração, `numero` o tempo das tentativas e `menor` o tempo da tentativa de menor valor.

Seguimos para a leitura do número de tentativas `T`:
```c
       while (scanf("%d", &T) != EOF)
		{
        }
```
Usamos esse `while` com a condição `EOF` devido ao exercício não limitar quantas vezes os testes serão executados.

Passamos para lógica do exercício:
```c
        while (scanf("%d", &T) != EOF)
		{

		menor = 100.0;
		for (i = 0; i < T; i++)
		{
			scanf("%f", &numero);
			if (numero < menor)
				menor = numero;

		}

		printf("%.2f\n", menor);

	}
```
Iniciamos a variável `menor` com um valor alto para garantir que o primeiro `if` seja executado. A lógica do `if` é, caso encontrar um valor menor na última leitura de tempos na variável `numero`, a variável `menor` torna-se o valor de `numero`.

Terminamos exibindo a saída pedida pelo URI:
```c
        printf("%.2f\n", menor);
```
**OBS:**A saída tem que possuir duas casa após a vírgula, por isso tem que ter o formato de `%.2f`.

#### Para aprender um pouco mais sobre: [A utilização do EOF](https://www.clubedohardware.com.br/topic/827103-eof/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com