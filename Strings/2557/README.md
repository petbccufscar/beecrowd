# Problema:
Durante sua grande aventura na Terra do Oeste, Joãozinho descobriu um livro sagrado que, segundo as lendas, foi escrito pelos próprios deuses antigos. Uma passagem em particular chamou a atenção do jovem aventureiro:

“A origem daquele que nada sabe se revelará quando aquele escolhido pelos deuses desvendar o enigma por eles lhe imposto. R+L=J.”

O enigma o intrigou bastante. Joãozinho logo começou a procurar por valores de R, L e J que satisfazem a equação citada na passagem. Após investigações, o jovem encontrou dois dos três valores citados. Joãozinho deve agora determinar o terceiro dos valores citados, para que o enigma seja solucionado e para que “a origem daquele que nada sabe” seja revelada.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2557

# Resolução:

Para resolver esse problema a lógica é a seguinte: deve ler uma equação, feito isso, percorre-se cada caractere dessa equação para que os números e sinais sejam armazenados. Em seguida, basta analisar qual operação deve ser feita e ver a posição de cada número em relação à equação. Com isso, obtém-se o necessário para realizar a conta e desvendar o enigma.
Antes de mais nada, declara-se as bibliotecas de função que serão usadas. Neste caso: `<stdio.h>` para receber e imprimir dados; `<stdlib.h>` para usar-se a função `atoi`; `<string.h>` para usar-se as funções `strlen` e `memset`. 
``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

Agora, dentro da função `main`, declara-se as váriaveis necessárias. Do tipo `char`: `equacao` que será o vetor responsável por armazenar a equação lida; `valores` que será a matriz bidimensional (uma dimensão para cada número da equação) responsável por armazenar os valoes numéricos da equação. Do tipo `int`: `soma` para definir qual operação será realizada; `lado_esquerdo1` e `lado_esquerdo2` que controlará em que lado da equação os valores 1 e 2 estão em relação ao sinal de igual, respectivamente; `valor1` e `valor2` para receber os valores da equação como número inteiros; `tamanho` que receberá a quantidade de caracteres da equação; `i`, `j` e `k` que serão contadores.
``` c
int main() {
    char equacao[50]={'0'}, valores[2][10] = {{'0'}};
    int soma=0, i=0, j=0, k=0, lado_esquerdo1=1, lado_esquerdo2=1, valor1, valor2, tamanho;
``` 

Na sequência, abre-se um loop `while` para leitura das equações que só se encerrará quando a leitura for `EOF` ("end of file"), atendendo assim aos requisitos dos testes automáticos feitos pelo corretor do URI. 
``` c
    while (scanf(" %s", equacao) != EOF) {
    /* código omitido para
    futuras explicações */
```

Dentro do loop, após a leitura da equação, define-se seu comprimento e abre-se outro `while`, usando a váriavel `i`como contador de caracteres percorridos, usando como limite o último caractere da equação. Esse loop é único para cada equação e será resposável por acessar cada membro dela, fazendo as manipulações necessárias.
``` c
        tamanho =(strlen(equacao));
        while (i<tamanho) {
```

Dando prosseguimento ao programa, a variável `j` deve ser zerada, pois ela será usada para armazenar os números da equação nas posições corretas da matriz `valores`. Ademais, abre-se outro `while` para percorrer os caracteres conferindo se eles não são letras ou sinais - o loop também possui como limite o tamanho da equação. Em seu interior (acessado somente se o caractere em questão for número), armazena-se os números lidos, confere-se, com uso de `if`, se o próximo caractere é um sinal. Caso sim, aumenta-se `k` - essa etapa é necessária para que se acesse a segunda dimensão da matriz de valores depois do número que estiver sendo lido no momento, possibilitando que o armazenamento dos números da  equação seja feita de uma forma independente. Por fim, incrementa-se `i` e `j`, para que haja avanço na leitura e armazenamento de caracteres.
``` c
            j=0;
            while (equacao[i] != 'R' && equacao[i] != 'L' && equacao[i] != 'J' && equacao[i] != '+' && equacao[i] != '=' && equacao[i] != '-' && i<tamanho) {
                valores[k][j] = equacao[i];
                if(equacao[i+1] == '+' || equacao[i+1] == '=' ||equacao[i+1] == '-' ) {
                    k++;
                }
                i++;
                j++;
            }
```

