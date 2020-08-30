# Problema:
...O navegador de Lucas possui um campo de busca onde o usuário poderá inserir uma palavra chave, e ao clicar em um botão de confirmação, ele será redirecionado para outra página com os resultados de sua pesquisa. Quando alguma string for digitada no campo de busca, Lucas quer que seu programa exiba, logo abaixo, algumas opções para auto completar esta string de acordo com as buscas já realizadas pelo usuário.

Por exemplo, se as palavras “algoritmos” e “algas” já foram pesquisadas, ao digitar a string “alg”, o programa deverá sugerir as palavras “algoritmos” e “algas”. Portanto, para cada string digitada, o programa deverá sugerir palavras pesquisadas anteriormente e que possuem como prefixo esta string. Caso alguma palavra seja igual a string digitada, ela também deve ser sugerida.

Lucas está preocupado com a quantidade de palavras que seu programa pode sugerir, além do tamanho máximo que elas podem alcançar. Por isso, ele pediu que você o ajude escrevendo um programa em que dadas algumas palavras já pesquisadas e uma série de consultas compostas por uma string, indique quantas palavras o navegador deverá sugerir ao usuário, além do comprimento da maior dessas palavras
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2635
 
 
# Resolução:
 
Para a resolução do problema, iremos importar a biblioteca `string.h`, para utilizarmos a função `strlen()` e `strncmp()`, e a biblioteca `stdlib.h`, para utilizarmos a função `malloc()`. 

Além disso, iremos declarar cinco variáveis do tipo `inteiro `, `n`, `q`, `i`, `achou` e `tam` e um vetor de caracteres de tamanho 100, `consulta[100]`. A variável `achou` indica quantas palavras o navegador deverá sugerir, `tam` o comprimento da maior dessas palavras e `consulta[100]` irá armazenar a string que será consultada.

```c
int n, q, i, achou, tam ;
char consulta[100];
```

Em seguida, lemos o número de palavras já pesquisadas.

```c
scanf("%d", &n);
```

Após isto, iremos alocar o espaço necessário para armazenar as palavras já pesquisadas. Como só conhecemos a quantidade de memória necessária durante a execução do programa, quando o usuário fornecer a quantidade de palavras já pesquisadas (`n`), precisamos utilizar a alocação dinâmica, utilizando a função `malloc()`.
Iremos alocar uma matriz de caracteres, com `n` linhas de tamanho 100, pois é informado que cada string pesquisada tem tamanho máximo de 100 letras minúsculas.
 
```c
char **pesquisa; 
pesquisa = malloc (n * sizeof (char *));
for ( i = 0; i < n; i++)
    pesquisa[i] = malloc (100 * sizeof (char));
```

Em seguida, utilizaremos uma estrutura de repetição `for` que irá iterar `n` vezes, uma para cada pesquisa. 
A cada iteração do laço de repetição lemos a string pesquisada.

```c
for( i = 0; i < n ; i++){
    scanf("%s", pesquisa[i]);
}
```

Depois disto, lemos o número de consultas que serão feitas.

```c
scanf("%d", &q);
```

Em seguida, vamos utilizar a estrutura de repetição `while(q--)` para o programa funcionar até que o valor de `q` seja 0, iterando `q` vezes.

A cada iteração do laço de repetição:
- atribuímos valor zero as variáveis `achou` e `tam`;
- lemos a string que será consultada;
- para cada pesquisa já feita:
        - verificamos se a consulta atual é prefixo de alguma pesquisa feita anteriormente. Fazemos isso por meio da função `strncmp()`, que compara duas strings caracter por caracter. O terceiro parâmetro da função define o número de caracteres a ser comparado. A função retorna "0" caso as strings sejam iguais. Se for :
        - adicionamos "1" a variavel `achou` e, se `tam` for menor que o tamanho da pesquisa cujo prefixo é igual à consulta, `tam` recebe este valor;
- Verificamos se `achou` é um ou zero:
        - caso seja zero, exibimos "-1" com quebra de linha.
        - caso seja positivo, exibimos `achou` e `tam` com quebra de linha.

```c
while(q--){
        achou = 0;
        tam = 0;

        scanf("%s", consulta);
        for( i = 0; i < n ; i++){
            
            if(strncmp(consulta, pesquisa[i], strlen(consulta)) == 0 ){

                achou++;
                if(tam < strlen(pesquisa[i]))
                    tam = strlen(pesquisa[i]);
            }
        }
        
        if(achou == 0)
            printf("-1\n");
        else
            printf("%d %d\n", achou, tam);
    }
```

 
##### Mais sobre alocação dinâmica: [alocação dinâmica](https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
