# Problema:

Dado a posição inicial de um cavalo em um tabuleiro de xadrez e a posição destino, deve se dizer se, com exatamente um único movimento, o cavalo consegue alcançar a posição destino. Se isso for possível, o movimento é classificado como válido, caso contrário, o movimento é dito inválido.
![tabuleiro](https://resources.urionlinejudge.com.br/gallery/images/contests/UOJ_360_M.png)
Em um tabuleiro de xadrez se utiliza números, de 1 a 8, para especificar a linha do tabuleiro e letras, de 'a' a 'h' para especificar a coluna.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2808

# Resolução:

Para resolver este problema, receberemos duas posições (inicial e final) no tabuleiro de xadrez, iremos compará-las com o movimento feito pelo cavalo (L) e exibiremos se é um movimento que o cavalo pode fazer (Válido) ou não (Inválido).

Para iniciar, criamos a função `diferenca` que servirá para contar a distância entre o valor inicial e final do movimento do cavalo e retornar esse valor. Essa função funciona recebendo dois valores inteiros (a e b) como parâmetros, e os compara com o comando `if`. Caso `a` seja maior que `b`, `a` subtrai `b`, caso contrário `b` subtraí `a`. Nos dois casos, o resultado é armazenado em uma variável auxiliar `aux`, a qual será retornada.
```c
int diferenca(int a, int b)
{
	int aux;

	if(a>b)
		aux = a-b;
	else
		aux = b-a;
	
    return aux;
}
```

Iniciamos a funcão principal `main` e declaramos as variáveis `inicial` e `final`, que são vetores de `char` e irão representar a posição inicial e final do cavalo, respectivamente; e mais duas váriaveis inteiras `coluna` e `linha`, que servirão para verificar os movimentos feitos pelo cavalo nas colunas e linhas do tabuleiro, respectivamente.
```c
char inicial[3], final[3];
int colunas, linhas;
```

Com o `scanf` lemos as posições inicial e final do cavalo.
```c
scanf("%s %s", inicial, final);
```

Em seguida, `coluna` recebe o valor da diferença das posições final e inicial nas colunas do tabuleiro, retornados pela função `diferenca`.
```c
colunas = diferenca( inicial[0], final[0]);
```

E `linha` recebe o valor da diferença das posições final e inicial nas linhas do tabuleiro, retornado pela função `diferenca`
```c
linhas = diferenca( inicial[1], final[1]);
```
Note que, as posiçoes que são representadas por vetores de `char` são tranformadas em inteiros ao serem passadas para a função `diferenca`, isso é possível porque o tipo `char` interpreta números em letras através da [Tabela ASCII](https://www.tecmundo.com.br/imagem/1518-o-que-e-codigo-ascii.htm) permitindo realizar operações como se as variáveis `char` fossem inteiros. 

Através do operadores lógicos, verificamos se a diferença na `coluna` é igual a `1` *e* na `linha` é igual a `2` *ou* se a diferença na `coluna` é igual a `2` *e* na `linha` é igual a `1`. Caso uma dessas proposições seja verdadeira os movimentos do cavalo são válidos e exibimos VALIDO com o comando `printf`, caso nenhumas delas seja, o movimento é inválido e exibimos INVALIDO, também com o `printf`.
```c
if((colunas == 1 && linhas == 2) || (colunas == 2 && linhas == 1))
    printf("%s\n", "VALIDO");

else 
    printf("%s\n", "INVALIDO");
```

##### Para aprender um pouco mais sobre funções: [funções em C](http://linguagemc.com.br/funcoes-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com