# Problema:   

Cacunda, Bizz e Massacote são amigos inseparáveis. Na faculdade, em alguns dias, não iam à aula para jogar truco. Certo dia, um professor estava passando perto deles. Na mesma hora, os três gritaram bem alto a palavra “gzuz”. Após esse grito, ficaram invisíveis, e o professor não os viu. Outra vez, a turma deles estava respondendo perguntas do professor. Quando era a vez de algum deles, respondiam com a palavra “gzuz”, e o professor aceitava como resposta e dava a nota máxima da pergunta. Faça a simulação da saída que eles encontraram para se safar dos mais diversos problemas.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2861

# Resolução:

Apesar de ser um problema extremamente simples - só precisamos ler a entrada e imprimir `gzus`, existem dois detalhes que devemos nos atentar:
- As strings de entrada contêm espaços;
- Precisamos dar um jeito de desconsiderar o enter (`\n`) que vem depois do número de casos.

Primeiro, vamos por partes: começamos declarando as duas variáveis que vamos utilizar, `C` para o número de casos e `entrada` para o texto de entrada. Note que o texto pode conter até 99 caracteres, por isso criamos um vetor de caracteres com o mesmo tamanho.

```c
int C;
char entrada[99];
```

Logo após, vamos ler a quantidade de casos de teste do exercício. Existe um `\n` no final do `scanf()`, já que essa função procura por **padrões** no texto. Com isso, podemos ler o número `C` e pular para a próxima linha, sem interferir nas leituras dos textos seguintes.  
###### Este detalhe é necessário apenas para a particularidade do exercício, em que precisamos ler um texto com espaços após o número.

```c
scanf("%d\n", &C);
```

Usaremos a função `while()` para percorrer todos os casos de teste. Essa função é executada enquanto a condição dentro dela for verdadeira, mas a linguagem C não trabalha com "verdadeiro" ou "falso", mas sim com 0 e 1. Na verdade, qualquer coisa diferente de 0 é entendida como **verdadeiro** para o C, por isso podemos passar a quantidade de casos e decrementar ela ao mesmo tempo - quando os casos chegarem a 0, o `while()` interpreta isso como falso e interrompe a repetição.

```c
while (C--) {
```

O próximo detalhe está na função que vamos utilizar para ler o texto de entrada. Normalmente, quando utilizamos `scanf("%s")`, só conseguimos guardar o texto até o primeiro espaço ou quebra de linha. Para contornar isso, utilizamos a função `fgets()`, passando a variável `entrada` que vamos salvar, o tamanho máximo `99` dela e de onde vamos ler os valores - no caso, do "terminal" `stdin`.

```c
    fgets(entrada, 99, stdin);
```

Por último, a resposta para qualquer pergunta é `gzuz`. Sendo assim, imprimimos a expressão na tela e pulamos para a próxima linha.

```c
    printf("gzuz\n");
}
```

##### Para aprender mais sobre a função fgets: [fgets](http://www.cmaismais.com.br/referencia/cstdio/fgets/)
##### Para ler sobre diferentes formas de entrada em C: [Como ler do stdin em C?](https://pt.stackoverflow.com/questions/42981/como-ler-do-stdin-em-c)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
