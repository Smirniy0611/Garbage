# Запишем
# Демонстрирует запись в текстовый файл
print('Создаю текстовый файл методом write().')
text_file = open('write_it.txt', 'w', encoding='utf-8')
text_file.write('Строка 1\n')
text_file.write('Это строка 2\n')
text_file.write('Этой строке достался номер 3\n')
# Попробуем записать текст в файл одной командой
text_file.write('Строка 1 \nЭто строка 2 \nЭтой строке достался номер 3\n')
text_file.close()
text_file = open('write_it.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()

# Пробуем метод writelines
text_file = open('write_it.txt', 'w', encoding='utf-8')
text_file.writelines('стр1,\n '
                     'стр2,\n '
                     'стр3\n')
text_file.close()

text_file = open('write_it.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()