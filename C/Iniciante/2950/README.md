# Problema:

Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.



##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2950
 
 
# Resolução:

Começando pela declaração de variáveis, teremos 3 para a entrada, `N` `X` `Y` do tipo `int`, que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
E para armazenar o resultado do ICM, utilizaremos a variável `icm`.

```c
    float N, X, Y;
    float icm;
```

Agora, receberemos os valores de entrada por meio da função `scanf`

```c
    scanf("%f %f %f",&N,&X,&Y);
```

Com os valores já nas variáveis, podemos efetuar a conta do ICM igual proposto pelo enunciado e imprimir na tela com a função `printf`

```c
    icm = (N / (X + Y));
    printf("%.2f\n",icm);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
