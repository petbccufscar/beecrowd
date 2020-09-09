# Problema:
Dado um conjunto de N pontos sobre uma circunferência de um círculo, todo par de pontos está ligado por um segmento e três desses segmentos nunca se encontram em um ponto interno à circunferência.

Sua tarefa é determinar em quantas partes esses segmentos dividem o interior do círculo.

![imagem](https://resources.urionlinejudge.com.br/gallery/images/contests/UOJ_360_D.png)

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2802

# Resolução:

O exercício consiste em ler o número de pontos na circunferência e imprimir um inteiro representando a quantidade de partes do círculo.

Primeiro instanciamos as variáveis necessárias, sendo elas: 2 `long long` (`N` para o número de pontos e `resultado` para armazenar o resultado de quantas partes foi dividido).
Começamos lendo o número de pontos existem, lembrando de que como estamos utilizando um `long long` devemos utilizar `%lli` para ler e imprimir essa variável

```c
	long long N, resultado;
    scanf("%lli", &N);
```

Agora calculamos em quantas partes foi dividido o círculo. O exemplo do exercício não deixa claro como fazer tal cálculo, aparenta só ser necessário elevar ao quadrado, contudo o `resultado` vem da expressão ***1 + combinacional de N por 2 + combinacional de N por 4***.

- Entenda um pouco mais sobre a matemática do problema:
- [Combinacional pdf](http://blogimages.bloggen.be/gnomon/attach/218796.pdf)
- [Combinacional vídeo](https://www.youtube.com/watch?v=_gMRRS1wbj4)

```c
    resultado = 1 + (((N - 1) * N) / 2) + ((N * (N - 1)*(N - 2)*(N - 3)) / 24);
```

Por fim nos resta imprimir o número de partes.

```c
    printf("%lli\n", resultado);
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
