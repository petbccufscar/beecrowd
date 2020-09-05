# Problema:
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1.Criar 16 variáveis inteiras;

2.Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;

3.Ter 39 traços (-) na primeira linha;

4.Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 4o traço deve começar a escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, embaixo do 26o traço deve começar a escrever “Hexadecimal” e o restante preencher com espaço em branco;

5.Repita o procedimento 1;

6.Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 8o traço deve imprimir o valor da primeira variável em valor decimal, embaixo do 18o traço deve imprimir o valor da primeira variável em valor octal, embaixo do 31o traço deve imprimir o valor da primeira variável em valor hexadecimal e o restante preencher com espaço em branco;

7.Repita o procedimento 6 para as outras 15 variáveis;

8.Repita o procedimento 1.


##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2750
 
 
# Resolução:

Para essa resolução, faremos uma abordagem um pouco diferente da proposta no enunciado, a fim de tornar o processo um pouco mais automático e prático.

Incluímos, em nosso código a biblioteca `string.h` para utilizarmos funções de manipulação de strings, no caso, fazemos uso da função strlen(str), que retorna o tamanho de `str` (que é uma string qualquer).

Vamos a declaração de variáveis:
* Vetores de tamanho 16 (0-15 posições) nomeados de `decimais[16]` (que contêm os números decimais de 0 a 15), `octais[16]` (que contêm em octal o equivalente ao 0 a 15 em decimal).
* Auxiliares `i=0` e `k=0`

```c
    int decimais[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    int octais[16] = {0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17};
    int i=0, k=0;
``` 

