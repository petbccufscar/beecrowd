# Problema:
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor ímpar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1179


# Resolução:
A base deste exercício encontra-se na análise de cada uma das entradas conforme são fornecidas, de modo a inseri-la no vetor correspondente (par ou ímpar) até que esteja completo e, nesse caso, será exibido por completo. Ao final da leitura, é possível que os últimos valores armazenados não tenham preenchido todo o vetor, porém também devem ser impressos.  

Com o intuito de modularizar corretamente o código, utilizaremos 3 funções com funcionalidades específicas: `ehPar()`, `ehImpar()` e `imprimeRestante()`. Estas devem ser declaradas e definidas anteriormente à função `main()`, porém serão explicadas conforme são requisitadas no código.  

De acordo com o enunciado, serão fornecidas 15 entradas para serem colocadas em 2 vetores de 5 posições cada um. Portanto, é importante declararmos os vetores: `entradas` (com tamanho 15) para armazenar os números fornecidos; assim como `par` e `impar`, de tamanho 5, para separá-los de acordo com sua natureza.
As variáveis `posicaoPar` e `posicaoImpar` terão a funcionalidade de controlar as posições do vetor a serem preenchidas. São inicializadas com 0 para representar a localização do primeiro valor a ser armazenado.
`qtdeValores` atua como variável auxiliar para indicar quantos valores (dentre os 15) já foram lidos.

```c
int entradas[15], par[5], impar[5];
int posicaoPar=0, posicaoImpar=0;
int qtdeValores;
```

Primeiramente, é preciso realizar a leitura de todas as entradas e o armazenamento destas no vetor `entradas`. Isto pode ser feito com o auxílio da estrutura de repetição `for`, cujo escopo conterá o comando `scanf()`, de modo a repeti-lo até que todos os valores sejam lidos e inseridos na posição correspondente ao valor da iteração.

```c
for(qtdeValores = 0; qtdeValores < 15; qtdeValores++){
		scanf("%d",&entradas[qtdeValores]);
}
```

Um novo loop `for`, com mesma quantidade de iterações, ocorre novamente para que possamos efetuar a análise de cada um dos valores agora presentes no vetor `entradas`. Em seu escopo, será verificado se o valor atual equivale a um número par ou ímpar. Para enquadrar-se no primeiro caso, a estrutura `if` exige que a divisão deste por 2 possua resto igual a zero e, em seu interior, realiza a chamada da função `ehPar()`. Em situação contrária, o `else` direciona para a execução de `ehImpar()`.
Vale destacar que são fornecidos alguns parâmetros em ambas funções, os quais serão enviados até o escopo destas para fazer parte de sua lógica. Aqueles que contém `&` logo anteriormente, significa que estão sendo passados por referência. Isto significa que estamos fornecendo a posição daquela variável no arquivo do programa em questão e, dessa forma, garantimos que, se seu valor for alterado na função, será automaticamente atualizado também na `main()`. Esse mesmo feito ocorre quando vetores são parametrizados, porém não necessitam do caractere `&`.  

```c
for(qtdeValores = 0; qtdeValores < 15; qtdeValores++){

  if (entradas[qtdeValores]%2 == 0) {
    ehPar(entradas, par, qtdeValores, &posicaoPar);
  }

  else{
    ehImpar(entradas, impar, qtdeValores, &posicaoImpar);
  }

}
```

Para declarar uma função, deve-se determinar qual o tipo de retorno que fornecerá, seguido de seu nome e, entre parênteses, os parâmetros a serem recebidos (lembrando de especificar seus tipos). No caso das duas funções anteriormente citadas, a determinaremos como `void`, indicando que não haverá nenhum retorno. Os vetores enviados, assim como o inteiro fornecido como referência (ou seja, em que foi enviada sua posição na memória) devem conter um **asterisco** logo à esquerda para que seja utilizado o conteúdo contido ali. O mesmo deve ser feito para trabalhar com estas variáveis no interior das funções.  

