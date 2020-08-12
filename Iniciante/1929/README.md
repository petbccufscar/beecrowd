# Problema:

Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1929

# Resolução:

Um triângulo pode ser formado por três varetas se a maior vareta do trio for menor que as outras duas varetas juntas. Isso é conhecido como [Condição de existência de um triângulo](https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-a-condicao-existencia-um-triangulo.htm).

Nesse exercício criamos oito variáveis do tipo `int`:
```c
    int A, B, C, D, v[4], i, j, aux;
```
`A`, `B`, `C` e `D` são as quatro variáveis que serão lidas, representando o comprimento de 4 varetas. `v` é um vetor de 4 posições que vamos usar para ordenar os valores lidos. `i` e `j` serão usada durante o laço de repetição `for` e `aux` é um auxiliar para a ordenação dos valores.

Precisamos ler os valores de `A` a `D`. Aqui vamos usar o `scanf` para ler o valor:
```c
    scanf("%d%d%d%d", &A, &B, &C, &D);
```
Podemos escrever mais de um valor dentro de um `scanf` usando vários `%d`. Depois de ler esses valores, colocamos os dados obtidos no vetor `v`:
```c
    v[0] = A;
    v[1] = B;
    v[2] = C;
    v[3] = D;
```
Aqui começa a ordenação dos valores. Vamos deixar os valores dados em ordem crescente e para isso usamos duas estruturas `for`. Dentro dela, verificamos se `v[i]` é maior que `v[i+1]` (`v[i] > v[i+1]`) e, se for, invertemos os dois valores:
```c
    for(j=0;j<4;j++)
      for(i=0;i<3;i++) {
        if (v[i] > v[i+1]) {
          aux = v[i+1];
          v[i+1] = v[i];
          v[i] = aux;
        }
      }
```
Para garantir que os valores estão em ordem crescente, passamos por todos os valores do vetor 4 vezes (`j=0;j<4;j++`). Ao inverter valores, devemos ter cuidado para não sobrescrever nenhum valor, por isso usamos a variável `aux`. Ela guarda um valor e permite a troca entre `v[i]` e `v[i+1]`.

Agora que os comprimentos estão ordenados, podemos verificar se é possível fazer um triângulo usando três dos quatro valores mostrados. Como não sabemos qual valor será descartado nós consideramos todos os casos possíveis. Se for possível fazer o triângulo o programa deve mostrar `S` na tela, senão deve mostrar `N`:
```c
    if ((((v[0] + v[1]) > v[3]) || ((v[0] + v[2]) > v[3])) || (((v[1] + v[2]) > v[3]) || ((v[0] + v[1]) > v[2])))
      printf("S\n");
    else
      printf("N\n");
```
Segundo a condição de existência de um triângulo, a soma dos dois comprimentos menores deve ser maior que o comprimento maior do triângulo. Por causa disso fizemos a ordenação, sem ela não conseguimos selecionar qual o maior valor para ser comparado.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre estruturas de decisão: [Estrutura de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
