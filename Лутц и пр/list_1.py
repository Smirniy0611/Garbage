L = [123, 'spam', 1.23]
L.append('NI')  # добавляем к конец списка 'NI'
print(L)
L.pop(2)  # удаление элемента поз.2
print(L)

M = ['bb', 'aa', 'cc']
M.sort()  # сортируем
print('\n', M)
M.reverse()  # обратный порядок
print(M)

N = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print('\n', N[1])
print('\n', N[1][1])

col = [n[1] for n in N]  # выводим столбец 1
print('\n', col)

col = [n[1] + 1 for n in N]  # выводим столбец 1, прибавляя 1 к каждому числу
print('\n', col)

col = [n[1] for n in N if n[1] % 2 == 0]  # отфильтровать нечетные
print('\n', col)

diag = [N[i][i] for i in [0, 1, 2]]  # собрать диагональ
print('\n', diag)