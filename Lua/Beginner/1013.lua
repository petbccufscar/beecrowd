function maior(a, b)
	return (a + b + math.abs(a - b)) / 2
end

A, B, C = io.read('*n', '*n', '*n')
print(string.format('%d eh o maior', maior(maior(A, B), C)))