# Problema:

Durante o show, um bule de chá completo é preparado e são entregues uma xícara de chá para cada um dos cinco competidores. Os participantes devem cheirar, saborear e avaliar a amostra, de modo a identificar o tipo de chá, que pode ser: (1) o chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas. No final, as respostas são verificadas para determinar o número de suposições corretas.

Dado o tipo de chá real e as respostas fornecidas, determinar o número de participantes que receberam a resposta correta.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2006

# Resolução: 

Para resolver o problema receberemos o número referente ao sabor do chá que será degustado, a resposta dos 5 degustadores sobre qual é o sabor do chá e por fim exibimos quantos degustadores acertaram o sabor.

Para Começar, declaramos as variáveis que receberão o sabor do chá(`cha`), a resposta dos degustadores(`degustador`), a quantidade de degustadores que acertaram o sabor(`acertos`) e o `i` que servirá para verificar cada resposta dos degustadores. Também, iniciamos o `acertos` com 0, pois será incrementado posteriormente.

```c
int cha, degustador, acertos, i;

acertos = 0;
```
Depois, recebemos o sabor do chá com comando `scanf`. E iniciamos o laço de repetição `for` que irá receber cada uma das respostas dos 5 degustadores.
```c
scanf("%d", &cha);

for(i=0; i<5; i++){
	scanf("%d", &degustador);
	/*
	Próximo Bloco de Código
	*/
} 
```
Após recebermos a resposta de um dos degustadores verificamos se ela está certa, se sim acrescentamos +1 a variável `acertos`.  
```c
if(cha == degustador)
	acertos++;
```
Por fim, depois de verificar a resposta de cada um dos 5 degustadores exibimos quantos acertaram o sabor do chá.
```c
printf("%d\n", acertos);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com





