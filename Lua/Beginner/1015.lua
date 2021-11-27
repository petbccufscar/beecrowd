function distancia(x1, y1, x2, y2)
	dx = x1 - x2
	dy = y1 - y2
	return math.sqrt(dx^2 + dy^2)
end

x1, y1 = io.read('*n', '*n')
x2, y2 = io.read('*n', '*n')

print(string.format('%.4f', distancia(x1, y1, x2, y2)))