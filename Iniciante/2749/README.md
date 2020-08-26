# Problema
O seu professor de programação gostaria de fazer uma tela com as seguintes características:

    1.Ter 39 traços (-) na primeira linha;
    2.Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 2o traço deve começar a escrever "x = 35" e o restante preencher com espaço em branco;
    3.Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
    4.Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 17o traço deve começar a escrever "x = 35" e o restante preencher com espaço em branco;
    5.Repita o procedimento 3;
    6.Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 33o traço deve começar a escrever "x = 35" e o restante preencher no meio com espaço em branco;
    7.Repita o procedimento 1.

No final deve ficar igual a imagem a seguir:
```
--------------------------------------- (39 traços)

|x = 35                               |

|                                     |

|                x = 35               |

|                                     |

|                               x = 35|

--------------------------------------- (39 traços)
```

#### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2749]

De início declaramos as variáveis que usaremos, são elas: `tela` que será nossa matriz utilizada para receber os elementos da imagem, ela é composta de 39 colunas e 7 linhas; Em seguida, temos as variáveis `expressao1`, `expressao2` e `expressao3` que serão utilizadas para serem as linhas que contêm as expressões "x = 35'; Por fim, declaramos `i` e `j` para serem auxiliares no decorrer do código.
 
``` c
    char tela[39][7];
    char expressao1[] = "|x = 35                               |";
    char expressao2[] = "|               x = 35                |";
    char expressao3[] = "|                               x = 35|";
    int i = 0, j = 0;
```

Primeiramente, iremos atribuir a cada elemento da matriz `tela` a um caractere vazio `' '`, pois a linguagem C pode acessar lixo de memória que talvez estejam alocados no mesmo ramo de memória de um elemento da matriz, se isso acontecer ao imprimirmos a matriz irá aparecer caracteres indesejados na tela. Sendo assim, atribuimos caracteres vazios para termos uma matriz visualmente limpa. Para tal, criamos dois loops `for` sequenciados, o primeiro percorrerá 7(de 0 até 6) elementos e representa as linhas; o segundo percorrerá 39(de 0 até 38) elementos e é referente as colunas. 
``` c
        for(j = 0; j <= 6; j++) {
            for(i = 0; i <= 38; i++) { 
                tela[i][j] = ' ';
            }
        }
```
Agora, com nossa matriz pronta, começaremos a atribuir nela os elementos que compõe a imagem desejada. De início, atribuíremos os elementos da primeira e última linha. Visando isso, criamos um loop `for`, utilizando a variável `i`, que irá percorrer todos os elementos da primeira e última linha, respectivamente, atribuindo a eles o caractere `-`. Nesse caso: `tela[i][0]` e `tela[i][6]`.
``` c
    for (i=0; i<=38; i++) {
        tela[i][0] = '-';
        tela[i][6] = '-';
    }
```
Em seguida, precisamos atribuir os elementos presente nas primeiras e últimas colunas entre as linhas 1 e 5 da nossa matriz. Portanto, utilizaremos novamente a estratégia do loop `for`, dessa vez contaremos com a variável `j`. Dessarte, nosso loop percorrerá os primeiros e últimos elementos de cada linha, respectivamente, atribuindo a eles os caractere `|`, nesse caso: `tela:[0][1]` e `tela[38][5]`. 
``` c
 for (j=1; j<=5; j++) {
        tela[0][j] = '|';
        tela[38][j] = '|';
    }
``` 
Para finalizar, precisamos imprimir a matriz. Pensando nisso, fazemos um loop `for`, de 0 a 6 elementos (7 no total), que representará as linhas da nossa matriz. Dentro dele criamos uma estruturas condicionais alinhadas `if` e duas `else if`, elas ativaram nas linhas 1, 3 e 5, respectivamente. Tais estruturas são relativas as linhas que contêm as expressões "x = 35", contidas nas variáveis `expressao1`, `expressao2` e`expressao3`. Logo, quando forem ativadas elas imprimirão a linha correspondente a posição correta da expressão, formando corretamente a imagem.  Ademais, montamos uma estrutura `else` e dentro dela um loop `for` de 0 até 38 elementos (39 no total), assim imprimimos os demais elementos da matriz. Terminando as estruturas condicionais, colocamos uma função `printf` para garantir a quebra de linha entre cada execução do primeiro loop `for` (referente as linhas da matriz).
``` c
for(j = 0; j <= 6; j++) {
            if (j == 1) {
                printf("%s", expressao1);
            }
            else if (j == 3) {
                printf("%s", expressao2);
            }
            else if (j == 5) {
                printf("%s", expressao3);
            }
            else {
                for(i = 0; i <= 38; i++) {   
                    printf("%c", tela[i][j]);
                }
            }
            printf("\n");
    } 
``` 

#### Para aprender mais sobre matrizes: [http://linguagemc.com.br/arrays-com-varias-dimensoes-em-c/] [http://linguagemc.com.br/matriz-em-c/]
#### Para aprender mais sobre lixo na memória, segue alguns problemas como exemplo: [https://www.guj.com.br/t/problema-com-lixo-de-memoria-fflush/346328/4]
#### Para aprender mais sobre estruturas condicionais alinhadas: [https://www.vichinsky.com.br/Cbasico/pag13b.html] [http://linguagemc.com.br/estruturas-de-decisao-encadeadas-if-else-if-else/]

