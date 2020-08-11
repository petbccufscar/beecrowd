# Problema:
Amarelinha provavelmente é a brincadeira em que as crianças da vila mais se divertem, porém a mesma vem causando um bom tempo de discussão e choro nas crianças que a praticam. A causa do transtorno é para decidir quem será o próximo a pular, mas recentemente Quico (O gênio!) teve uma grande ideia para solucionar o problema. Basicamente a brincadeira só poderá ser jogada de dois em dois jogadores e para escolher o próximo jogador Quico indicou o uso do tradicional método par ou ímpar, onde os dois jogadores informam um número e se a soma desses números for par o jogador que escolheu PAR ganha ou vice verso. Entretanto a utilização desse método vem deixando o Quico louco, louco, louco... E por esse motivo ele pediu a sua ajuda! Solicitou a você um programa que dado o nome dos jogadores, suas respectivas escolhas PAR ou ÍMPAR e os números, informe quem foi o vencedor.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1914
 
# Resolução:

Primeiro instanciámos as variáveis necessárias, sendo elas: 1 inteiro(`QT` para o numero de casos de teste); 2 `long long` (para armazenar os números), iremos utilizar esse tipo pois os valores a serem lidos podem alcançar 10⁹, assim precisaremos um espaço de memoria muito maior para armazenamento; e 4 `char`(para armazenar o nome dos 2 jogadores, que podem alcançar 100 caracteres; para `escolha[6]`, iremos utilizar somente 1 variável tendo em vista que se sabemos a do `jogador2` podemos inferir a escolha do `jogador`; e para o `resultado`).
Começamos lendo o número de casos de teste.

```c
    int QT;
    long long num, num2;
    char jogador[100], jogador2[100], escolha[6], resultado;

    scanf("%d", &QT);
```
 
Agora iremos utilizar um `while(QT--)` para passar por todos os casos de teste, decrementando `QT` ao final do `while()` ate que `QT` seja `0`. Dentro dele iremos ler todos os valores do caso de teste referente, sendo eles: `jogador`, `escolha`, `jogador2`, `escolha`, `num`, `num2`, respectivamente nessa ordem.

Obs: Como estamos utilizando um `long long` (que continua sendo um inteiro, mas nesse caso com mais espaço na memoria), a maneira de lermos ele também muda, temos que utilizar `%lld` ao invés de `%d`

Após ler iremos utilizar um `if()` para verificar o `resultado`, para isso utilizaremos o resto de uma divisão inteira por 2 (`%2`), sendo que se o resto de `num` for igual ao resto de `num2` (`num % 2 == num2 % 2`) o `resultado` é par (`P`), caso contrario é ímpar (`I`).

Por fim comparamos o `resultado` com o primeiro caractere do `escolha` (que esta com a escolha do `jogador2`), caso sejam iguais, imprimimos `jogador2`, caso contrario imprimimos `jogador`.

```c
    while (QT--) {
        scanf("%s", jogador);
        scanf("%s", escolha);
        scanf("%s", jogador2); 
        scanf("%s", escolha);
        scanf("%lld %lld", &num, &num2);

        if (num % 2 == num2 % 2) resultado = 'P';
        else resultado = 'I';

        if (escolha[0] == resultado) printf("%s\n", jogador2);
        else printf("%s\n", jogador);
    }
```

##### Para aprender um pouco mais sobre o laço de repetição While: [While](http://linguagemc.com.br/o-comando-while-em-c/)

##### Para aprender um pouco mais sobre tipos de Variáveis: [Variáveis](https://en.wikipedia.org/wiki/C_data_types)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com