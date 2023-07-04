import openpyxl

volume = int(input('Введите объем здания: '))
floor = int(input('Укажите количество этажей здания: '))
height = int(input('Введите высоту здания: '))
category_1 = int(input('Введите категорию сложности работ (1,2 или 3): '))
category_2 = int(input('Введите категорию сложности здания (1,2 или 3): '))
book = openpyxl.open('data.xlsx', read_only=True)  # открыли файл только для чтения
sheet = book.active  # позиционируемся на 1-ом листе
i = 2

tab_1 = {(1, 1): 7, (1, 2): 8, (1, 3): 9,
         (2, 1): 11, (2, 2): 12, (2, 3): 13,
         (3, 1): 15, (3, 2): 16, (3, 3): 17}

tab_2 = {(1, 1): 26, (1, 2): 27, (1, 3): 28,
         (2, 1): 30, (2, 2): 31, (2, 3): 32,
         (3, 1): 34, (3, 2): 35, (3, 3): 36}

tab_3 = {(1, 1): 45, (1, 2): 46, (1, 3): 47,
         (2, 1): 49, (2, 2): 50, (2, 3): 51,
         (3, 1): 53, (3, 2): 54, (3, 3): 55}

tab_4 = {(1, 1): 64, (1, 2): 65, (1, 3): 66,
         (2, 1): 68, (2, 2): 69, (2, 3): 70,
         (3, 1): 72, (3, 2): 73, (3, 3): 74}

if floor == 1:
    k = tab_1[(category_1, category_2)]
    j = tab_3[(category_1, category_2)]
else:
    k = tab_2[(category_1, category_2)]
    j = tab_4[(category_1, category_2)]

while height != sheet[4][i].value:
    i += 1

cost_obm = sheet[k][i].value
cost_obsl = sheet[j][i].value

K_inf = 4.91  # II кв. 2022 (http://www.consultant.ru/document/cons_doc_LAW_39473/)

print('Стоимость обмерных работ составит: ', int(volume * 0.01 * cost_obm * K_inf))
print('Стоимость обследовательских работ составит: ', int(volume * 0.01 * cost_obsl * K_inf))

book.close()