```c
void ehPar(int *entradas, int *par, int qtdeValores, int *posicaoPar){
  //escopo da função ehPar
}

void ehImpar(int *entradas, int *impar, int qtdeValores, int *posicaoImpar){
  //escopo da função ehImpar
}
```

No escopo da função `ehPar()`, a única variável declarada corresponde a `tamanhoVetor`, que auxiliará no controle de iterações em momento futuro.
Objetivando iniciar a inserção de valores no vetor `par`, precisamos ter conhecimento se este possui condições de adicioná-lo. Para isto, a estrutura condicional `if` verifica se `posicaoPar` (variável correspondente a posição atual que pode ser preenchida) é menor que 5 (tamanho máximo do vetor). Em caso afirmativo, o vetor de pares irá armazenar, na devida posição, a entrada que está sendo verificada nesta iteração e, em seguida, incrementar a posição.
Em circunstância negativa, significa que o vetor está cheio e não consegue guardar mais nenhum valor. Dessa forma, no interior da estrutura `else`, precisaremos usufruir do loop `for` para exibir todos os valores ali contidos (seguindo o formato de saída estipulado pelo exercício) e, somente após todas as iterações serem feitas, zeramos a variável `posicaoPar`. Com isto garantimos que a entrada será inserida na primeira posição do vetor e, após tal feito, a incrementamos em 1.

```c
void ehPar(int *entradas, int *par, int qtdeValores, int *posicaoPar){
	int tamanhoVetor;

	if(*posicaoPar < 5){
		par[* posicaoPar] = entradas[qtdeValores];
		* posicaoPar = * posicaoPar + 1;
	}

	else{			
		for(tamanhoVetor=0; tamanhoVetor<5; tamanhoVetor++){
			printf("par[%d] = %d\n",tamanhoVetor,par[tamanhoVetor]);
		}

		* posicaoPar = 0;
		par[* posicaoPar] = entradas[qtdeValores];
		* posicaoPar = * posicaoPar + 1;
	}
}
```

Esta mesma lógica ocorre na função `ehImpar`, apenas realizando substituição pela variável e vetor correspondentes: `posicaoImpar`, `impar`.  

```c
void ehImpar(int *entradas, int *impar, int qtdeValores, int *posicaoImpar){
	int tamanhoVetor;

	if(*posicaoImpar < 5){
		impar[posicaoImpar] = entradas[qtdeValores];
		posicaoImpar = posicaoImpar + 1;
	}

	else{
		for(tamanhoVetor=0; tamanhoVetor<5; tamanhoVetor++){
			printf("impar[%d] = %d\n",tamanhoVetor,impar[tamanhoVetor]);
		}

		posicaoImpar = 0;
		impar[posicaoImpar] = entradas[qtdeValores];
		posicaoImpar = posicaoImpar + 1;
	}
}
```

Ao final da leitura completa de `entradas`, é possível que os últimos valores armazenados não tenham preenchido totalmente os vetores `par` ou `impar`. Todavia, também devem ser impressos e, com este intuito, realizamos a chamada da função `imprimeRestante()`. Assim como as demais, é declarada anteriormente à função principal e possui apenas parâmetros enviados por referência.
Contido em seu escopo, temos a declaração de uma variável `i` para auxílio em ambas as estruturas de repetição `for` que seguem. Nestas, limitamos, através de `posicaoImpar` e `posicaoPar`, que a iteração chegue somente até a última posição recentemente preenchida do vetor que está sendo analisado. Portanto, `printf()` exibirá na tela o restante dos valores contidos em `impar` e `par`, nesta ordem.  

##### Para aprender um pouco mais sobre ponteiros: [Programar em C/Ponteiros](https://pt.wikibooks.org/wiki/Programar_em_C/Ponteiros)

##### Para aprender um pouco mais sobre declaração de funções: [Funções em C](http://linguagemc.com.br/funcoes-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
