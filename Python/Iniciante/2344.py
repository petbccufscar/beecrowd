# Problema 2344 - URI - Iniciante - Nível 1

# Lendo a nota
nota = int(input())

# Fazendo a conversão da nota
if(nota == 0):
  print('E')
elif(nota >= 1 and nota <= 35):
  print('D')
elif(nota >= 36 and nota <= 60):
  print('C')
elif(nota >= 61 and nota <= 85):
  print('B')
else:
    print('A')


