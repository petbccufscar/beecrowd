# Problema
 [...] Seu amigo precisa aumentar o número de variações de sua senha, e pediu sua ajuda. Dada a senha que ele escolheu, diga o número de diferentes variações que é possível montar.
problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1632

# Resolução

Para resolvermos o problema, iremos percorrer cada caracter e verificar se ele é um caracter especial. Tudo será explicado em detalhes a seguir.

Usamos a biblioteca `ctype.h` para podermos usar a função `tolower`que transfroma qualquer caracter em seu correspondente minúsculo.

Declaração de variáveis:
Começamos declarando as variáveis dentro da `main` (nesse exercício não foi preciso criar procedimentos nem funções).
possibilidades: do tipo `int`, conta o número de possibilidades para a senha;
T: do tipo `int` indicando o número de casos de testes;
i, j: do tipo `int` que serão auxiliares no loop;
senha: do tipo char, será a senha que o usuário irá digitar.

``` c
int possibilidades;
    int T;
    int i, j;
    char senha[20];
```

Logo após a declaração de variáveis, lemos o número de senhas que o usuário irá digitar:

``` c
scanf("%d", &T);

```
Depois, fazemos um for que começa em 0 e termina um número antes de `T`, em que a há um incremento de 1 em `j` a cada loop. Dentro desse `for`, fazemos a leitura da variável `senha`, e declaramos que a variável possibilidades é igual a 1, já que ela será multiplicada por 2 ou 3 no loop que vem a seguir.

``` c
for (j = 0; j < T; j++){

        scanf(" %s", senha);
        possibilidades = 1;
```
Agora, fazemos um outro `for` dentro do `for` anterior. Esse, começa em zero e termina quando já tivermos percorrido todos os caracteres da variável `senha`, somando 1 na variável auxiliar `i` a cada loop. Dentro desse `for`, fazemos um `if` que funciona da seguinte forma: se a senha tiver algum caracter "especial", ou seja, se a senha tiver "a" ou "e" ou "i" ou "o" ou "s", a variável `possibilidades` é multiplicada por 3, senão é multiplicada por 2. Essa multiplicação ocorre porque, caso a senha possua um caracter especial, ele pode ser substituido por outros dois: ele mesmo maiúsculo ou um número: a por 4, e por 3, i por 1, o por 0, s por 5. Enquanto as demais letras não podem ser sustituídas por números. Lembrando que a função `tolower` transforma as letras maiúsculas em minúsculas para que a verificação seja mais rápida.

``` c
for (i = 0; senha[i]; i++){
            if (tolower(senha[i]) == 'a' || tolower(senha[i]) == 'e' || tolower(senha[i]) == 'i' || tolower(senha[i]) == 'o' || tolower(senha[i]) == 's')
                possibilidades *= 3;
            else
                possibilidades *= 2;   
```

No final, o número de possibilidades é printado para a tela.

``` c
 printf("%d\n", possibilidades);

```


