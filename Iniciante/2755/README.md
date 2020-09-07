# Problema:

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1. Mostre a seguinte frase na tela: "Ro'b'er to\/" (Entre o r e o t tem uma tabulação);
2. Mostre a seguinte frase na tela: (._.) ( l: ) ( .-. ) ( :l ) (._.);
3. Mostre a seguinte frase na tela: (^_-) (-_-) (-_^);
4. Mostre a seguinte frase na tela: ("_") ('.');

Exemplo de Saída:

                        "Ro'b'er        to\/"
                        (._.) ( l: ) ( .-. ) ( :l ) (._.)
                        (^_-) (-_-) (-_^)
                        ("_") ('.')

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2755

# Resolução

O exercício se resume a seguir a sequência de instruções dada pelo exercício para exibir a saída desejada.

Seguimos a ordem das instruções começando pela primeira:

1ª Mostre a seguinte frase na tela: "Ro'b'er to\/" (Entre o r e o t tem uma tabulação);

```c
        printf("\"Ro'b'er	to\\/\"\n");
```

Alguns caracteres necessitam de formas especiais para poderem ser exibidos no `printf` normalmente, ex o caso `\"` exibe aspas duplas, `\\` exibe barra invertida. 

2ª Mostre a seguinte frase na tela: (._.) ( l: ) ( .-. ) ( :l ) (._.);
Sempre lembrando da quebra de linha `\n` necessária em todas as etapas:

```c
       printf("(._.) ( l: ) ( .-. ) ( :l ) (._.)\n");
```

3ª Mostre a seguinte frase na tela: (^_-) (-_-) (-_^);

```c
        printf("(^_-) (-_-) (-_^)\n");
```

4ª Mostre a seguinte frase na tela: ("_") ('.');

```c
        printf("(\"_\") ('.')\n");
```
Nessa etapa final só se atentar ao tentar imprimir aspas duplas, não basta apenas colocar ela dentro do `printf` devido a função compreender isso como uma palavra chave, então devemos usar o mesmo modo que usamos na primeira etapa para exibir as aspas duplas que é `\"`. Com isso finalizamos o exercício.

#### Para aprender um pouco mais sobre: [Formatação da frase dentro do printf](http://excript.com/linguagem-c/caracter-escape-c.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com