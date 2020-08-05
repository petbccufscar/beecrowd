# Problema:

Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

# Resolução:

O objetivo desse exercício é verificar se o valor lido é 2002 e mostrar na tela a mensagem `Acesso Permitido` se o valor for 2002 ou `Senha Invalida` se não for. 

Nesse exercício só precisamos de uma variável do tipo `int`:
```c
    int senha;
```
`senha` é a variável que será lida e comparada com o número 2002, valor dado no enunciado.

Precisamos ler a senha inúmeras vezes, já que não sabemos quantas vezes o usuário vai errar a senha. Aqui vamos usar o `do.. while`:
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
Se `senha` for igual a 2002 (`senha == 2002`), mostramos a mensagem `Acesso Permitido` usando `printf` e o programa termina a repetição no `while`, pois o processo só acontece de novo se senha for diferente de 2002 (`senha != 2002`).

Se a senha for diferente de 2002, o programa mostra na tela a mensagem `Senha Invalida` e vai repetir o processo de leitura de `senha`.

##### Para aprender um pouco mais sobre a estrutura do... while: [Do... while](http://linguagemc.com.br/comando-do-while/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
