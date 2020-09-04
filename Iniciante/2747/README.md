# Problema:

O seu professor de programação gostaria de fazer uma tela com as seguintes características:

    1. Ter 39 traços (-) na primeira linha;
    2. Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
    3. Repita o procedimento 2 mais quatro vezes;
    4. Repita o procedimento 1.

No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
--------------------------------------- (39 traços)

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2747

# Resoluçāo:

Neste exercício consiste em imprimir a saída conforme o padrão apresentado.

As variáveis `i` e `j` são utilizadas para poder fazer iteração dentro de dois laços, sendo `i` indicando as linhas e `j` as colunas.

```c
   int i, j;
```

Então utilizamos os `for` para fazer a impressão do padrão correspondente. É verificado primeiro se estamos nas bordas da figura. Na primeira condição verificamos se `i` está na linha 0 ou 6, em caso afirmativo é impresso `-`. Se a condição não for satisfeita, é verificado se `j` pertence a coluna 0 ou 38, se for positivo imprimimos `|`. No último caso estamos dentro da figura e so é impresso um espaço. 

Ao final de todas as iterações do laço interno, imprimimos uma quebra de linha dentro do laço interno para formar a figura desejada.

```c
   for (i = 0; i < 7; i++)
    {
        for (j = 0; j < 39; j++)
        {
            if (i == 0 || i == 6)
            {
                printf("-");
            }
            else if (j == 0 || j == 38)
                printf("|");
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
```
 
##### Para aprender um pouco mais sobre laço de repetição: [Laços](http://linguagemc.com.br/estruturas-de-repeticao/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com