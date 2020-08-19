# Problema:

No crepúsculo, a cidade de Portland fica cheia de vampiros e lobisomens. Entretanto, nenhum deles quer ser visto enquanto passeiam pelo centro.

Vão ser instaladas câmeras de vigilância em cada esquina do centro de Portland. A cada mês, um mapa atualizado com as câmeras já em funcionamento é disponibilizado no site da prefeitura.

Uma quadra é considerada segura se existem câmeras em, pelo menos, duas de suas quatro esquinas. No centro de Portland todas as quadras são quadrados de mesmo tamanho.

Sua tarefa é, dado o mapa das câmeras em funcionamento nas esquinas, indicar o status de todas as quadras do centro.


Exemplo de Entrada:

                    2
                    1 0 0
                    1 1 0
                    0 0 1
Saída: 

                    SU
                    SS


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2168

# Resolução

O exercício a princípio pode causar uma confusão, porém ele consiste no geral em avaliar se há pelo menos dois 1 em uma quadra de uma matriz quadrática, pegando uma quadra da matriz 3x3 do exemplo de entrada temos:  

                                                                          1 0 
                                                                          1 1 

E nessa quadra vemos a presença de três 1 e a condição é no mínimo 2 pra ser considerado segura, no caso apresentar saída S, porém esse passo tem que ser repetido até todas as quadras sejam avaliadas.

Começamos declarando as variáveis que serão utilizadas:

```c
        int N;
        scanf("%d", &N);
        int M[N+1][N+1];
        int i, j;
```

`N` é o tamanho da matriz e esse tamanho é passado pelo usuário, portanto temos que ler ele primeiro antes de fazer a declaração da matriz `M`, `i` e `j` são as variáveis de iteração do nosso `for`.

Fazemos a leitura da matriz `M` e para isso precisamos de dois `for` em conjunto, devido a natureza da matriz e ela possuir linha, representada no `for` como `i`, e coluna, representada por `j`:

```c
       for (i = 0; i <= N; i++){  
                for (j = 0; j <= N; j++){
                        scanf("%d", &M[i][j]);
                } 
        } 
```

Seguimos para a construção dos `for` onde será feito a lógica do exercício:

```c
        for (i = 0; i < N; i++)
        {  
          for (j = 0; j < N; j++)
        {
                if(M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1] < 2)
                        printf("U");
                else 
                        printf("S");
        }
          printf("\n");
        }

```

Lembrando que queremos verificar as quadras dentro de uma matriz quadrática, pegando uma matriz 2x2 como exemplo, representaríamos a quadra dela na forma escrita assim: `M[0][0], M[0][1], M[1][0], M[0][1]` (Lembrando que o início se dá no 0 e não no 1). Então tendo isso em mente podemos verificar, usando `if`, se há pelo menos dois 1 nessa quadra, tendo ela na forma escrita fica fácil, porém isso deve estar transcrito de uma forma genérica, iremos somar essas posições e caso for maior que 2 está seguro ou `S`, menor que 2 não segura `U`

##### Para aprender um pouco mais sobre Matriz: [Matriz](http://linguagemc.com.br/matriz-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com