valores = list(map(int,input().split()))

print(f'A={valores[0]}, B={valores[1]}, C={valores[2]}')

soma = valores[0] + valores[1]

if soma > valores[2]:
  print(f'A soma ({soma}) é maior que C({valores[2]})')
else:
  print('A soma é menor')
