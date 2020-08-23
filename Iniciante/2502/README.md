# Problema:
A cifra mais antiga conhecida é a Cifra de César. César escrevia suas cartas trocando cada letra pela próxima do alfabeto, para evitar que, quando a carta fosse interceptada, conseguissem ler. Com o tempo, a criptografia adquiriu melhor qualidade, mas a criptografia por substituição ainda é uma brincadeira de criança interessante, por exemplo:

ZEN I T
POLAR

Neste tipo de brincadeira, ao escrever uma carta a letra Z é trocada pela letra P e vice versa, bem como: E e O e assim sucessivamente. A frase cifrada desta forma: "Osro roxre osri caftide" pode ser decifrada como: "Este texto esta cifrado". Como a brincadeira ficou séria, a você foi solicitado um programa que decifre as mensagens cifradas a partir de uma chave fornecida.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2502

# Resolução:

Para resolver esse problema receberemos a quantidade de letras das cifras, a quantidade de linhas da mensagem a ser decifrada, as cifras e cada linha da mensagem a ser decifrada. A partir disso, comparamos as letras da mensagem com as letras das duas cifras. Caso alguma letra seja igual, trocamos com a letra correspondente na outra cifra.

Começamos inserindo 2 bibliotecas, a `string.h` e a `ctype.h`. A primeira contém a função `strlen`, que será utilizada posteriormente para verificar o tamanho de uma `string`, já a segunda possuí as funções `tolower` e `toupper`, as quais serão utilizadas para mudar uma letra maiúscula para minúscula, e vice versa, respectivamente.

```c
#include <string.h>
#include <ctype.h>
```

Em seguida, declaramos as variáveis. `tamCifra` servirá para armazenar o tamanho das cifras; `qntLinhas` armazenará a quantidade de linhas da mensagem a ser decifrada; `i`, `j`, `k` variáveis a serem utilizadas por laços de repetição `for`; `cifra1`, `cifra2` são vetores de caracteres(`strings`), que guardarão as duas cifras e `fraseEncriptada`, outra `string` que armazenará as linhas da mensagem.
```c
int tamCifra, qntLinhas, i, j, k;
char cifra1[21], cifra2[21], fraseEncriptada[1000];
```

Iniciamos o laço de repetição `while`, onde iremos decifrar as mensagens. A condição de parada do laço possui o comando `scanf`, que fará a leitura das variáveis `tamCifra` e `qntLinhas` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição.
```c
while(scanf("%d %d\n", &tamCifra, &qntLinhas) != EOF){
```
 * Note que: o enunciado do problema não especifíca a condição de parada do `while` com (EOF), mas visto isso em exercícios anterioes, podemos concluir que é assim que termina.

Depois, recebemos as duas cifras através do comando `fgets`, que é similar ao comando `scanf`, mas se difere por poder armazenar caracteres em branco (`' '`) mais facilmente.
```c
fgets(cifra1, sizeof(cifra1), stdin);
fgets(cifra2, sizeof(cifra2), stdin);
```

Criamos um laço de repetição `for` para tornar todas a letras das cifras minúsculas. Utilizamos a função `tolower` da biblioteca `ctype.h`, explicada anteriormente, para esse propósito. Isto é feito para que caracteres especiais, números e espaços sejam trocados para letras minúsculas, como pede o enunciado.  
```c
for (i = 0; i < tamCifra ; i++){
	
	cifra1[i]=tolower(cifra1[i]);
	cifra2[i]=tolower(cifra2[i]);
}
```

Então, criamos outro loop `for` para decifrar as mensagens, uma linha de cada vez. E lemos, com o comando `fgets` a primeira linha da mensagem.
```c
for(i=0; i<qntLinhas; i++){
		
	fgets(fraseEncriptada, sizeof(fraseEncriptada), stdin);
```

Dentro do loop anterior, iremos criar outros dois `for` de forma aninhada. O primeiro loop percorrerá a linha da mensagem, já o segundo irá percorrer as duas cifras, comparando o caracter da linha com os caracteres das cifras, através do comando `if`. Caso sejam iguais, trocamos o caracter da linha pelo caracter da outra cifra. 
A condição de parada do primeiro `for` tem função `strlen`, que irá retornar o tamanho (em caracteres) da linha passada anteriormente.
```c
for(j=0; j<strlen(fraseEncriptada); j++){

	for(k = 0; k<tamCifra; k++){

		if(fraseEncriptada[j] == cifra1[k])
			fraseEncriptada[j] = cifra2[k];

		else if(fraseEncriptada[j] == cifra2[k])
			fraseEncriptada[j] = cifra1[k];

		else if(fraseEncriptada[j] == toupper(cifra1[k]))
			fraseEncriptada[j] = toupper(cifra2[k]);

		else if(fraseEncriptada[j] == toupper(cifra2[k]))
			fraseEncriptada[j] = toupper(cifra1[k]);
	} 
}
```   
 * Note que: utilizamos a função `toupper`, pois caso a letra da frase seja maiúscula conseguimos comparar com a letra minúscula das cifras. Assim, mantendo a letra maiúscula e respeitando a capitalização.

Por fim, exibimos a frase decifrada e na última frase da mensagem pulamos uma linha, como é pedido no enunciado do problema.
```c
		printf("%s", fraseEncriptada);
	}

	printf("\n");	    
}
```
 * A primeira chave fecha o `for` que percorre as linhas de uma mensagem, e a segunda fecha o `while` que recebe cada mensagem.

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a função `fgets`: [fgets](https://aprendendoc.wordpress.com/tag/fgets/)
##### Para aprender um pouco mais sobre a biblioteca `string.h`: [string.h e strncmp](http://linguagemc.com.br/a-biblioteca-string-h/)
##### Para aprender um pouco mais sobre a biblioteca `ctype.h`: [string.h e strncmp](http://linguagemc.com.br/ctype-h-toupper-tolower-isalpha-isdigit-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com





   
