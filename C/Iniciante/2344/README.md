# Problema:   

Rosy é uma talentosa professora do Ensino Médio que já ganhou muitos prêmios pela qualidade de sua aula. Seu reconhecimento foi tamanho que foi convidada a dar aulas em uma escola da Inglaterra. Mesmo falando bem inglês, Rosy ficou um pouco apreensiva com a responsabilidade, mas resolveu aceitar a proposta e encará-la como um bom desafio.

Tudo ocorreu bem para Rosy até o dia da prova. Acostumada a dar notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova dos alunos da Inglaterra. No entanto, os alunos acharam estranho, pois na Inglaterra o sistema de notas é diferente: as notas devem ser dadas como conceitos de A a E. O conceito A é o mais alto, enquanto o conceito E é o mais baixo.

O problema é que Rosy já deu as notas no sistema numérico, e terá que converter as notas para o sistema de letras. Porém, Rosy precisa preparar as próximas aulas (para manter a qualidade que a tornou reconhecida), e não tem tempo suficiente para fazer a conversão das notas manualmente.

Você deve escrever um programa que recebe uma nota no sistema numérico e determina o conceito correspondente.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2344

# Resolução:

Iniciaremos a resolução desse problema com a declaração da variável que iremos armazenar o valor que será inserido. Após isso realizamos a leitura do valor através da função `scanf`
```c
int n;
scanf("%d", &n);
```


Após armazenado o valor, iremos realizar uma sequência de comparações para selecionar em qual intervalo o valor inserido se encontra, ao entrar no `if` correspondente realizamos a impressão do conceito atribuído à aquele intervalor de notas.
```c
if (n == 0)
	printf("E\n");
else if (n >= 1 && n <= 35)
	printf("D\n");
else if (n >= 36 && n <= 60)
	printf("C\n");
else if (n >= 61 && n <= 85)
	printf("B\n");
else
	printf("A\n");
```

##### Para revisar sobre: [Titulo](link)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
