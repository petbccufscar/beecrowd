# Problema:

Há muito tempo atrás, em uma galáxia muito, muito distante...

Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para um terreno 4 x 7 com um sabre de luz nele (na posição (2, 4)).

![Matriz](https://resources.urionlinejudge.com.br/gallery/images/contests/935.png)


**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2163

# Resoluçāo:

Para resolver este exercício, é necessário percorrer a matriz que é dada de entrada, e quando achar um valor igual a 42, verifica se todos os números vizinhos dele são iguais a 7.

Inicialmente declaramos as variáveis inteiras `N`, `M` que respectivamente guardam o número de linhas e colunas da matriz do problema. Já `i` e `j` são atuam como auxiliáres para percorrer laços. Por último, `padrao` conterá um valor 0 ou 1, em que 0 é quando não há padrão do sabre de luz da matriz de entrada, e 1 ocorre quando esse padrão é encontrado.


```c
   int N, M;
   int i, j, padrao = 0;
```

Então lemos os valores de `Ǹ` e `M` e declaramos a matriz `padraoSabre`
```c
   scanf("%d %d", &N, &M);
   int padraoSabre[N][M];
```

Usamos a função `scanf` para guardar o valor de cada valor que pertece a posição `i` `j` da matriz `padraoSabre`
```c
   for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            scanf("%d", &padraoSabre[i][j]);
        }
    }
```

Percorremos os elementos da matriz, começando em 1 e terminamos em `n-1`, pois o padrao do sabre de luz percisa que o número 42 tenha 8 números 7 ao redor dele.

Após acharmos um elemento é 42, usamos a função `oitoVizinhos` para fazer a verificação dos números ao redor do 42. No primeiro `if` nessa função fazemos a verificação se os números acima da posição 42 são 7; a segunda condicional verifica as posições ao abaixo do 42 e por fim verificamos as posições ao lado do 42.

Caso todos os números ao redor do 42 forem 7, retornamos 1, caso contrário será retornado 0.

```c

int oitoVizinhos(int i, int j, int N, int M, int m[N][M])
{
    int padrao = 0;

    if ((m[i][j + 1] == 7 && m[i - 1][j + 1] == 7) && m[i + 1][j + 1] == 7)
    {
        if (m[i - 1][j - 1] == 7 && m[i][j - 1] == 7 && m[i + 1][j - 1] == 7)
        {
            if (m[i - 1][j] == 7 && m[i + 1][j] == 7)
            {
                padrao = 1;
            }
        }
    }
    return padrao;
}
```

A variável `padrao` guardará o valor de retorno de `oitoVizinhos`. Usando um `if` para verificar se `padrao` é igual a 1, se for verdadeiro terminamos o laço interno do `for` usando o comando `break`. Essa verificação também é feita para o laço externo.
```c
   for (i = 1; i < N - 1; i++)
    {
        for (j = 1; j < M - 1; j++)
        {
            if (padraoSabre[i][j] == 42)
            {
                padrao = oitoVizinhos(i, j, N, M, padraoSabre);
                if (padrao == 1)
                {
                    printf("%d %d\n", i + 1, j + 1);
                    break;
                }
            }
        }
        if (padrao == 1)
            break;
    }
```

Ao final, se em nenhum momento o valor de `padrao` não mudar ele será 0, usamos uma condicional para fazer essa verificação e imprimimos o resultado quando nenhum padrão de sabre de luz é encontrado.
```c
    if (padrao == 0)
      printf("0 0\n");
```


 
##### Para aprender um pouco mais sobre Matrizes: [Matrizes](http://linguagemc.com.br/matriz-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com