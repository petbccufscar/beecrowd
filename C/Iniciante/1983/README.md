# Problema:    
As aulas do Prof. Jatobá estão dando o que falar. Os representantes do MEC vieram até a UNIME de Lauro de Freitas para saber mais detalhes sobre essa nova forma de ensinar Algoritmos. Além disso, eles queriam selecionar 1 aluno para participar da OBI-Tec (Olimpíada Brasileira de Informática Nível Técnica) e representar a rede Kroton na competição, pois sabem que lá estão os melhores. Para selecionar o melhor, eles têm disponível uma lista com o número de inscrição de cada aluno e a sua respectiva nota na disciplina. Sua tarefa é ajudar o pessoal do MEC a encontrar o aluno mais apto a representar a instituição e quem sabe garantir sua vaga. Só tem um detalhe, se a nota mais alta não for maior ou igual a 8, você deverá imprimir “Minimum note not reached”.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1983


# Resolução:
Devemos comparar todas as N notas, selecionar a maior e exibir o número da matrícula desse aluno. Para isso, vamos assumir que a primeira nota é sempre a maior e comparar com as notas seguintes - caso alguma nota seja maior, atualizamos a nota e a matrícula do aluno.  

Começamos declarando as variáveis necessárias para o problema. `N` será o número de alunos a serem lidos e `i` será usada para realizar um loop para os N alunos. As variáveis `matricula` e `nota` serão lidas para todos os alunos, enquanto as variáveis `matriculaMaior` e `notaMaior` somente serão atualizadas quando alguma nota for maior que a primeira lida.  
Obs: como as notas possuem valores decimais, devem ser declaradas como `float`.

```c
int N, i, matricula, matriculaMaior;
float nota, notaMaior;
```

Faremos a leitura do número de alunos:

```c
scanf("%d",&N);
```

Sabendo que sempre haverá pelo menos 1 aluno, vamos assumir que este tem a maior nota no início:

```c
scanf("%d %f", &matriculaMaior, &notaMaior);
```

Como já fizemos uma leitura de aluno, começaremos nosso loop `for` com `i = 1` ao invés de `i = 0`.  
Faremos a leitura de cada aluno nas variáveis `matricula` e `nota`. Caso sua nota seja maior que a última maior nota lida, atualizamos as variáveis `matriculaMaior` e `notaMaior`.

```c
for (i = 1; i < N; i++) {
    scanf("%d %f", &matricula, &nota);

    if (nota > notaMaior) {
        matriculaMaior = matricula;
        notaMaior = nota;
    }
}
```

Por fim, devemos verificar se a maior nota entre os alunos é maior ou igual a 8. Se sim, exibimos a matrícula do aluno. Caso contrário, exibimos a frase dada no enunciado.

```c
if (notaMaior >= 8) {
    printf("%d\n", matriculaMaior);
}

else {
    printf("Minimum note not reached\n");
}
```

##### Para revisar variáveis de ponto flutuante: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)
##### Para relembrar sobre o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
