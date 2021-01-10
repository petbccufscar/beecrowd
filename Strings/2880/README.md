# Problema

![Enigma](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2880.png)

Neste problema, dada uma mensagem cifrada e um crib, seu programa deve computar o número de posições possíveis para o crib na mensagem cifrada.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2880

# Resolução

Para resolver este exercício, é necessário verificar se um crib poderia estar em uma mensagem cifrada. Para verificar isso, comparamos se uma letra se repete nas mesmas posições do crib e da mensagem. Caso não se repita, essa palavra (crib) pode estar contida na mensagem cifrada.    

Iremos importar a biblioteca `string.h` que para utilizar a função `strlen` que retorna o tamanho de uma `string`.
```c
#include <string.h>
```

Iniciamos declarando as variáveis:
`cifra` e `crib`, vetores de `char`, que armazenarão a mensagem cifrada e o crib, respectivamente;
`igualdades`, que servirá para verificar se duas letras são iguais;
`limite`, irá limitar até que posição da mensagem cifrada podemos encaixar uma `crib`; 
`qtsPosicoesPossiveis`, será utilizada para contar em quantas posições da mensagem cifrada podemos encaixar a `crib` recebida;
`i, j, k`, serão usados para iterar pelas letras de `cifra` e `crib`.
```c
char cifra[10001], crib[10001];

int igualdades, limite, qtsPosicoesPossiveis;
int i, j, k;
```

Em seguida, recebemos `cifra` e `crib` com o comando `scanf` e iniciamos as variáveis: `i` em 0, para verificarmos as `strings` do começo; `qtsPosicoesPossiveis` em 0, pois ainda não verificamos as `strings` e `limite` com o tamanho de `cifra` menos o tamanho de `crib` com a função `strlen`.
```c
k = 0;
igualdades = 0;
qtsPosicoesPossiveis = 0;
limite = strlen(cifra) - strlen(crib);
```

Criamos um laço de repetição `while`, que irá percorrer as duas `strings` até `crib` não encaixar em `cifra`. E iniciamos o restante das variáveis que serão alteradas em cada iteração do `while`. 
`j = 0` para sempre começar da primeira letra de `crib`. 
`i = k`, para comparar sempre a próxima letra de `cifra`.
`igualdades = 0`, pois não encontramos nenhuma no começo de cada iteração.
```c
while (k <= limite){

	j = 0;
	i = k;
	igualdades = 0;
```

Depois, criamos outro `while` que com o comando `if-else`, irá comparar cada letra de `crib` e `cifra` até que `crib` acabe, ou que encontrar duas letras iguais. Nesse último caso, a `igualdade` recebe 1, assim a condição do `while`é desfeita e voltamos para o laço exterior.
Incrementamos `k` em 1 e verificamos se `igualdade` é igual a 0, caso verdade também incrementamos `qtsPosicoesPossiveis` em 1.
```c
while ( j < strlen(crib) && !igualdades){

	if (cifra[i] == crib[j])
		igualdades = 1;

	else{

		j++;
		i++;
	}
}

k++;

if (!igualdades)
	qtsPosicoesPossiveis++;
```

Por fim, depois de percorrer a `string` `cifra` exibimos a quantidade de posições em que é possível encaixar a `crib`
```c
printf("%d\n", qtsPosicoesPossiveis);
``` 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
