# Problema:

Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

# Resolução:

Primeiro, precisamos declarar as variáveis para representar as 4 notas, a média e a nota do exame. 
Como esses valores tem casa decimal, utilizamos o `double`.

    double n1, n2, n3, n4, media, exame;

Para leitura das notas, utilizamos a função `scanf`. Usamos `%lf` para ler valores do tipo double:

    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);

Agora precisamos calcular a média ponderada com os pesos descritos. Basicamente, a média ponderada é a soma dos fatores com cada fator sendo multiplicado por um número, que chamamos de peso; E essa soma será dividida pela soma dos pesos. No caso a soma dos pesos é igual a 10:

    media = (2*n1 + 3*n2 + 4*n3 + n4)/10;


Com a média calculada, precisamos apresentá-la na tela, como pedido no problema. Para isso, utilizamos o `printf`: 

    printf("Media: %.1lf\n", media);

Note que normalmente usamos `%lf` para representar um double, aqui adicionamos .1 `(%.1lf)`, isso serve para que só apresente uma casa decimal na tela (`.2` seriam duas casas e assim por diante). 

Agora precisamos dizer se o aluno foi aprovado (caso onde a média é maior ou igual a 7), apresentamos a mensagem de "Aluno aprovado" com a estrutura `printf`

        if(media >= 7)
            printf("Aluno aprovado.\n");

Ou caso ele seja reprovado (onde a média é menor que 5), apresentamos a mensagem "Aluno reprovado".

        else if(media < 5)
            printf("Aluno reprovado.\n");

Caso não esteja nos casos abordados, a média é um valor entre 5.0 e 6.9, inclusive estes, deixando o aluno de exame. Neste caso, recebereremos como entrada sua nota no exame (então lemos com o `scanf`) e precisamos apresentá-la em tela (com  `printf`):

    else { 
        printf("Aluno em exame.\n");
        scanf("%lf", &exame);
        printf("Nota do exame: %.1lf\n", exame);

Além disso, precisamos recalcular a média agora, a nova média será a média da nota final e da nota no exame:

    media = (media + exame)/2;

Como descrito no problema, se a nova média for maior ou igual a 5, o aluno será aprovado, se não, ele está reprovado:

    if(media >= 5)
        printf("Aluno aprovado.\n");
    else
        printf("Aluno reprovado.\n");


Por fim, apresentamos a nova média final na tela, como descrito no problema.

    printf("Media final: %.1lf\n", media);


###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
##### Para relembrar média ponderada: [Média Ponderada](https://www.somatematica.com.br/fundam/medias2.php) 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com