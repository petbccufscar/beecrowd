# Problema:

Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

# Resolução:

O objetivo desse exercício é ler uma senha, verificar se é 2002 e, caso seja, mostrar na tela a mensagem `Acesso Permitido` e encerrar o programa. Caso não seja, mostrar na tela `Senha Invalida` e repetir o processo. 

Nesse exercício vamos declarar uma variável do tipo `int` chamado de `senha`:
```c
    int senha;
```
`senha` irá armazenar a senha lida. Depois no decorrer do código, iremos comparar o valor dessa variável com a senha correta fornecida pelo enunciado (2002).

Precisamos de uma estrutura que efetue a leitura enquanto a senha correta não for lida. Aqui vamos usar o `do.. while`:
```c
    do {
      scanf("%d", &senha);
```
Ao iniciar o laço de repetição, lemos um valor usando `scanf`. Em seguida, comparamos esse valor a 2002 e mostramos na tela a mensagem correspondente:
```c
      if (senha == 2002)
        printf ("Acesso Permitido\n");
      else
        printf ("Senha Invalida\n");
    } while (senha != 2002);
```
Se `senha` for igual a 2002 (`senha == 2002`), mostramos a mensagem `Acesso Permitido` usando `printf` e o programa termina a repetição do `while`, pois o loop de repetição só continua em execução caso a senha for diferente de 2002 (`senha != 2002`).

Se a senha for diferente de 2002, o programa mostra na tela a mensagem `Senha Invalida` e vai repetir o processo de leitura de `senha`.

##### Para aprender um pouco mais sobre a estrutura do... while: [Do... while](http://linguagemc.com.br/comando-do-while/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
