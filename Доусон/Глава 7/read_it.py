# Прочитаем
# Демонстрирует чтение из текстового файла
print('Открываю и закрываю файл.')
text_file = open('read_it.txt', 'r')
text_file.close()

print('\nЧитаю файл посимвольно:')
text_file = open('read_it.txt', 'r')
print(text_file.read(1))
print(text_file.read(6))
text_file.close()

print('\nЧитаю файл целиком:')
text_file = open('read_it.txt', 'r')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print('\nЧитаю одну строку посимвольно:')
text_file = open('read_it.txt', 'r')
print(text_file.readline(2))
print(text_file.readline(4))
text_file.close()

print('\nЧитаю одну строку целиком')
text_file = open('read_it.txt', 'r')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nЧитаю весь файл в список')
text_file = open('read_it.txt', 'r')
lines = text_file.readline()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print('\nПеребираю файл построчно')
text_file = open('read_it.txt', 'r')
for line in text_file:
    print(line)
text_file.close()