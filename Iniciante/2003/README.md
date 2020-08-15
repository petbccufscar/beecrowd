# Problema:

Todos os domingos, Bino faz compras na feira. Ele sempre marca com seu amigo Cino de se encontrarem no terminal de ônibus da Parangaba às 8h, para irem juntos comprar na feira. Porém, muitas vezes Bino acorda muito tarde e se atrasa para o encontro com seu amigo.

Sabendo que Bino leva de 30 a 60 minutos para chegar ao terminal. Diga o atraso máximo de Bino.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2003

# Resolução:

Para resolver o problema, vamos receber horários em que o Bino acorda e, para cada horário, exibir o tempo máximo de atraso até Bino chegar ao terminal de ônibus na hora combinada (8h da manhã). 

Primeiro declaramos as variáveis `hora` e `minutos` que receberão a hora e minuto referentes ao horário em que Bino acordou. 
```c
int hora, minuto;
```

Depois, iniciamos o laço de repetição `while`, onde iremos calcular cada possível atraso de Bino de acordo com a hora em que ele acordou. A condição de parada do laço possui o comando `scanf`, que fará a leitura das variáveis `hora` e `minuto` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição.
Os caracteres que são inseridos no meio, como :, são ignorados pela função `scanf`, pois com o `%d`  ela procura apenas por números inteiros. 
```c
while(scanf("%d:%d", &hora, &minuto)!=EOF){
	/*
		restante do código omitido
	*/
} 
```

Agora, dentro do `while` começamos a escrever a mensagem de atraso, referente a cada horário em que Bino acorda
```c	
printf("Atraso maximo: ");
```

Por fim, verificamos o tempo de atraso de Bino de acordo com o horário recebido e exibimos esse valor. Se ele acordou antes das 7h *ou* às 7h em ponto ele não irá se atrasar, pois ele demora até 60 minutos(1h) para chegar. Portanto, escrevemos: 0.
```c
if(hora<7 || (hora==7 && minuto==0))
	printf("0\n");

```

Se ele acordou depois das 7h em ponto ele irá se atrasar, por isso calculamos quanto tempo será esse atraso. Para realizar esse calculo, primeiro, contamos quantas horas ele está atrasado, depois transformamos essas horas em minutos e somamos com os minutos armazenados na variável `minuto`. Guardamos esse tempo nessa mesma variável `minuto` e exibimos o tempo de atraso.
```c
else{
	minuto = ((hora + 1)-8)*60 + minuto;
	printf("%d\n", minuto);
}
```

##### Para aprender um pouco mais sobre final de arquivo (EOF): [EOF](https://pt.wikipedia.org/wiki/EOF)

##### Para aprender um pouco mais sobre operadores lógicos: [Operadores Lógicos](http://linguagemc.com.br/operadores-logicos-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com