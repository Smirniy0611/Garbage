import hashlib

word = input().encode()
ciphers = list(hashlib.algorithms_guaranteed)
ciphers2 = {}
for i in ciphers:
    word_2 = hashlib.new(i)
    word_2.update(word)
    ciphers2[i] = word_2
for j, k in sorted(ciphers2.items()):
    print(j, k.hexdigest())