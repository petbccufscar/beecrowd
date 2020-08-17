# Problema:   
Seu Júlio é proprietário de um grande apiário situado no interior da Paraíba. Todo ano, semestralmente, seu Júlio coleta o mel produzido pelas abelhas da sua propriedade e armazena-o em um recipiente de formato CILÍNDRICO para que facilite o transporte do mel para os estabelecimentos que encomendam esse produto natural para a comercialização.
Certa vez seu Júlio percebeu que devido a um crescimento na produção do mel, em relação ao semestre anterior, o recipiente que possuia não suportaria o volume de mel produzido por suas abelhas. Seu Júlio precisa agora que você faça um programa que informado o volume de mel em cm3 e o diâmetro da parte interna do recipiente em cm, calcule e mostre:

\- Qual deve ser a altura(em cm) da parte interna do recipiente;

\- A área(em cm2) da boca(entrada) do recipiente.

Obs.: Considere π = 3.14

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2029

# Resolução:

Iniciamos a resolução através da declaração de algumas variaveis, algumas destas serão passadas e outros usaremos para armazenar valores durante o processo 
```c
double volume, diametro, altura, area, raio;
```


Utilizaremos o laço de repetição `while` juntamente com uma verificação se chegamos ao final do arquivo passado, para isso fazemos uma comparação com o valor `EOF` que é o retorno da função `scanf` caso tenha acabado. Caso seja negativo, prosseguimos com à resolução com os valores já lidos e armazenados nas variáveis `volume` e `diametro`
```c
while(scanf("%lf%lf", &volume, &diametro)!=EOF){
```


Dentro deste do laço, para cada dois valores de volume e diâmetros passados iremos realizar um calculo com o objetivo de encontrar a altura e área que o recipiente deverá possuir.
* Para o calculo do raio basta dividirmos o valor do diâmetro que foi passado por 2. 
* Para calcular a área foi dito para considerar PI como 3,14 desta forma basta multiplicar PI por raio ao quadrado (raio\*raio).
* E para a altura basta dividirmos o valor contido em volume pelo valor encontrado e armazenado na variável `area`
```c
raio = diametro/2;
area = 3.14*raio*raio;
altura = volume/area;
```


Ao final de cada iteração do laço `while` realizamos a impressão dos respectivos valores de altura e área seguindo a formatação proposta pelo problema
```c
printf("ALTURA = %.2lf\n", altura);
printf("AREA = %.2lf\n", area);	
```


    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
