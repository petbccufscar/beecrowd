# Problema

Neste problema, para acabar com a dúvida do Paulinho, vamos simular esse jogo milhares de vezes e contar quantas vezes o jogador ganhou o carro. Vamos supor que:

• O jogador sempre escolhe inicialmente a porta 1;

• O jogador sempre troca de porta, depois que o apresentador revela um bode abrindo uma das duas portas que não foram escolhidas inicialmente.

Nessas condições, em um jogo, dado o número da porta que contém o carro, veja que podemos saber exatamente se o jogador vai ganhar ou não o carro.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2879

# Resolução

Para resolver o problema, é necessario muita atenção às condições apresentadas no enunciado. Iremos receber o nº de jogos e qual porta contém o carro em cada um dos jogos. Visto que o jogador sempre escolhe a 1ª porta mas, antes de abrí-la, troca de porta, iremos contabilizar o número de casos em que o carro não está na porta 1 (já que o jogador sempre desiste da porta 1 para mudar para outra). Com isso, contabilizamos o número de vezes em que o jogador consegue o carro (isto é, quando está na porta 2 ou 3).

Começamos declarando as variáveis que serão utilizadas no exercício, todas do tipo inteiro. Serão elas:
* `jogos`, para o número de jogos que serão recebidos;
* `carro`, para a porta que contém o carro em cada jogo;
* `ganhou`, para o contador de vezes em que o jogador ganhou o carro.
```c
    int jogos, carro, ganhou;
```

Inicializamos a variável `ganhou` com 0, visto que nenhum jogo foi lido ainda.
```c
    ganhou = 0;
```

Recebemos o número de jogos que serão lidos em seguida, utilizando a função `scanf`.
```c
	scanf("%d", &jogos);
```

Agora, utilizaremos a estrutura de repetição `while` para receber cada jogo. Usaremos a variável `jogos` que, a cada loop da estrutura, diminuirá 1, até que chegue em 0, parando o `while`. 
```c
	while (jogos--)
```

Faremos a leitura de cada jogo com a estrutura `scanf`, e salvaremos na variável `carro` qual porta é a escolhida do jogo.
```c
    scanf("%d", &carro);
```

Caso a porta do carro não seja a 1ª (que é a que o jogador sempre muda e, com isso, nunca escolhe no final), consideramos que o jogador acertou e, portanto ganhou o carro neste jogo.
```c
    if (carro != 1)
        ++ganhou;
```

Por fim, exibimos quantas vezes o jogador ganhou o carro no fim de todos os jogos
```c
	printf("%d\n", ganhou);
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
