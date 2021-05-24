# Problema:   

Você fica tão feliz no natal que tem vontade de gritar para todo mundo: "Feliz natal!!". Pra colocar toda essa felicidade pra fora, você montou um programa que, colocado um índice I de felicidade, seu grito de natal é mais animado.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2483

# Resolução:

Para a resolução deste problema iremos declarar uma variável para armazenar a quantidade de repetições da letra "a" o usuário deseja e uma variável para utilizarmos em um laço `for`. Realizamos também a leitura do valor através da função `scanf`.
```c
int i, indice;
scanf("%d", &indice);
```

Com o valor de repetições definidos, iniciamos imprimindo uma parte base da mensagem que contém as letras até o momento em que serão inseridas as novas, ou seja, iremos imprimir "Feliz nat". Após isso entramos em um laço de repetição que irá iterar o número de vezes inserida pelo usuário realizando a impressão da letra "a", e por final imprimimos a parte que falta para completarmos a frase, sendo essa parte o "l!", seguido de um `\n` como é solicitado pelo problema.
```c
printf("Feliz nat");
for(i = 0; i < indice; i++){
	printf("a");
}
printf("l!\n");
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
