valor = io.read('*n')
print(valor)

notas = {100, 50, 20, 10, 5, 2, 1}

for _, nota in pairs(notas) do
	quantidade = 0
	
	while valor >= nota do
		valor = valor - nota
		quantidade = quantidade + 1
	end
	
	print(string.format('%d nota(s) de R$ %d,00', quantidade, nota))
end