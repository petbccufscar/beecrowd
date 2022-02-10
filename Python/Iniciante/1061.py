# Problema 1061 - Beecrowd - Iniciante - Nível 3

# Inicialmente, recebemos as entradas formatadas e as dividimos com o
# método .split( ), assim, retirando apenas a informação que nos interessa da string.
diaA = int(input().split(' ')[1])
horaA, minutoA, segundoA = map(int, input().split(' : '))

diaB = int(input().split(' ')[1])
horaB, minutoB, segundoB = map(int, input().split(' : '))
 
# SEGUNDOS
# Substraimos a quantidade do 'segundo inicial' da quantidade do 'segundo final'
# e fazemos módulo por 60, assim, não ultrapassamos a quantidade de segundos existentes (59)
# e também, não temos uma unidade de tempo negativa.
segundos = (segundoB - segundoA) % 60

# MINUTOS
# Seguimos a mesma lógica anterior, mas nesse ponto, salvamos uma variável booleana com a
# informação: O 'segundo inicial' do evento é maior que o 'segundo final' do evento?
# Ao ser transformada com int(), podemos substrair 1 dos minutos, caso essa condição
# seja satisfeita.
segundoMaior = segundoA > segundoB
minutos = (minutoB - minutoA - int(segundoMaior)) % 60

# HORAS
# Seguimos a mesma lógica anterior, mas nesse ponto, salvamos uma variável booleana com a
# informação: O 'minuto inicial' do evento é maior que o 'minuto final' do evento?
# Ao ser transformada com int(), podemos substrair 1 das horas, caso essa condição
# seja satisfeita.
# Nesse caso, os segundos também influênciam para se ter uma unidade completa de hora,
# porém, já temos essa informação salva da variável anterior.
minutoMaior = minutoA > minutoB
horas = (horaB - horaA - (int(segundoMaior) or int(minutoMaior))) % 24

# DIAS
# Seguimos a mesma lógica anterior, mas nesse ponto, salvamos uma variável booleana com a
# informação: A 'hora inicial' do evento é maior que a 'hora final' do evento?
# Ao ser transformada com int(), podemos substrair 1 dos dias, caso essa condição
# seja satisfeita.
# Aqui, os segundos e os minutos também influênciam para se ter um dia completo,
# porém, já temos essa informação salva das variáveis anteriores.
horaMaior = horaA > horaB
dias = diaB - diaA - (int(segundoMaior) or int(minutoMaior) or int(horaMaior))
    
# Por fim, os dados são informados na tela utilizando f-string
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")