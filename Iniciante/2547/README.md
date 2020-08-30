# Problema:

Todos os habitantes da Nlogônia estão super animados com a abertura do Ricardo Barreiro World, o mais novo parque de diversões do país. Na TV e no rádio só passam propagandas da montanha-russa do parque, a mais rápida do continente. É nela que todos, de crianças a idosos querem andar.

Infelizmente foram impostas algumas restrições no momento da homologação do brinquedo pelo governo. Por questões de segurança, há uma altura mínima e uma altura máxima que as pessoas devem ter para poder passear na montanha-russa.

Para o dia da inauguração do parque, todos os convidados realizaram um pré-cadastro no qual indicaram sua altura. Para reduzir filas e otimizar a operação do parque no primeiro dia, você foi contratado para fazer um programa que dado o número de visitantes, altura mínima, altura máxima e as alturas de todos os visitantes, calcule quantas pessoas poderão andar na montanha-russa.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2547

# Resoluçāo:

O objetivo desse problema é verificar se a altura de cada visitante está dentro dos limites estabelecido para poder andar na montanha russa, e ao final, imprimir o total de visitantes que podem usar a montanha russa.

Primeiramente iremos reclarar as variáveis inteiras: `n` armazena a quantidade de pessoas que irão na montanha russa, `min` e `max` são os limites mínimo e máximo de alturas permitidos. `i` tem a função de auxiliar do loop `for`, `altura` guarda o valor da altura que usaremos para verificar se está dentro do limite permitido e por fim, `visitantes` é um contador que tem o número total de visitantes que podem andar na montanha russa.

```c
    int n, min, max, i;
    int altura, visitantes = 0;
```

Então usamos o `while` para ler os valores de entrada, e o `EOF` para fazer a verificação se chegou ao final do arquivo.
 
```c
while (scanf ("%d %d %d", &n, &min, &max) != EOF)
{
```

No interior do `while`, há um `for` que serve para ler a altura de cada pessoa que quer entrar na montanha russa e assim, verificar por meio de um `if` se a altura da pessoa é maior ou igual que a altura mínima e se é menor ou igual que a altura máxima; caso seja a variável `visitantes` é incrementada em uma unidade. 

```c
    for ( i = 0; i < n; i++)
    {
        scanf ("%d", &altura);
        if (altura >= min && altura <= max)
            visitantes++;
    }
```

Após realizar todas as iterações possíveis dentro do loop, usamos a função `printf` para imprimir a quantidade de visitantes permitidos na montanha russa, e igualamos `visitantes` a 0, para que ela possa ser usada para outras entradas no mesmo arquivos.

```c
    printf ("%d\n", visitantes);
    visitantes = 0;
    }
```


##### Para aprender um pouco mais sobre Loops: [Loops](https://sites.google.com/site/itabits/treinamento/introducao-a-programacao-em-c/comandos-de-repeticao)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
