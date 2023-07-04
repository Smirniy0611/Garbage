import hashlib

a = 'I love Python'
h1 = hashlib.md5(b'I love Python')
h2 = hashlib.sha256(b'a')
h3 = hashlib.sha3_512(b'a')
print(h2)
print(h1.hexdigest())
print(h2.hexdigest())
print(h3.hexdigest())

h4 = input('Enter password ')
h22 = hashlib.md5(h4.encode())
print(h22.hexdigest())

h5 = hashlib.sha256(b'Python')
h5 = h5.hexdigest()
h6 = input('Enter password:  ')
h6 = hashlib.sha256(h6.encode())
if h6.hexdigest() == h5:
    print('Ok')
else:
    print('No')

s1 = 'Питон'
s2 = s1.encode('utf-8')
print(s2)
s3 = s2.decode('utf-8')
print(s3)

s_list = list(hashlib.algorithms_guaranteed)
print(s_list)

