# Problema:
Para melhor gerenciar a fabrica de presentes, os duendes estipularam quantos minutos são necessários para fabricar cada presente.
Já está quase no final do expediente, e um dos duendes pediu sua ajuda.
Faltam N minutos para a hora de ir embora, e restam dois presentes para o duende Ed fabricar. Ajude-o a descobrir se ele conseguirá fabricar os dois ainda hoje, ou se deve deixar o trabalho para amanhã.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2717
 
# Resolução:
O exercício consiste em ler o tempo restante para ir embora e o tempo para fazer os 2 presentes restantes, se não der tempo de fabricar os presentes eles ficaram para amanhã.

Primeiro instanciamos as variáveis necessárias, sendo elas: 3 `int` (`N` minutos restantes; `A` e `B` o tempo para cada presente).
E lemos os valores de `N`, `A` e `B`.


```c
    int N, A, B;
    scanf("%d", &N);
    scanf("%d %d", &A, &B);
```
 
Agora iremos utilizar um `if()` para comparar o tempo restante (`N`) com a soma do tempo dos presentes. Caso o tempo restante seja menor que a soma imprimimos `Deixa para amanha!`, caso contrário (ou seja, dê tempo de fabricar os presentes) imprimimos `Farei hoje!`.

```c
    if (N < A + B)
        printf("Deixa para amanha!\n");
    else
        printf("Farei hoje!\n");
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com





