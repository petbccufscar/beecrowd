# Problema: 2523

Ao voltar de um intenso jogo de RPG na casa de um amigo, o jovem Will desapareceu misteriosamente! Todos estão desesperadamente procurando por ele por todos os cantos. Enquanto isso, coisas estranhas estão acontecendo em sua casa. Uma delas, entretanto, lhe permite comunicar-se com o garoto!

Há exatamente 26 lâmpadas penduradas na parede da sua sala, numeradas de 1 a 26 da esquerda para a direita. Além disso, há uma letra do alfabeto pintada na parede em baixo de cada lâmpada. Quando Will quer lhe enviar uma mensagem, ele irá (misteriosamente) piscar, uma a uma, as lâmpadas correspondentes a cada letra de sua mensagem. Por exemplo, se ele quer enviar a mensagem HELP, ele irá piscar, nesta ordem, as lâmpadas acima das letras H, E, L e P.
Dada a letra associada a cada lâmpada e a ordem das lâmpadas que foram piscadas por Will, decifre a mensagem que ele enviou!

##### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2523](https://www.urionlinejudge.com.br/judge/pt/problems/view/2523)
# Resolução:

De início declaramos as variáveis que serão utilizadas, para esse problema serão: "tamanho" para armazenar o tamanho da messagem a ser recebida; "i" para auxiliar no loop while;  "posicao_letras" para receber a posição das letras da mensagem. Ademais, vamos declarar um vetor "letras" para armazenar a sequência das letras do alfabeto que serão recebidas:
``` c 
	int  tamanho = 0,posicao_letras, i = 0;
	char  letras[25];
```
Primeiramente, é preciso receber a sequência de letras a ser armazenada no vetor "letras". Para tal, criamos usamos um a função `scanf`. Entretanto, como se trata de um exercício em que o vários testes realizados pelo URI são feitos através de arquivos temos que fazer um mecanismo para detectar o fim destes arquivos, sendo assim fazemos a leitura das letras dentro de um loop `while` que se encerrará quando atingir `EOF` ("end of file", fim do arquivo):
``` c 
	while(scanf("%s", letras) != EOF) {
```
Na sequência, receberemos o valor da variável "tamanho" com a função `scanf`:
```c
	scanf("%d", &tamanho);
```
Agora recebemos a posição de cada letra na variável "posicao_letras" através de `scanf` e imprimos sua letra correspondente usando `printf` no indice do vetor "letras".
 Para continuar imprimindo as letras até completar a mensagem usamos um loop `while` que acontecerá enquanto o valor da variável "i" for menor que o valor de "tamanho", dessa forma recebemos todas as letras da mensagem.  Por fim imprimimos uma linha em branco para finalizar a mensagem.
```c
	while (i < tamanho) {
	scanf("%d",&posicao_letras);
	printf("%c",letras[posicao_letras-1]);
	i++;
	}
	printf("\n");
}
```
###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
 