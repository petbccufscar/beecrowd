# Problema:    
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1080


# Resolução:
A resolução deste exercício necessita que sejam armazenados todos os 100 valores inteiros fornecidos nas entradas e, em seguida, realize-se a comparação entre todos, para que seja encontrado aquele de maior valor.

Para guardar cada um dos valores que serão fornecidos, é declarado um vetor de tamanho equivalente a quantidade de entradas (neste caso, 100). Além disso, como o enunciado exige que seja fornecido o maior valor obtido, bem como a posição deste, declara-se as variáveis `valor` e `posicao`, respectivamente. Esta última é inicializada com o valor 0 devido a padronização da linguagem C, a qual impõe que a 1ª posição de um vetor possua índice igual a 0. Já a variável `i` servirá de auxílio posteriormente.

```c
int entrada[100];
int valor, posicao=0;
int i;
```

Em seguida, será utilizada a estrutura de repetição `for` (cobrindo as 100 iterações necessárias) para que cada uma das entradas sejam lidas e analisadas. Para isto, a leitura será feita através da função `scanf()` e armazenada na posição `i` do vetor `entrada`.

```c
for(i=0; i<100; i++){
  scanf("%d",&entrada[i]);
  ...
}//chave referente ao laço for
```

Como próximo passo, aplica-se a estrutura de decisão `if` para verificar qual valor é maior: o que está guardado na posição corrente do vetor ou aquele cujo índice está contido em `posicao`. Caso seja o primeiro, as variáveis são atualizadas para que contenham os novos dados correspondentes ao maior valor. Em cenário contrário, `else` garante que o valor continue o mesmo e a posição deste não seja alterada.

```c
if(entrada[i] > entrada[posicao]){
  valor = entrada[i];
  posicao = i;
}
else{
  valor = entrada[posicao];
}
}//chave referente ao laço for
```

Por fim, basta que sejam exibidos na tela (utilizando-se a função `printf()`) o maior valor encontrado e a posição de entrada. A variável `posicao` está sendo somada a 1 pois o exercício deseja saber qual das 100 entradas possui o maior valor, ou seja, entre a 1ª ou a 100ª. Todavia, o vetor tem 0 como primeira posição e, assim, é necessário o acréscimo em 1.

```c
printf("%d\n",valor);
printf("%d\n",posicao+1);
```

##### Para aprender um pouco mais sobre vetores: [Vetores – arrays em linguagem C](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

##### Para aprender um pouco mais sobre a estrutura for: [O laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
