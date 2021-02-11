# Problema

No século XXII, uma doença devastadora atingiu mais da metade da população mundial. O governo está desesperado em busca de uma cura, pois há um grande risco de que a doença dizime toda a população. Os hospitais estão lotados e a aflição no olhar das pessoas é notável.

Nesta época, poucas pessoas têm acesso livre à internet, mas você é uma delas. Ao vasculhar a rede, você encontrou alguns textos dispersos sobre um amuleto de uma palavra mágica escrita em forma de um triângulo que cura doenças letais. Incrédulo mas esperançoso, você se lembrou de que a biblioteca do Sr. Severino tinha um livro um tanto inusitado, com a seguinte capa:

![imagem](https://resources.urionlinejudge.com.br/gallery/images/contests/UOJ_231_A.jpg)

Então, você foi imediatamente à biblioteca. Chegando lá, ao ler somente o prefácio do livro, já confirmou tudo o que viu sobre os amuletos na rede, e em seguida, deu a si mesmo uma missão: espalhar palavras mágicas na rede em forma de um triângulo a fim de alertar as pessoas de que pode haver uma cura para a doença. Por consequência, se forem construídos amuletos em massa com palavras mágicas e estes forem entregues às pessoas, a doença pode ser aniquilada e a população, salva.

Para completar tal missão, você deverá começar pelo passo mais simples: escrever um programa que receba uma palavra e a transforme em um triângulo, tal como na capa do livro.

**Problema completo**: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2484](https://www.urionlinejudge.com.br/judge/pt/problems/view/2484)

# Resolução

Iremos escrever todos os caracteres da palavra de forma separada, dando um espaço entre eles e a cada linha escrita, diminuiremos um caractere e aumentamos um espaço no início da palavra, até termos apenas uma caractere escrito.

Pontos a serem observados da saida:
* Entre as saídas referentes a uma entrada, existe uma linha vazia
* Em todas as linhas da saída, temos um espaço entre duas letras (apenas entre duas letras, a última letra não possui espaço a direita).
* A cada linha, a palavra diminui em 1 letra, portanto 2 caracteres (letra e espaço)
* A mesma medida que diminui as letras, a palavra (ou resto dela) aumenta um espaço em branco antes de começar a imprimir caracteres


Esses dois últimos pontos faz com que o efeito de pirâmide invertida aconteça, já que sempre ao tirar 2 caracteres, colocamos 1.

Começaremos com a declaração de variáveis, `palavra` é um vetor de caracteres que armazenará a palavra recebida da entrada e `tamanho` armazenará o tamanho da `palavra`.

```c
int i, j, tamanho;
char palavra[110];
```

Como no problema temos que a entrada deve ser lida até o fim do arquivo, fazemos o loop while com essa condição. Comparamos o [retorno da função scanf](https://www.tutorialspoint.com/c_standard_library/c_function_scanf.htm) com EOF (end of file) e em caso de serem diferentes, podemos continuar dentro do loop.

```c
while(scanf("%s",palavra) != EOF){
    .
    .
    .
}
```

Dentro do loop, atualizamos a variável `tamanho` para o tamanho da palavra recebida com a função `int strlen(char *str)` já que para cada palavra, esse valor deve ser alterado.

Assim, podemos fazer um loop `for` que terá `tamanho` iterações já que como pode ser percebido na saída, vemos que o número de linhas, é o mesmo que o tamanho da palavra.

Em cada uma dessas linhas iremos printar `j` espaços, repare que a cada iteração do loop `for` externo, o tamanho de `j` é aumentado em 1 unidade, portanto, mais espaços serão exibidos.


```c
 while(scanf("%s",palavra) != EOF){

    tamanho = strlen(palavra);

    for(j = 0; j < strlen(palavra); j++){
        for(i=0;i<j;i++){
            printf(" ");
        }   
        .
        .
        .

    }
}
```

Agora com o ínicio da palavra já setado pela quantidade de espaços impressa, podemos imprimir a palavra, caractere a caractere. Portanto, criamos um loop de 0 a `tamanho - 1`, printando o caractere na posição `i` e um espaço em branco.
ao fim do loop, printamos mais um caractere, sem o espaço à direita, pois fizemos o loop até `tamanho-1`. Esta letra é impressa junto com um `\n`, para encerrar a linha atual.

Com isso, podemos encerrar essa linha retirando um caractere da palavra, fazemos isso decrementando a variável `tamanho`. Ao diminuir a quantidade de iterações do loop `for`,  é impresso um caractere a menos. 

Ao terminar de imprimir todas as linhas originando a pirâmide solicitada no problema, pulamos uma linha para começar o processo novamente para a próxima palavra.

```c
while(scanf("%s",palavra) != EOF){

    tamanho = strlen(palavra);

    for(j = 0; j < strlen(palavra); j++){
        for(i=0;i<j;i++){
            printf(" ");
        }
        for(i = 0; i < tamanho-1 ;i++){
            printf("%c ",palavra[i]);
        }
        printf("%c\n",palavra[i]);
        tamanho--;
    }
    
    printf("\n");

}
```

Não se esqueça do `return 0` ao final!


##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
