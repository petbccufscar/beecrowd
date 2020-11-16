# Problema:
Em diversos sistemas de computação, vários processos podem ler de um mesmo recurso durante o mesmo ciclo de máquina, mas somente um processo pode escrever no recurso durante o ciclo de máquina. Leituras e gravações não podem se misturar em um mesmo ciclo de máquina. Dado um histórico de leituras e gravações que ocorreram durante a execução de um determinado processamento, e um número inteiro que representa o número de processos usados, calcule a duração mínima do processamento, em ciclos de máquina. O rastro de histórico representa cada leitura por uma letra 'R' e cada gravação por uma letra 'W'.

Por exemplo, se o rastro de histórico é "RWWRRR" e o número de processos é 3, então o número mínimo de ciclos de máquina será 4: um para a primeira leitura, um para cada uma das gravações e apenas um para todo o último grupo de leituras.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1262

# Resolução: 
Para resolver este problema, leremos uma sequência de caracteres "W" e "R" e, conforme os padrões estipulados pelo enunciado, definiremos a quantidade de ciclos de máquinas realizados através da análise da sequência lida.
Iniciando, incluímos as bibliotecas que usaremos para a resolução: `<stdio.h>`, para leitura e impressão na tela de dados; `<string.h>`, para calcularmos o tamanho de vetor de caracteres.
``` c
#include <stdio.h>
#include <string.h>
```

Começando a função `main()`, declaramos as variáveis que serão utilizadas: do tipo `char`, `rastro_procesamento` que será nosso vetor recebedor dos caracteres "W" e "R"; do tipo `int`, `processos` que recebrá a quantidade de processos máximos; `i` nosso iterador para loop; `ciclos_maquina` que assumirá o valor dos ciclos realizados; `tam_rastro` que receberá o valor dos rastro(vetor de caracteres no código); `sequencia_leitura` que receberá o valor das leituras feitas em sequência ("R" seguidos).
``` c
    char rastro_processamento[50];
    int processos, i, ciclos_maquina, tam_rastro, sequencia_leituras;
```

Como no problema é expecíficado que a execução é feita por casos de testes e só se encerarrá com um caso `EOF` ("end of file"), iniciamos nossos comando com um loop `while` que lerá o rastro, irá guardá-lo no respectivo vetor e o comparará com `EOF`. Logo, enquanto o rastro fornecido for composto por "W" e "R", o programa executará.
``` c
    while(scanf("%s", &rastro_processamento) != EOF) {
        /* código omitido para
        futuras explicações */
``` 

Após a leitura de um caso de teste válido, lemos a quantidade de processos máximos simultâneos com o uso de `scanf` - armazendo-os em `processos`; calculamos o tamanho do vetor de caracteres com `strlen` - armazenando-o em `tam_rastro`; inicamos a contagem de ciclos atribuindo valor 0 à `ciclos_maquina`.
``` c
        scanf("%d", &processos);
        tam_rastro = strlen(rastro_processamento);
        ciclos_maquina = 0;
``` 

Dessa forma, usamos `i` para iniciar um loop `for` e, `tam_rastro` para limita-lo ao tamanho do vetor. Dentro desse loop, abrimos uma estrutura condicional `if` para comparar o primeiro elemento do vetor ao valor de "R" - indicação de uma leitura. Caso a comparação seja verdadeira, aumentamos a contagem de `ciclos_maquina` em 1 (o início de uma leitura é o início de um ciclo). Ademais, configuramos o valor de `sequencia_leituras` para 1, pois, ao se ler um valor "R", abre-se a possibilidade de início de uma sequência.
``` c
        for (i=0; i <= tam_rastro; i++) {
            if (rastro_processamento[i] == 'R') {
                ciclos_maquina++;
                sequencia_leituras = 1;
                i++;
``` 

Portanto, para verificar o tamanho da sequência de "R", aumentamos em 1 o valor de `i` (para acessar o próximo elemento do vetor), abrimos um loop `while` que confere se o elemento `i` do vetor é igual a "R". Se for, repetimos os passos de incrementos das variáveis relativas à sequência de "R" e de `i`. Com esse loop, obtemos o valor final de `sequencia_leituras`. 
 Agora, temos que saber quantos processos essa sequência demanda. Para tal, abrimos outro loop `while`, que ficará ativo enquanto a sequência for maior que o número máximo de processos. Em seu interior, aumentamos em 1 o valor de `ciclos_maquina`, pois, se a sequencia for maior que o numero de processos, significa que outro ciclo teve que ser inciado, e subtraímos o valor de `processos` da variável `sequencia_leituras` para dar baixa nas leituras contabilizadas no ciclo. Sendo assim, finalizamos o primeiro `if`.
``` c
                while (rastro_processamento[i] == 'R') {
                    sequencia_leituras++;
                    i++;
                }
                while (sequencia_leituras > processos) {
                    ciclos_maquina++;
                    sequencia_leituras = sequencia_leituras - processos;
                }   
            }
``` 

Agora, ainda dentro do loop `for`, abrimos um `if` para conferir se o elemento `i` do vetor sendo analisado é correspondente a "W". Se for, incrementamos em 1 o valor de `ciclos_maquina`, pois cada gravação é correspondente a um ciclo.
``` c
            if (rastro_processamento[i] == 'W') {
                ciclos_maquina ++;
            }
```

Por fim, imprimimos o valor de ciclos com a função `printf`, finalizando o loop `for`(e o caso de teste em questão), e finalizamos nosso programa com `return 0`.
``` c
        printf("%d\n", ciclos_maquina);
    }
    return 0;
}
``` 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com