Implementamos para esse exercício uma função `void faz_linha()` que se encarrega de escrever 39 traços na tela, que forma uma espécie de linha. Essa função está declarada antes do início da função principal(`int main`).
Nota: Funções do tipo [void](https://www.pucsp.br/~so-comp/cursoc/aulas/c740.html#:~:text=Em%20ingl%C3%AAs%2C%20void%20quer%20dizer,fun%C3%A7%C3%A3o%20que%20n%C3%A3o%20retorna%20nada%3A&text=Se%20n%C3%A3o%20quisermos%2C%20basta%20declarar,tipo%2Dde%2Dretorno%20void.) não possuem retorno, como no nosso caso precisamos apenas que a função escreva na tela, é o tipo mais recomendado.

```c
void faz_linha(){
    int i;
    for(i=0;i<39;i++){
        printf("-");
    }     
    printf("\n");
}
```

Utilizamos essa função em nosso código da seguinte forma: `faz_linha()`.

Nesse momento, é importante percebermos que temos 39 caracteres por linha, basicamente 39 colunas que podem ser preenchidas com caracteres ou inteiros. Por isso, é essencial se atentar ao tamanho das palavras ou números que estaremos imprimindo na tela.

Iniciamos um loop `for(i=0;i<39;i++)` para percorrer essas 39 colunas que temos, e preênche-las de acordo com o que foi pedido no enunciado.

    "Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 4o traço deve começar a escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, embaixo do 26o traço deve começar a escrever “Hexadecimal” e o restante preencher com espaço em branco;"

Durante o loop, passaremos por todas a posições e faremos verificações se correspondem a alguma posição que devemos inserir algo diferente de um espaço em branco, que é nosso caso "default". Começaremos o loop `for` em 0, o que nos leva a uma diferença de posição em relação ao exercício, que começa sua contagem a partir do 1. Assim, subtraimos 1 dessa posição dada pelo enunciado para encontrar o valor real no nosso loop. (Primeiro traço = 0, Décimo terceiro = 12 e assim por diante).

* O primeiro `if` verifica as posições em que deve existir um traço vertical e caso positivo, imprime uma barra vertical na tela `printf("|")`;
* O próximo `else if` verificam se está na posição inicial de a palavra decimal e caso positivo a imprime na tela e logo em seguida aumenta o contador em `strlen("decimal") - 1` pois temos um número limitado de caracteres para escrever (39) e nesse momento utilizamos `strlen("decimal")` que nos retorna o inteiro 7. Ademais, subtraimos 1, porque a primeira letra 'd' já foi considerada pela iteração do próprio loop
* Os próximos `else if` fazem o mesmo, mas para as palavras octal e Hexadecimal;
* Por fim, o `else` imprime um espaço em branco na tela (caso em que não temos nenhuma posição determinada no enunciado do exercício).
  
```c
for(i=0;i<39;i++) {
        if((i==0) || (i==12) || (i==22) || (i==38)) {
            printf("|");
        }
        else if(i==3) {
            printf("decimal");
            i += strlen("decimal") - 1;
        }

        else if(i==15) {
            printf("octal");
            i += strlen("octal") - 1;
        }

        else if(i==25) {
            printf("Hexadecimal");
            i += strlen("Hexadecimal") - 1;
        }
        else
            printf(" ");
    } 
    printf("\n");
```

Após essa linha escrita, temos mais uma linha com 39 traços, portanto:

```c
    faz_linha();
```

Nessa próxima parte, iremos escrever as 16 linhas que contêm os números, que já estão salvos nos vetores declarados no começo do exercício, e percorreremos, para cada linha, as 39 "colunas", uma a uma, verificando as condições de escrita que o exercício nos passa. Novamente, estamos com o iterador `i` variando de 0 a 38, então para todas as verificações, faremos "-1" na posição passada pelo enunciado.

PS: Os trechos de código a seguir estão contidos dentro do loop for interno, os blocos condicionais serão separados a fim de tornar a explicação mais didática.

```c
for(k=0;k<16;k++) {
    for(i=0;i<39;i++){
        /* blocos condicionais */
    }
}
```

No primeiro condicional, verificaremos as posições em que imprimiremos uma barra vertical.
    
    "Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha"

```c
    if((i==0) || (i==12) || (i==22) || (i==38)) {
        printf("|");
    }
```

No segundo bloco de verificação, agora um `else if`, temos dois casos para imprimir decimais:
* Caso 1: `i==7` imprimimos na tela o decimal na posição solicitada pelo exercício;
* Caso 2: Linha maior que 9 (`k>9`), ou seja, estamos lidando com um número de dois dígitos, e portanto, devemos imprimi-lo uma coluna antes, para as unidades ficarem alinhadas verticalmente. Para isso, deve satisfazer a condição `i==6 && k>9`.

O condicional interno verifica se estamos imprimindo um número de 2 digítos, e caso positivo, aumenta nosso contador `i` em 1, para não ultrapassar os 39 caracteres máximos e desalinhar a "tabela" que estamos criando.

```c
else if((i==7)||((i==6) && (k > 9))){
    printf("%d",decimais[k]);      
    if(k>9)
        i++;    
}
```


No terceiro bloco de verificação, novamente `else if`, temos a mesma divisão feita para os decimais, porém, com os números octais.
* Caso 1: `i==17` imprimimos na tela o octal na posição solicitada pelo exercício;
* Caso 2: Linha maior que 7 (`k>7`), ou seja, estamos lidando com um número de dois dígitos, e portanto, devemos imprimi-lo uma coluna antes, para as unidades ficarem alinhadas verticalmente. Para isso, deve satisfazer a condição `i==16 && k>7`;

O condicional interno verifica se estamos imprimindo um número de 2 digítos, e caso positivo, aumenta nosso contador `i` em 1, para não ultrapassar os 39 caracteres máximos e desalinhar a "tabela" que estamos criando.

```c
else if((i==17) ||((i==16) && (k > 7))){
    printf("%d",octais[k]);
    if(k>7)
        i++;
}
```

No quarto bloco de verificação, temos mais um `else if` porém, dessa vez não temos uma divisão, já que a escala hexadecimal equivalente de 0 a 15 em decimal não utiliza dois dígitos para representar um número.
Porém, temos uma conversão a ser feita, já que a partir do 9 decimal, os hexadecimais são escritos com as primeiras letras do alfabeto, para isso, utilizamos a estrutura `switch() { case }`, tendo como o caso default apenas um print do valor presente no vetor de decimais.

```c
else if(i==30) {
    switch(k){
        case 10 : printf ( "A" ); break; 		
        case 11 : printf ( "B" ); break;
        case 12 : printf ( "C" ); break;
        case 13 : printf ( "D" ); break;
        case 14 : printf ( "E" ); break;
        case 15 : printf ( "F" ); break;
        default:  printf("%d",decimais[k]);
    }

}
```

No quinto e último bloco de verficação, temos um `else` para imprimir um espaço em branco quando a posição não corresponder as posições indicadas no enunciado.

```c
else
    printf(" ");
}
```

Por fim, imprimimos mais uma linha com 39 traços, para fechar a "tabela" proposta pelo exercício.

```c
faz_linha();
```

E claro, não se esqueça do `return 0`

```c
    return 0;
```


Obs: Alguns `printf("\n")` foram omitidos durante essa explicação, porém são necessários para a formação da tabela como pede no enunciado. Aconselho que consulte o arquivo 2750.c nessa mesma pasta para verificar tais casos!

#### Para aprender sobre funções: [Funções](http://linguagemc.com.br/funcoes-em-c/#:~:text=Uma%20fun%C3%A7%C3%A3o%20nada%20mais%20%C3%A9,do%20nome%20atribu%C3%ADdo%20a%20ela.)

#### Relembrando estruturas: [Switch Case](http://linguagemc.com.br/o-comando-switch-case-em-c/)

#### Funções básicas da biblioteca string.h: [Funções String](http://linguagemc.com.br/a-biblioteca-string-h/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