Finalizado o loop anterior, tem-se que o primeiro membro da equação foi lido, sendo assim, torna-se necessário definir alguns parâmetros para uso futuro. Primeiramente, é necessário definir se o primeiro caractere lido foi um número, para usa-se um `if`. Se `i` for 0, significa que foi lido uma letra, logo a  váriavel `lado_esquerdo1`  é zerada. Segundamente, confere se a operação que será feita é uma soma ou divisão, para isso basta  verificar se o caractere sendo acessado no momento por `i` é um sinal positivo, se sim, incrementa-se o valor de soma. Por fim, confere-se se alguma letra está do lado esquerdo da equação, para tal basta configurar o acesso para ser limitado ao penúltimo membro da equação (`i < tamanho-2`) e o primeiro número deve estar ao lado esquerdo (`lado_esquerdo1 == 1`). Ademais, incrementa-se `i` para acessar o próximo caractere. Assim finaliza-se o segundo loop.
``` c
if(i==0) {
                lado_esquerdo1 = 0;
            }
            else if(equacao[i] == '+') {
                soma++;
            }
            if((equacao[i+1] == 'R' || equacao[i+1] == 'L' ||equacao[i+1] == 'J') && lado_esquerdo1 == 1 && i<tamanho-2) {
                lado_esquerdo2 = 0;
            }
            i++;
        }
```

Avançando, usa-se a função `atoi`(resposável por transformar números de uma string em um dado do tipo `int`) para armazenar os números lidos na forma de números integrais.
``` c
        valor1 = atoi(valores[0]);
        valor2 = atoi(valores[1]);
```

Dessa forma, têm-se o necessário para imprimir o resultado, basta estipular cada condição e sua operação respectiva - para tal usa-se estruturas condicionais alinhadas.
* A primeira condição é: a operação é uma soma e ambos os números estão do lado esquerdo, logo soma-se os valores;
* A segunda: a operação é uma soma, mas um dos número não está do lado direito da equação, logo subtrai-se do segundo valor o primeiro valor;
* A terceira: a operação é uma subtração e ambos os valores estão do lado esquerdo da igualdade, logo subtrai-se do primeiro valor o segundo valor; 
* A quarta condição: a operação é uma subtração e um dos valores está do lado direito da igualdade, logo subtrai-se do primeiro valor o segundo valor.
``` c 
        if(soma == 1 && lado_esquerdo1==1 && lado_esquerdo2 == 1) {
            printf("%d\n", valor1 + valor2);
        }
        else if(soma == 1 && (lado_esquerdo1==0 || lado_esquerdo2 ==0)) {
            printf("%d\n", valor2 - valor1);
        }
        else if(soma == 0 && lado_esquerdo1 == 1 && lado_esquerdo2 == 1) {
            printf("%d\n", valor1 - valor2);
        }
        else if(soma==0 && (lado_esquerdo1==0 || lado_esquerdo2 ==0)){
            printf("%d\n", valor1 - valor2);
        }
```

Após a impressão do resultado, basta reiniciar os valores das variáveis para reiniciar o loop responsável pelos testes de caso. Assim sendo, configura as variáveis do tipo `int` para 0, e usa-se a função `memset` para zerar os valores das variáveis do tipo `char`. Dessa forma, o loop principal está encerrado e, para finalizar o programa, basta inserir `return 0`.
``` c
        soma = 0;
        i = 0;
        k = 0;
        j = 0;
        lado_esquerdo1 = 1;
        lado_esquerdo2 = 1;
        memset(valores[0], 0, 10);
        memset(valores[1], 0, 10);
    }
    return 0;
}
```

##### Para aprender um pouco mais sobre memset:[memset]http://www.cplusplus.com/reference/cstring/memset/
##### Para aprender um pouco mais sobre atoi:[atoi]https://www.cplusplus.com/reference/cstdlib/atoi/

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
