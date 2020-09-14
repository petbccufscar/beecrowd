# Problema:

Dado a posição inicial de um cavalo em um tabuleiro de xadrez e a posição destino, deve se dizer se, com exatamente um único movimento, o cavalo consegue alcançar a posição destino. Se isso for possível, o movimento é classificado como válido, caso contrário, o movimento é dito inválido.

![tabuleiro](https://resources.urionlinejudge.com.br/gallery/images/contests/UOJ_360_M.png)

Em um tabuleiro de xadrez se utiliza números, de 1 a 8, para especificar a linha do tabuleiro e letras, de 'a' a 'h' para especificar a coluna.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2808

# Resolução:

Para resolver este problema, receberemos duas posições (inicial e final) do tabuleiro de xadrez, iremos compará-las e exibir se o movimento desejado (L) pode ser feito pelo cavalo (Válido) ou não (Inválido).
Iniciamos criando a função `diferenca` para calcular a distância entre as posições inicial e final do cavalo e retornar o valor obtido. Esta recebe dois valores inteiros (`a` e `b) como parâmetros e os compara através do comando `if`-else`: se o primeiro valor for maior que o segundo, armazenamos em uma variável auxiliar (`aux`) a subtração de `a` por `b`; caso contrário, será armazenado o resultado de `b - a`.
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

Iniciamos a função principal `main` declarando os vetores `inicial` e `final`, do tipo `char`, para armazenar as posições fornecidas na entrada; assim como as variáveis inteiras `coluna` e `linha`, que servirão para verificar os movimentos feitos pelo cavalo nas colunas e linhas do tabuleiro, respectivamente.
```c
char inicial[3], final[3];
int colunas, linhas;
```

Com o `scanf` lemos as posições inicial e final do cavalo.
```c
scanf("%s %s", inicial, final);
```

Em seguida, calculamos a diferença entre as posições do cavalo em relação aos valores da `coluna` e da `linha`, separadamente. Portanto, tais variáveis receberão o retorno correspondente obtido pela função `diferenca`.    
```c
coluna = diferenca(inicial[0], final[0]);
linha = diferenca(inicial[1], final[1]);as = diferenca( inicial[1], final[1]);
```
Note que as posições que são representadas por vetores de `char` são transformadas em inteiros ao serem passadas para a função `diferenca`. Isso é possível porque o tipo `char` interpreta caracteres como números através da [Tabela ASCII](https://www.tecmundo.com.br/imagem/1518-o-que-e-codigo-ascii.htm) permitindo realizar operações como se as variáveis `char` fossem inteiros. 

Através dos operadores lógicos, verificamos se a diferença na `coluna` é igual a `1` *e* na `linha` é igual a `2` *ou* se a diferença na `coluna` é igual a `2` *e* na `linha` é igual a `1`. Caso uma dessas proposições seja verdadeira os movimentos do cavalo são válidos e exibimos VALIDO com o comando `printf`, caso nenhumas delas seja, o movimento é inválido e exibimos INVALIDO, também com o `printf`.
```c
if((coluna == 1 && linha == 2) || (coluna == 2 && linha == 1))
    printf("VALIDO\n");

else 
    printf("INVALIDO\n");
```

##### Para aprender um pouco mais sobre funções: [funções em C](http://linguagemc.com.br/funcoes-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com