# Problema:

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

## Entrada

A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

## Saída

Imprima o nome do animal correspondente à entrada fornecida.

# Resolução:

Para resolver o exercício precisamos criar 3 vetores de 20 caracteres do tipo char:
```c
        char palavra1[20], palavra2[20], palavra3[20];
```
No enunciado do problema, está escrito para ler três palavras para identificar o animal.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

Para ler as variáveis, usa-se scanf:
```c
        scanf("%s", palavra1);
        scanf("%s", palavra2);
        scanf("%s", palavra3);
```
Para ler um vetor de chars, também conhecido como string, é utilizado um %s. Para esse tipo de leitura string a palavra escrita não pode superar o número de caracteres da variável e não pode conter espaços dentro da variável.

##### Para aprender um pouco mais sobre strings: [Strings](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

Para poder saber qual é o animal com base nas palavras, as palavras são comparadas com as palavras base presentes no enunciado. Cada variável leva a duas opções diferentes até chegar na resposta que será mostrada na tela:
```c
        if (strcmp(palavra1,"vertebrado") == 0) 
            if (strcmp(palavra2,"ave") == 0) 
                if (strcmp(palavra3,"carnivoro") == 0) 
                    printf("aguia\n");
                else
                    printf("pomba\n");
            else
                if (strcmp(palavra3,"onivoro") == 0) 
                    printf("homem\n");
                else
                    printf("vaca\n");
                
        else
            if (strcmp(palavra2,"inseto") == 0) 
                if (strcmp(palavra3,"hematofago") == 0) 
                    printf("pulga\n");
                else
                    printf("lagarta\n");
            else
                if (strcmp(palavra3,"hematofago") == 0) 
                    printf("sanguessuga\n");
                else
                    printf("minhoca\n");       
```
Como devem ser comparadas palavras, é preciso usar uma biblioteca especial chamada de string.h para fazer essas comparações. Essa biblioteca contém a função strcmp, que retorna a um valor inteiro. Essa função compara as duas palavras e, se elas forem iguais, retorna 0.

Com base nessas comparações ele mostra na tela o nome do animal usando a função printf. O \n no fim serve para pular uma linha na tela depois de mostrar o dado.

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

##### Para aprender um pouco mais sobre a biblioteca string.h: [Biblioteca string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

###### Tirando o strcmp, todas as funções utilizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa. O string.h deve estar contido na linha seguinte.
