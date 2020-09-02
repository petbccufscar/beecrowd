# Problema:

Conta-se nos arredores de Montes Claros que, há muito tempo no mercado municipal, Sebastião e seus companheiros de trabalho sempre jogam uma partida de adivinhação após a entrega dos produtos agrícolas colhidos na semana que se passou. O jogo, que se chama Adivinhe Onde o Feijão Está'', consiste em esconder um grão de feijão em um de quatro copos opacos e, depois de embaralhá-los, o apostador deve adivinhar em qual copo o legume está.

Neste ano, devido ao grande sucesso cultural e histórico e à enorme quantidade de pessoas que praticam este jogo no mercado municipal, a prefeitura resolveu realizar um campeonato de Adivinhe Onde o Feijão Está''. Entretanto, ela necessita de um programa para mostrar aos expectadores onde o feijão estava após o fim de uma partida. Sabendo que a próxima Maratona Mineira de Programação ocorrerá na cidade, ela logo encomendou uma solução aos exímios programadores. Desta forma, você deve auxiliar a organização nesta missão com um programa que informe, ao fim de uma partida, onde o feijão esteve

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2791
 
 
# Resolução:

Começando pela declaração de variáveis, criamos uma variável do tipo inteiro `copo`, um iterador `i` para realizar o loop `for` e uma variável para armazenar a posição do feijao, chamada de `feijao_pos`

```c
int i, copo, feijao_pos;
```

Para receber os 4 valores, utilizamos um loop `for(i = 0; i < 4; i++)` começado em 0, enquanto o iterador ser < 4 (intervalo 0,1,2,3), com passo 1.

Dentro do loop, recebemos um inteiro por meio da função `scanf` e armazenamos na variável `copo`.

Assim, podemos verificar se o valor inserido nessa variável é 1, que é o que buscamos. Caso positivo, armazenamos a posição `i+1` na variável `feijao_pos` porém, utilizamos.

Utilizamos `i+1` pois estamos trabalhando em um intervalo diferente do padrão, já que os copos vão de 1 a 4 e nosso `for` de 0 a 3.

```c
   for(i = 0; i < 4; i++){
        scanf("%d",&copo);
        if(copo == 1){
            feijao_pos = i + 1;
        }
    }
```

Por fim, imprimimos a posição do feijão na tela, com a função `printf`

```c
printf("%d\n",feijao_pos);
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com