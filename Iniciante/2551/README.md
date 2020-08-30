# Problema

A grande Maratona de Rua de Curitiba irá ocorrer nos próximos dias! Vários atletas estão treinando há dias para o grande dia da corrida. Flávio é um dos atletas que está treinando diariamente para se sair bem na corrida. Ele tem corrido todas as manhãs nas pistas próximas de sua casa.

Os treinos do garoto são monitorados por um aplicativo em seu celular. Após cada treino, Flávio sabe tanto a duração do treino quanto a distância total percorrida. Com essas informações, ele consegue determinar a velocidade média obtida em cada treino.

Flávio está muito preocupado com a evolução de seu desempenho nos treinos, e em particular com seu recorde de velocidade média. Tal recorde é batido em um dado treino quando a velocidade média para este treino é maior que todas as velocidades médias obtidas nos treinos anteriores. Ajude Flávio a determinar em quais treinos ele conseguiu bater seu recorde.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2551

# Resolução

Para resolver o problema, iremos receber os valores de distância e tempo e calcular se são maiores que os recordes anteriores. Caso forem, exibimo-nos.

Começamos declarando as variáveis que serão utilizadas no problema, todas do tipo inteiro. Serão elas:
- `N`, para o número de treinos feitos;
- `recorde_D`, para o recorde de distância;
- `recorde_T`, para o recorde de tempo;
- `i`, para as iterações das estruturas de repetição;
- `T`, para o último tempo recebido pelo programa;
- `D`, para a última distância recebida pelo programa.
```c
 int N, recorde_D, recorde_T, i, T, D;
 ```

Em seguida, iniciamos nossa estrutura de repetição `while`. Seu critério de parada será a leitura de um EOF (End of File - Fim do arquivo) pela estrutura `scanf` na variável `N`.
```c
  while (scanf("%d", &N) != EOF) {
```

A variável `recorde_D` é inicializada com 0, visto que não lemos nenhuma distância ainda.
```c
	recorde_D = 0;
```

Porém, para a variável `recorde_T`, inicializaremos com 1 para que as contas que faremos posteriormente para calcular as médias não sejam anuladas.
```c
	recorde_T = 1;
```

Faremos uma estrutura de repetição `for` para ler os valores de cada treino. Esta estrutura se repetirá `N` vezes e, em cada repetição, lerá os valores de tempo e distância com a estrutura `scanf`.
```c
    for (i = 1; i <= N; i++) {
      scanf("%d %d", &T, &D);
```

Para realizar a conta dos recordes, faremos as médias do treino atual e do treino do recorde. Para isso, utilizaremos o cálculo da média dividindo a distância e o tempo, comparando ambas médias (tanto do atual quanto do recorde). Assim, faremos uma [regra de 3](https://www.somatematica.com.br/fundam/regra3s.php) para podermos multiplicar distâncias e tempos para compará-los, da seguinte forma:

distancia     recorde_D
---------  >  --------- 
tempo         recorde_T  

Utilizando a multiplicação cruzada, temos:

distancia * recorde_T > recorde_D * tempo

Caso a média do treino recebido seja maior do que a média do recorde anterior, exibimos qual dos treinos bateu o recorde e atualizamos a distância recorde e o tempo recorde nas variáveis.
```c
      if (D*recorde_T > recorde_D*T) {
        printf("%d\n", i);
        recorde_D = D;
        recorde_T = T;
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

