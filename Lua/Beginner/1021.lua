valor = io.read('*n')

notas = {100, 50, 20, 10, 5, 2}
moedas = {1, 0.5, 0.25, 0.1, 0.05, 0.01}

print('NOTAS:')

for _, nota in pairs(notas) do
	quantidade = 0
	
	while valor >= nota do
		valor = valor - nota
		quantidade = quantidade + 1
	end
	
	print(string.format('%d nota(s) de R$ %.2f', quantidade, nota))
end

print('MOEDAS:')

for _, moeda in pairs(moedas) do
	quantidade = 0
	
	while valor >= moeda do
		valor = valor - moeda
		quantidade = quantidade + 1
	end
	
	print(string.format('%d moeda(s) de R$ %.2f', quantidade, moeda))
end