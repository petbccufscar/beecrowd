# Problema:

Seu professor gostaria de fazer uma tela com as seguintes características:

1. Ter 39 traços (-) na primeira linha;
2. Ter uma | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, abaixo do 10º traço deve-se começar a escrever a palavra "Roberto" e o resto preencher no meio com espaços em branco;
3. Ter uma | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço branco;
4. Ter uma | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, abaixo do 10º traço deve-se começar a digitar o número "5786" e o resto preencher no meio com espaços em branco;
5. Repita o procedimento 3;
6. Ter uma | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, abaixo do 10º traço deve-se começar a escrever a palavra “UNIFEI” e o restante preencher no meio com espaços em branco;
7. Repita o procedimento 1;

No final, deve ser semelhante à seguinte imagem:

![Imagem_Da_Descrição](https://i.ibb.co/8gBZVX8/ex.png)

**Problema Completo:** https://www.urionlinejudge.com.br/judge/en/problems/view/2748

# Resolução:

Este é um problema relativamente simples, pois para resolve-lo apenas utiliza-se o comando `printf` para escrever nosso output de acordo com a descrição do problema. Abaixo, temos o corpo principal do nosso código:

```c
#include <stdio.h>
 
int main() {
 
    /*
		restante do código omitido
	*/
 
    return 0;
}
```

E dentro deste corpo principal, na parte que diz "restante do código omitido", basta escrevermos as 7 linhas descritas no problema da seguinte forma:

```c
#include <stdio.h>
 
int main() {
 
    printf("---------------------------------------\n");
    printf("|        Roberto                      |\n");
    printf("|                                     |\n");
    printf("|        5786                         |\n");
    printf("|                                     |\n");
    printf("|        UNIFEI                       |\n");
    printf("---------------------------------------\n");
 
    return 0;
}
```
