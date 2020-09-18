# Problema

Todo ano, Roberto gosta de escolher a sua árvore de natal, ele não deixa ninguém escolher para ele, pois ele acha que a árvore para ser bonita, deve satisfazer algumas condições, como altura, espessura e quantidade de galhos, para ele conseguir pendurar muitos enfeites nela.

Roberto quer que sua árvore tenha pelo menos 200 centímetros de altura, mas não quer que ela seja maior do que 300 centímetros, ou a árvore não irá caber em sua casa. Quanto a espessura, ele deseja que a sua árvore tenha um tronco com 50 centímetros de diâmetro ou mais. O número de galhos da árvore tem que ser igual ou maior a 150.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/3040

# Resolução

Para resolver o problema, iremos receber os valores de tamanho da árvore, do tronco e a quantidade de galhos e verificar se a entrada está dentro do esperado por Roberto.

Começamos declarando nossas variáveis, todas do tipo inteiro. Serão elas:
* `casos`: para a quantidade de casos que o programa verificará;
* `altura`: para a altura da árvore;
* `tronco`: para o tamanho do tronco da árvore;
* `galhos`: para a quantidade de galhos da árvore;
* `i`: para a iteração do laço de repetição do problema.
```c
    int casos, altura, tronco, galhos, i;
``` 

Lemos, inicialmente, a quantidade de casos que serão lidos, com a estrutura `scanf`.
```c
    scanf("%d", &casos);
```

Em seguida, iniciamos a estrutura de repetição `for` que terá a variável `i` repetir a quantidade `casos` de vezes.
```c
    for (i = 0 ; i < casos; ++i)
```

Recebemos, com a estrutura `scanf`, as variáveis de altura da árvore, tamanho do tronco e quantidade de galhos.
```c
    scanf("%d %d %d", &altura, &tronco, &galhos);
```

Verificamos se essas entradas estão de acordo com os critérios explicitados no enunciado, verificando se:
* A altura da árvore é maior ou igual a 200cm e menor ou igual a 300cm;
* O tamanho do tronco é maior ou igual a 50cm;
* A quantidade de galhos é maior ou igual a 150.```c
    if (altura >= 200 && altura <= 300)
        if (tronco >= 50)
            if (galhos >= 150)


Caso esses critérios sejam atendidos, exibimos "Sim" com a estrutura `printf`. Utilizamos a estrutura `continue` para que passe para a próxima iteração do laço. A condição do laço continua sendo testada, assim como o incremento.
Caso os critérios não sejam atendidos, exibi-se "Não" e passa para a próxima iteração do laço.
```c
            printf("Sim\n");
            continue;
        }

    printf("Nao\n");
```

##### Para aprender um pouco mais sobre o comando continue: [continue](http://linguagemc.com.br/o-comando-continue/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
