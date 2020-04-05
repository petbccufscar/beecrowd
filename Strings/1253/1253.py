from functools import partial

def caesar(letter, rot):
    return chr(((ord(letter) - ord('A') - rot) % 26) + ord('A'))

n = int(input())
for _ in range(n):
    word = input()
    rot = int(input())
    print("".join(list(map(partial(caesar, rot=rot), word))))
