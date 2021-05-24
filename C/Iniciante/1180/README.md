# Problema:
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1180


# Resolução:
É importante armazenarmos o primeiro valor de entrada para que o vetor a ser utilizado tenha o tamanho necessário. Além disso, este conterá cada uma das próximas N entradas, para que sejam analisadas com o intuito de encontrar a de menor valor, bem como sua posição.  

Seguindo a sugestão do enunciado, é declarada a inteira `N`, com o objetivo de armazenar o tamanho do vetor a ser utilizado. Além disso, como exige-se que sejam fornecidos o menor valor obtido e a posição deste, declaramos as variáveis `menorValor` e `posicao`, respectivamente. Esta última é inicializada com o valor 0 para representar a 1ª posição do vetor que, de acordo com a padronização da linguagem C, possui índice igual a 0.

```c
int N, posicao=0, menorValor;
```

Realizamos a leitura da primeira entrada, através da função `scanf()`; obtendo, assim, o valor inteiro `N`. Com isso, temos o valor necessário para que seja possível declarar o vetor `X` com seu devido tamanho. A variável `i`, também declarada, servirá de auxilio posteriormente.

```c
scanf("%d",&N);
int X[N], i;
```

Em seguida, realizamos o loop `for` iterando de acordo com as `N` próximas entradas a serem lidas e analisadas. Para isto, a leitura será feita através da função `scanf()` e armazenada na posição `i` do vetor `X`.

```c
for(i=0;i<N;i++){
		scanf("%d",&X[i]);
  ...
}//chave referente ao laço for
```

Como próximo passo, aplica-se a estrutura de decisão `if` para verificar qual valor é menor: o que está guardado na posição corrente do vetor ou aquele cujo índice está contido em `posicao`. Caso seja o primeiro, as variáveis são atualizadas para que contenham os novos dados correspondentes ao menor valor. Em cenário contrário, `else` garante que o valor continue o mesmo e a posição deste não seja alterada.

```c
  if(X[i] < X[posicao]){
    menorValor = X[i];
    posicao = i;
  }

  else{
    menorValor = X[posicao];
  }
}//chave referente ao laço for
```

Por fim, basta que sejam exibidos na tela (utilizando-se `printf()`) o menor valor encontrado e a posição deste no vetor. Vale destacar que é essencial inserir na função de saída os textos "Menor valor:" e "Posicao: ", como exemplificado no exercício.

```c
printf("Menor valor: %d\n",menorValor);
printf("Posicao: %d\n",posicao);
```

##### Para aprender um pouco mais sobre vetores: [Vetores – arrays em linguagem C](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

##### Para aprender um pouco mais sobre a estrutura for: [O laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
