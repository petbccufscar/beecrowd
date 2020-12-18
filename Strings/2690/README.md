# Problema:
Um novo conjunto de autenticação será implementado no Instituto Federal do Sul de Minas, campus Muzambinho.

Bom, o novo serviço de autenticação é seguro, sem bugs e dores de cabeça mesmo porque estamos no final de semestre. Ele permitirá que sua senha tenha espaços, mas não números ou caracteres especiais. A atualização ocorre sempre no período de férias, para que todos os ajustes sejam feitos e no final agrade todos os usuarios. Como estagiário da central de suporte da escola, seu dever é implementar a nova autenticação. Por enquanto o novo padrão para nomes de usuários está sendo estudado.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2690.jpg" />

Como podemos perceber para cada conjunto de letras teremos um numero especifico. Bole um programa maroto para fazer essa conversão das letras para os números, e como você não acessará as senhas dos alunos, faça um algoritmo para que o mesmo faça o processo sozinho usando seus proprios casos de teste.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2690

 
# Resolução:
 

Inicialmente, iremos incluir a biblioteca `<ctype.h>`, para utilizar as funções `isalpha()`, que verifica se um caractere é uma letra do alfabeto.
Em seguida, globalmente, iremos declarar nossa função `converte(char)`, que recebe um caractere e retorna seu número correspondente, conforme a imagem no enunciado do problema indica, por meio da utilização de uma estrura `switch(letra)`. Note que optamos pela utilização de um `switch()` ao invés de estruturas condicionais `if-else`, pois não sabemos à priori quais casos são mais recorrentes e que com essa informação poderíamos utilizar `if-else` em ordem decrescente de recorrência, realizando o menor número de checagens, já que são feitas de forma sequencial(o último condicional necessita mais tempo para acessar que o primeiro). Por outro lado, no `switch()`, os `cases` possuem o mesmo tempo de acesso, já que é implementado por meio de uma lista hash.

```c
char converte(char letra){
	switch(letra){
		case 'G': case 'Q': case 'a': case 'k': case 'u':
			return 0;
		case 'I': case 'S': case 'b': case 'l': case 'v':
			return 1;
		case 'E': case 'O': case 'Y': case 'c': case 'm': case 'w':
			return 2;
		case 'F': case 'P': case 'Z': case 'd': case 'n': case 'x':
			return 3;
		case 'J': case 'T': case 'e': case 'o': case 'y':
			return 4;
		case 'D': case 'N': case 'X': case 'f': case 'p': case 'z':
			return 5;
		case 'A': case 'K': case 'U': case 'g': case 'q':
			return 6;
		case 'C': case 'M': case 'W': case 'h': case 'r':
			return 7;
		case 'B': case 'L': case 'V': case 'i': case 's':
			return 8;
		case 'H': case 'R': case 'j': case 't':
			return 9;
	}
}
```

Em seguida, em nossa função principal, iremos declarar três variáveis do tipo inteiro: `numSenhas`, indicando o número de casos; `qtdLetrasTraduzidas`, indicando a quantidade de letras já traduzidas e `i`, utilizada como auxiliar para lermos as letras de uma linha. Além disso, também iremos declarar o vetor de caracteres `senha[100]`, que irá armazenar a linha lida.

```c
int numSenhas;
int qtdLetrasTraduzidas, i;
char senha[100];
```

Depois, lemos a quantidade de senhas, armazenamos-a em `numSenhas` e utilizamos um laço de repetição `while( numSenhas --)`, que irá iterar `numSenhas` vezes. A cada iteração:
- lemos a senha a ser traduzida em questão, utilizando `scanf(" %[^\n]", senha)`, que efetua a leitura até que se encontre um `\n`;
- atribuímos 0 tanto a  `qtdLetrasTraduzidas`; 
- atribuímos 0 a nosso auxiliar de leitura da senha, `i`;
- utilizamos outro laço de repetição `while()`, que irá executar até que não haja caracteres a serem traduzidos em senha, ou que a `qtdLetrasTraduzidas` atinja 12 e, que a cada iteração:
	- verifica se o caractere em questão `senha[i]` é uma letra do alfabeto e, caso seja, a convertemos e exibimos, utilizando `printf("%d", converte(senha[i]))` e incrementamos um à `qtdLetrasTraduzidas`;
	- incrementamos um à `i`.
- imprimimos uma quebra de linha para iniciarmos a tradução da próxima senha.

```c
while( numSenhas--){
		
		scanf(" %[^\n]", senha);
		qtdLetrasTraduzidas = 0;
		i = 0;
		while(senha[i] && qtdLetrasTraduzidas < 12){
			if(isalpha(senha[i])){
					printf("%d", converte(senha[i]));
					qtdLetrasTraduzidas++;
			}
			i++;
		}
		
		printf("\n");
	}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
