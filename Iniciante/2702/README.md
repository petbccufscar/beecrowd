# Problema:   
Em um longo voo, companhias aéreas oferecem uma refeição aos seus passageiros. Geralmente as aeromoças conduzem carrinhos contendo as refeições pelos corredores do avião. Quando o carrinho chega em sua fileira, você é questionado imediatamente: “Frango, bife, ou massa?”. Você sabe suas opções, mas você tem apenas alguns segundos para escolher e você não sabe qual a aparência de sua escolha pois seu vizinho ainda não abriu o embrulho…

A aeromoça deste voo decidiu alterar o procedimento. Primeiro ela vai perguntar a todos os passageiros qual sua escolha de refeição, e depois vai checar se o número de refeições disponíveis neste voo para cada escolha é suficiente.

Por exemplo, considere que o número de refeições de frango, bife e massa disponíveis são respectivamente (80, 20, 40), enquanto o número de passageiros que escolheu frango, bife e massa seja respectivamente (45,23, 48). Neste caso, onze pessoas seguramente ficaram sem suas respectivas escolhas de refeição, já que três passageiros que queriam bife e oito que gostariam de massa não poderão ser atendidos.

Dada a quantidade de refeições disponíveis para cada escolha e o número de refeições pedidas para cada escolha, você poderia por favor ajudar a aeromoça a determinar quantos passageiros seguramente não poderão ser atendidos?

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2702

# Resolução:

Começamos declarando as variaveis que iremos armazenar a quantidade de alimentos disponiveis, em seguida as variaveis que irão armazenar a quantidade que os passageiros pediram e outras tres variaveis para verificar se irá haver pedidos que não poderão ser atendidos. Juntamente com a declaração das variaveis realizamos a leitura dos valores.
```c
int frangoDisp, bifeDisp, massaDisp;
int frangoReq, bifeReq, massaReq;
int resFrango, resBife, resMassa;

scanf("%d %d %d", &frangoDisp, &bifeDisp, &massaDisp);
scanf("%d %d %d", &frangoReq, &bifeReq, &massaReq);
```


Para cada tipo de alimento sendo ele Frango, Bife ou Massa, teremos um bloco onde faremos o calculo de quantos alimentos faltaram, no caso do Frango iremos calcular o valor contido em `frangoDisp` menos o valor contido em `frangoReq`, com isso iremos ter algumas possibilidades de resultado:
- Caso de um numero negativo significa que tiveram mais pedidos do que alimento disponivel, então armazenamos este valor (negativo) em `resFrango`.
- Caso seja 0 ou um valor maior que 0 significa que foi possivel atender todos os pedidos, portanto iremos definir o valor em `resFrango` como 0, para que não atrapalhe na contagem de pedidos que não foram atendidos. 
```c
resFrango = frangoDisp - frangoReq;
if (resFrango > 0)
	resFrango = 0;
```


Ao final iremos imprimir apenas quantos passageiros não foram atendidos, para isso realizamos a soma dos valores contidos em `resFrango`, `resBife` e `resMassa`. Como são valores negativos realizamos a inversão do valor e imprimimos este na tela.
```c
printf("%d\n", -(resFrango + resBife + resMassa));
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com