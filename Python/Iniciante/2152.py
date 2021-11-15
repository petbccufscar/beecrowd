# Problema 2152 - Beecrowd - Iniciante - Nível 1

# Leitura da variável 'n' que indica quantas vezes será feito a leitura dos horários e o valor do sensor
n = int(input())

# Início do loop de leituras e prints
for i in range(n):
	# Leitura das variávies x(hora),y(minuto) e z(sensor)
	x, y, z = map(int, input().split(' '))
	
	# Ajustando os horários caso hora e minuto sejam menores que 10, para o formato hh:mm
	if (x<10) and (y<10):
		if(z==1):
			print(f'0{x}:0{y} - A porta abriu!')
		else:
			print(f'0{x}:0{y} - A porta fechou!')

	# Ajustando os horários caso a hora seja menor que 10, para o formato hh:mm
	elif (x<10) and (y>=10):
		if(z==1):
			print(f'0{x}:{y} - A porta abriu!')
		else:
			print(f'0{x}:{y} - A porta fechou!')

	# Ajustando os horários caso o minuto seja menor que 10, para o formato hh:mm
	elif (x>=10) and (y<10):
		if(z==1):
			print(f'{x}:0{y} - A porta abriu!')
		else:
			print(f'{x}:0{y} - A porta fechou!')
  
	# Printando hora e minuto caso sejam ambas maiores que 10, para o formato hh:mm
	else:
		if(z==1):
			print(f'{x}:{y} - A porta abriu!')
		else:
			print(f'{x}:{y} - A porta fechou!')

