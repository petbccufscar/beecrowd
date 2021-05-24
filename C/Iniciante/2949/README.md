# Problema:

Frodo era um pequeno hobbit (pessoinhas pequenas e de pés peludos) que vivia tranquilamente no Condado, tomando seus vários cafés da manhã recheados de muitos alimentos suculentos que a dieta de um bom hobbit proporciona.
Certo dia, seu tio Bilbo lhe entrega seu famoso anel dourado, e Gandalf, um mago muito “bacanudo”, diz a Frodo que esse anel não era normal e que deveria ser jogado na Montanha da Perdição, para que um grande mal fosse evitado. Para essa jornada, foi formada uma comitiva, composta de anões, elfos, humanos, hobbits e magos.
Frodo deseja saber a quantidade de cada raça que irá com ele para a jornada. Dada uma lista das pessoas que se alistaram, faça um relatório para Frodo da comitiva.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2949
 
 
# Resolução:

Começando pela declaração de variáveis, primeiramente uma `string` `nome[100]` que nada mais é que um vetor de caracteres, declarada inicialmente com 100 posições para evitar problemas do nome exceder as posições da string; Uma variável `char raca` que será utilizada para armazenar a raça da pessoa; `pessoas` que armazenará quantas pessoas estão partindo para a jornada; e variáveis de contagem para cada raça existente `hobbits` `magos` `humanos` `elfos` `anoes`, todas inicializadas com 0 pois para fins de contagem, esse é o valor nulo (que não tem valor para uma soma).

#### Aqui utilizamos uma variável `int` para cada raça existente no problema, pois eram apenas 5, em casos com muitas raças é altamente recomendável o uso de um vetor e criar uma relação entre as posições e as raças.

```c
    char nome[100], raca;
    int pessoas, i;
    int hobbits = 0, magos = 0, humanos = 0, elfos = 0, anoes = 0;
```

Efetuamos a leitura de quantas pessoas irão para a jornada e armazenamos na variável `pessoas`.

```c
    scanf("%d",&pessoas);
```

Assim, podemos fazer um loop `for` que conte até `pessoas` para receber toda a entrada.
Efetuamos a leitura do `nome` e `raca` com a função `scanf` 
E analisamos o valor da variável `raca` com a estrutura `switch case`, caso `raca == 'A'` incrementamos a variável `anoes`, caso `raca == 'E` incrementamos em `elfos` e assim para as 5 raças existentes.


```c
for(i = 0; i < pessoas; i++){
    scanf("%s %c",&nome,&raca);
    switch(raca){
        case 'A':   
            anoes++;    
            break;
        case 'E':   
            elfos++;
            break;
        case 'H':   
            humanos++;  
            break;
        case 'M':   
            magos++;    
            break;
        case 'X':
            hobbits++;
            break;
    }
}
```

Ao término do loop for, temos o valor de cada raça em sua respectiva variável, portanto podemos fazer o print da seguinte forma: 

```c
 printf("%d Hobbit(s)\n%d Humano(s)\n%d Elfo(s)\n%d Anao(s)\n%d Mago(s)\n",hobbits,humanos,elfos,anoes,magos);
```

#### Reveja a estrutura switch case: [Aqui](http://linguagemc.com.br/o-comando-switch-case-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
