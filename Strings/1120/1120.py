from itertools import dropwhile

a, b = input().split()
while a != '0' and b != '0':
    l = list(filter(lambda x: x!=a, b))
    if l:
        result = "".join(dropwhile(lambda x: x=='0', l))
        print(result if result else 0)
    else:
        print(0)
    a, b = input().split()
