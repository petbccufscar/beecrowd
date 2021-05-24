# Problema:

A popularização das redes WiFi aumentou a taxa de perda de informações sendo transferidas, uma vez que diversos fatores do meio ambiente podem facilmente comprometer os dados durante o tráfego. A URI, Unidade de Recuperação de Informações, tem como principal objetivo identificar e corrigir erros em mensagens enviadas via redes WiFi.  

A técnica utilizada pela URI para identificação de erros é o teste de paridade, o qual pode ser descrito da seguinte forma: Seja S uma mensagem que será enviada de um dispositivo para outro. Antes de S ser enviada, um bit extra B é adicionado no final da representação binária de S. Se a mensagem S tiver um número par de bits de valor 1, o bit extra B terá valor 0. Caso contrário, se S tiver um número ímpar de bits de valor 1, B terá valor 1. Desta forma, após a inserção do bit B, a mensagem S terá um número par de bits de valor 1.  

Quando o destinatário recebe a mensagem S ele faz a contagem de bits de valor 1. Se a quantidade for par, significa que a mensagem chegou com sucesso. Caso contrário, significa que a mensagem sofreu uma alteração e não está correta.  

Sua tarefa é escrever um algoritmo que faça a inserção do bit B na mensagem S, de forma que após a inserção a mensagem S tenha um número par de bits de valor 1.


##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2176
 
 
# Resolução:

Para resolver o exercício, vamos apenas receber uma sequência de caracteres e contar quantos números `1` aparecem nela.  
Começamos declarando as variáveis necessárias para o algoritmo - um vetor de 100 caracteres `msg` para armazenar a mensagem recebida, um inteiro `bits` para contar quantos bits `1` aparecem na mensagem e 
uma variável `i` para usar em um loop. Também inicializamos a contagem de bits com 0.
```c
char msg[100];
int bits, i;

bits = 0;
```

Em seguida, faremos a leitura da mensagem com a função `scanf()`. Note que o parâmetro `%s` se encarrega de gerenciar as posições do vetor de caracteres.

```c
scanf("%s", msg);
```

Para descobrir se a quantidade de bits `1` é par ou ímpar, vamos percorrer todos os caracteres lidos e verificar se são iguais a `1`. Caso sejam, incrementamos a variável `bits`.  
Note que utilizamos a função `strlen()`, da biblioteca `<string.h>`, para descobrir o tamanho da mensagem.

```c
for (i = 0; i < strlen(msg); i++) {
    if (msg[i] == '1') {
        bits++;
    }
}
```

Agora, para verificar se `bits` é par ou ímpar, usamos o resto da divisão por 2, representado pelo operador `%`:
- Se `bits % 2` for igual a `0`, o número é par;
- Se `bits % 2` for `1`, o número é ímpar.

Coincidentemente (ou não), a mesma lógica se aplica ao bit de paridade do exercício:
- Se `bits` for par, adicionamos `0` ao final;
- Se `bits` for ímpar, adicionamos `1`.

Logo, podemos exibir diretamente o resultado da operação `bits % 2` na tela, adicionando ao final da mensagem `msg`. Faremos isso com duas funções `printf()`:  

A primeira exibirá a mensagem original com o parâmetro `%s`;
```c
printf("%s", msg);
```

A segunda exibirá o resultado da operação de paridade na mesma linha. Como a operação retorna um número, utilizamos `%d` para a exibição. Ao final, adicionamos uma quebra `\n` para encerrar o exercício.
```c
printf("%d\n", (bits % 2));
```

##### Para descobrir mais sobre a biblioteca string.h: [Biblioteca string.h](http://linguagemc.com.br/a-biblioteca-string-h/)
##### Para relembrar sobre strings: [Strings em C](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
##### Para revisar sobre o resto de uma divisão: [Resto de uma divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com