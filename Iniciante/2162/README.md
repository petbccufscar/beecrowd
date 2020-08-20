# Problema:

Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatamente na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seguido por outro pico, nem um vale seguido por outro vale.

O professor MC ficou curioso com esse padrão e quer saber se, ao medir outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2162

# Resoluçāo:

O padrão de Nlogônia ocorre quando o vetor segue um padrão que há número maior que é seguido por um menor que ele para todos os elementos, chamaremos esse padrão de maiorMenor; ou o contrário, quando há um número menor que é seguido por um maior até o final da estrutura, vamos chama-lo de menorMaior. Sabendo disso, iremos verificar se esse padrão é quebrado.

Primeiramente iremos declarar os interios `n`, que guarda a quantidade de alturas, `i` é uma variável auxiliar para fazer a iteração dentro de laços e `padrao` guarda valor de 0 ou 1, sendo que 0 é quando o vetor de alturas não segue o padrão de Nlogônia e 1 é quando segue.

```c
   int n, i, padrao = 1;
```

Fazemos a leitura do valor de `n` e declararemos o vetor de alturas, com `n` posições.
```c
   scanf("%d", &n);
   int alturas[n];
```

Verificamos se a primeira posição de alturas é menor que a segunda posição, se esta condição for verdadeira, teremos um padrão que para cada par, a altura menor sempre vem antes de uma altura maior.

Fazemos as iterações neste `for` apenas nos números pares, primeiro é feita uma verificação se `i` é igual a `n-1`, isso significa que o número de elementos do vetor é impar, e é preciso verifica se a posição anterior a i é maior ou igual a 0 para saber se o padrão é quebrado, e terminamos o laço usando o comando `break`.

A outra verificação ocorre quando `i` é menor que `n-1`, quando é verdadeira, verificamos se a posição atual do vetor é maior ou igual a próxima posição, se for verdade o padrão de Nlogõnica é quebrado e a repetição é terminada.

```c
   if (alturas[0] < alturas[1])
  {
    for (i = 0; i < n; i += 2)
    {
      if (i == n - 1)
      {
        if (alturas[i] >= alturas[i - 1])
        {
          padrao = 0;
          break;
        }
      }
      if (i < n - 1)
      {
        if (alturas[i] >= alturas[i + 1])
        {
          padrao = 0;
          break;
        }
      }
    }
  }
```

Se a primeira condição não for satisfeita, verificamos se o primeiro valor é igual ao segundo, neste caso também o padrão é quebrado. 
```c
   else if (alturas[0] == alturas[1])
   padrao = 0;
```

Quando nenhuma das condições anteriores não é válida, então a primeira altura é maior que a segunda. A lógica é parecida com o padrão menorMaior, mas o que difere é na hora de verificar a quebra de padrão. Neste caso, essa quebra ocorre quando o número da posição atual é menor ou igual que a da próxima posição ou quando é menor ou igual que a posição anterior.
```c
   else
   {
    for (i = 0; i < n; i += 2)
    {
      if (i == n - 1)
      {
        if (alturas[i] <= alturas[i - 1])
        {
          padrao = 0;
          break;
        }
      }
      if (i < n - 1)
      {
        if (alturas[i] <= alturas[i + 1])
        {
          padrao = 0;
          break;
        }
      }
    }
   }
```

Ao final, exibimos o padrão que foi encontrado, de acordo com as verificações anteriores. 

```c
   printf("%d\n", padrao);
```
 
##### Para aprender um pouco mais sobre laço de repetição: [Laços](http://linguagemc.com.br/estruturas-de-repeticao/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com