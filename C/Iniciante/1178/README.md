# Problema:
Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1178


# Resolução:
É importante armazenarmos o valor da entrada a fim de, posteriormente, utilizá-lo para gerar os demais 99 valores e, então, exibi-los na saída.

Como a nomenclatura já foi determinada pelo enunciado, declararemos a variável `X` (para armazenar o valor inicial fornecido) e o vetor `N` (de tamanho 100), que conterá cada um dos valores da saída. Ambos devem ser do tipo `double`, conforme a entrada exemplificada no exercício ["(...) contém um valor de **dupla precisão** com 4 casas decimais."]. Já a variável `i`, do tipo `int`, servirá de auxilio posteriormente.

```c
double X, N[100];
int i;
```

Utilizamos `scanf()` para receber a primeira entrada e armazená-la em `X`. Para isto, a função possui como argumento `%lf`, de modo a representar que estamos tratando do tipo `double`. Após já termos esse valor em mãos, o inserimos na primeira posição do vetor `N` e, logo em seguida, o exibimos através do comando `printf()`. Uma vez que o exercício especificou o formato de saída desejado ["Cada valor do vetor deve ser apresentado com **4 casas decimais**."], a função deve conter `%.4lf`.

```c
scanf("%lf",&X);

N[0] = X;
printf("N[0] = %.4lf\n",N[0]);
```

Como próximo passo, é possível realizar o loop `for` que itere de acordo com a quantia de próximos números a serem calculados, ou seja, com `i` iniciando em 1 e atingindo seu máximo valor quando igual a 99. Assim, a estrutura de repetição conterá, primeiramente, a atribuição da **metade** do valor de `X` à posição corrente do vetor. Este dado, agora devidamente armazenado, terá sua exibição na tela pelo `printf()`.
Em seguida, atualizamos o valor de `X` para que contenha a **metade** de seu valor atual (ou seja, equivalente àquele já impresso). Dessa forma, no início da próxima iteração, é garantido que armazenaremos a **metade** deste na posição seguinte do vetor.

```c
for(i=1;i<100;i++){
		N[i] = X/2;
		printf("N[%d] = %.4lf\n",i,N[i]);
		X = X/2;
	}
```

##### Para aprender um pouco mais sobre o tipo double: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)  

##### Para aprender um pouco mais sobre vetores: [Vetores – arrays em linguagem C](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
