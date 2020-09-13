# Problema:

Rafael odeia pegar chuva, e para evitá-la ele começou a usar um sistema de previsão do tempo. Neste sistema ele consegue prever se irá chover no horário em que ele vai para o trabalho e/ou no horário que ele volta do
trabalho.

Rafael também odeia carregar guarda-chuva quando não está chovendo. Para evitar isso, ele vai comprar vários guarda-chuvas e deixá-los guardados em casa e no escritório, e só vai usá-los quando estiver chovendo. Ou seja, se estiver chovendo na hora de ir para o trabalho, ele vai pegar um guarda-chuva que está em sua casa, usá-lo no caminho para o trabalho, e deixá-lo lá. De maneira semelhante, se estiver chovendo na hora de voltar para casa, ele vai pegar um guarda-chuva que está no escritório, usá-lo no caminho para casa, e deixá-lo lá.

Dadas as previsões meteorológicas, descubra quantos guarda-chuvas Rafael deve comprar e guardar em casa e no escritório, de modo que ele nunca se molhe e nunca precise carregar o guarda-chuva quando não estiver chovendo.
 
**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2813

# Resoluçāo:

A solução deste exercício consiste em fazer verificações se o caminho de ida/volta está chovendo e a quantidade de guarda chuvas que está sobrando a partir disso, aumentamos ou diminuimos a quantidade de guarda chuva a comprar ou o que estão sobrando.


Primeiramente, iremos importar a biblioteca `stdlib.h`, pois utilizarmos a função `malloc()` para fazer alocação dinâmica, e também importaremos a biblioteca `string.h` para usarmos a função `strcmp` a fim de fazer comparação entre duas strings.

```c
    #include <stdlib.h>
    #include <string.h>
```

Então, iremos declarar as nossas variáveis inteiras. O inteiro `n` é o número de casos em que iremos analisar, e `i` é uma variável auxiliar para laços.

```c
    int n, i;
```

Estas variáveis de ponteiros de caracteres, `ida` e `volta` irão guardar respectivamente, a previsão do tempo da ida e da volta. Note que iremos alocar elas dinamicamente, pois não sabemos previamente o tamanho delas.

```c
    char *ida = (char*) malloc(sizeof(char));
    char *volta = (char*) malloc(sizeof(char));
```
Os inteiros abaixo irão guardar os valores relacionados a quantidade de guarda chuvas para comprar e guarda chuvas que estão sobrando. A variável `cCompra` corresponde aos guarda-chuvas da casa que é necessário comprar, `cSobra` são a quantidade de guarda-chuvas que estão sobrando em casa. Já `eCompra` são os guarda-chuvas do escritório que precisa ser comprado e `eSobra` são os guarda-chuvas do escritório que estão sobrando.

```c
    int cCompra = 0;
    int cSobra = 0;
    int eCompra = 0;
    int eSobra = 0;
```

Iremos usar a função `scanf` para guardar o valor de `n`. A seguinte, dentro do `for` será lido a previsão do tempo da ida e da volta. 

Assim, iremos fazer as verificações, a primeira condição usamos a função `strcmp` para verificar se `ida` é igual a chuva, e se o valor de `cSobra` é 0. Neste caso, vai chuver e não tem guarda-chuva em casa, então aumentamos em 1 as variáveis `cCompra` e `eSobra`, ou seja um guarda-chuva será comprado e a terá um de sobra.

No caso da ida estar chovendo e `cSobra` for maior que 0, decrementamos em uma unidade `cSobra` e aumentamos uma unidade de `eSobta`. Dessa forma o guarda-chuva de casa será usado e ele será deixado no trabalho.

Uma lógica semelhante é aplicada nas duas últimas condicionais, o que muda é que na verificação comparamos o valor da `volta` é igual a chuva e se `eSobra` é igual a 0 ou se é maior que 0. No caso em que `eSobra` é igual a 0 incrementamos em uma unidade as variáveis `cSobra` e `eCompra`. Caso `eSobra` for maior que 0 é aumentada em um a variável `cSobra` e diminuido em 1 `eSobra`.

```c
    scanf("%d",&n);
    
    for (i=0;i<n;i++){
        scanf("%s",ida);
        scanf("%s",volta);
   
        if(strcmp(ida, "chuva") == 0 && cSobra == 0){
            cCompra++;
            eSobra++;
        }
        else if(strcmp(ida, "chuva") == 0 && cSobra > 0){
            cSobra--;
            eSobra++;
        }
        
        if(strcmp(volta, "chuva") == 0 && eSobra == 0){
            cSobra++;
            eCompra++;  
        }
        else if(strcmp(volta, "chuva") == 0 && eSobra > 0){
            cSobra++;
            eSobra--; 
        }
    
    }
```

Ao final, imprimimos a quantidade de guarda-chuvas que é necessário comprar para casa e para o escritório.

```c
    printf("%d %d\n",cCompra, eCompra);
```


##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
