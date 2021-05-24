# Problema:

A sua tarefa é bem simples, será dado uma lista com diversos nomes de cursos de graduação e você terá que imprimir o nome do curso que Vitória deve fazer.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1924

# Resolução:

Nesse problema vamos ler inúmeras palavras e responder sempre `Ciencia da Computacao`, porque esse é o curso que Vitória deve fazer segundo os casos de exemplo do exercício.

Para resolver o exercício precisamos criar 2 variáveis do tipo `int` e 1 vetor de 100 caracteres do tipo `char`:
```c
    int n, i;
    char S[100];
```
`n` indica o número de cursos que Vitória vai considerar, `i` é a variável auxiliar para a estrutura `for` e `S` é o nome do curso que vai ser considerado.

Para ler a variável `n`, usa-se `scanf`:
```c
    scanf("%d", &n);
```
Para ler um vetor de `chars`, também conhecido como `string`, é utilizado a função `fgets`. Vamos ler `S` N vezes então usaremos o `for`:
```c
    for(i=0;i<n;i++)
      fgets(S, sizeof(S), stdin);       
```
`sizeof` indica o tamanho do vetor `S`. O nome que vai ser guardado no vetor não pode ter mais de 100 caracteres. O valor `S` será lido inúmeras vezes e manterá apenas o nome do último curso escrito.

Como mostra o enunciado, Vitória deve cursar Ciência da Comutação, sendo assim usando a função `printf` escreveremos na tela sempre `Ciencia da Computacao`. O `\n` no fim serve para pular uma linha na tela depois de mostrar o texto:
```c
    printf("Ciencia da Computacao\n");
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre strings: [Strings](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
