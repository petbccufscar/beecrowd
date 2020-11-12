# Problema

Então, nós temos que admitir: precisamos da sua ajuda. Esse ano as coisas não estao correndo tão tranquilamente quanto queríamos, e nós não conseguimos finalizar o sistema do software da competição a tempo. Uma parte vital está faltando, e como você sabe, nós precisamos desse sistema funcionando até essa tarde, para a verdadeira competição. A parte que está faltando é a que computa a pontuação dos times, dada a lista de submissões desse time.

Por favor, por favor, alguém nos ajude!

###### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/1367](https://www.urionlinejudge.com.br/judge/pt/problems/view/1367)

# Resolução

Resolveremos esse problema da seguinte forma: temos para cada letra do alfabeto dois armazenadores de tempo, dois para cada possível "problema" que está sendo resolvido. Um armazenador para o caso correto e um para os casos incorretos. Ao fim, verificamos todos os problemas que tiveram casos corretos e adicionamos 1 a contagem de corretos e para cada um desses, adicionamos ao tempo total a soma do tempo do caso do correto e o tempo de penalidade (+20) dos casos incorretos.

Para esse exercício, fazemos uso da biblioteca `string.h` para utlizar a função de comparação `strcmp(char* str1, char* str2)`

Começamos com a declaração de variáveis: 

`n` indica o número de submissões do caso de teste, finalizando a execução do programa quando for 0.

`identificador` `tempo` e `julgamento[10]` são relativos a submissão que está na entrada atual, para a linha `A 120 incorrect` temos que `identificador = A`, `tempo = 120` e `julgamento = incorrect`.

`corretos` e `tempo_total` são nossas saídas, representando o numero de submissões corretas e o tempo total referente ao caso de teste.

Os vetores `incorrect[26]` e `correct[26]` armazenarão o tempo gasto para um identificador específico.


```c
int n, tempo, i, corretos, tempo_total;
int incorrect[26], correct[26];
char identificador, julgamento[10];
```

Iniciamos o loop `while` principal que possue como condição estar lendo uma variável e a mesma ser diferente de 0 (condição dada pelo programa).

Nas primeiras linhas do loop, zeramos as variáveis de saída e de tratamento para retirar interferências das submissões anteriores ou do próprio lixo de memória (utlizamos [memset](https://www.tutorialspoint.com/c_standard_library/c_function_memset.htm) para os vetores). Com isso, podemos começar o loop `for` para receber e tratar todas as `n` submissões.

```c
while(scanf("%d", &n) && n){

    corretos = 0; tempo_total = 0;
    memset(incorrect, 0, sizeof(incorrect));
    memset(correct, 0, sizeof(correct));

    for (i = 0; i < n; ++i){
        .
        .
        .
    }
}
```

Agora no loop interno, utilizamos a função `getchar()` para limpar o buffer de entrada e com a função `scanf` lemos a submissão atual, atribuindo valores as variáveis `identificador`, `tempo` e `julgamento`.

O vetor `correct` funciona da seguinte forma, temos 26 posições, uma para cada letra do alfabeto, sendo A = 0, B = 1 e assim por diante. Essa conversão é feita utilizando a [tabela ASCII](https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm), com a conta (int(identifcador)-65) já que 65 é o inteiro relativo ao caractere A, assim, temos que A é 0 (65-65).
#### O mesmo vale para o vetor incorrect.

Com os valores da entrada devidamente armazenados, verificamos se o conteúdo de julgamento é `correct` ou `incorrect` com a função `strcmp` que nos retorna 0 caso as strings sejam iguais e um número diferente de 0 em caso negativo. 

No primeiro `if` verificamos se `julgamento == correct` e se `correct[(int(identifcador)-65)] também é 0, ou seja, para aquele `identificador` recebido, ainda não foi encontrada solução correta. No caso positivo desse `if` armazenamos o tempo gasto na solução correta ao vetor de corretos, na posição do identificador (identificador - 65). 

No segundo `if` verificamos se `julgamento == incorrect` e se ainda não foi encontrado a solução correta para aquele identificador. Em caso positivo desse `if` somamos 20  no vetor `incorrect` na posição do identificador (identificador - 65).

```c
for (i = 0; i < n; ++i) {
    getchar();
    scanf("%c %d %s", &identificador, &tempo, julgamento);

    if(strcmp("correct", julgamento) == 0 && correct[(int)identificador - 65] == 0)
        correct[(int)identificador - 65] = tempo;

    if(strcmp("incorrect", julgamento) == 0 && correct[(int)identificador - 65] == 0)
        incorrect[(int)identificador - 65] += 20;
}
```

Após a leitura de todas as submissões, podemos tratar a saída. Com um loop `for` percorremos todas as posições dos vetores `correct` e `incorrect` verificando se o valor armazenado em `correct[i]` é diferente de 0, em caso positivo ou seja, encontramos uma solução correta para aquele identificador de exercicio, a variável `corretos` é incrementada e o `tempo_total` recebe a soma de `correct[i]` e `incorrect[i]`.

Por fim, podemos printar quantos `corretos` tivemos e o `tempo_total` para aquelas `n` submissões.


```c
for (i = 0; i < 26; ++i) {
            if(correct[i] != 0){
                corretos++;
                tempo_total += (correct[i] + incorrect[i]);
            }
        }

        printf("%d %d\n", corretos, tempo_total);
```

##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
