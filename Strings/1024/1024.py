# -*- coding: utf-8 -*-
from string import ascii_letters

def first_run(letter):
    if letter in ascii_letters:
        letter = chr(ord(letter) + 3)
    return letter


n = int(input())
i = 0
while i < n:
    word = input()
    mid = len(word) // 2
    aux = list(map(first_run, word))[::-1]
    a = aux[:mid]
    b = list(map(lambda x: chr(ord(x)-1), aux[mid:]))
    print("".join(a+b))
    i += 1
