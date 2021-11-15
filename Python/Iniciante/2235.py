# Problema 2235 - Beecrowd - Iniciante - Nível 1

# Leitura dos dados
a, b, c = map(int, input().split(' '))

# Comparações para verificação de resultado
if(a == b or a == c or b == c):
  print("S")
else:
  if(a + b == c or a + c == b or b + c == a):
    print("S")
  else:
    print("N")
