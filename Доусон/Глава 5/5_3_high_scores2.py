# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores=[]
choice=None
while choice != "0":
    print(
        """
    Рекорды 2.0
    0- Выйти
    1- Показать результаты
    2- Добавить рекорд
    """
    )
    choice=input("Ваш выбор: ")
    print()
    # Выход
    if choice == "0":
        print("До свидания!")
    # вывод таблицы рекордов
    # если введено 1 комп перебирает элементы списка scores и распаковывает имя
    # каждого рекордсмена и его результат в переменные score и name
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ\tПОПЫТОК")
        for entry in scores: 
            score,name,tries=entry
            print(name,"\t", score, "\t", tries)
    # Добавление рекорда
    elif choice == "2":
        name=input("Впишите имя игрока: ")
        score=int(input("Впишите его результат: "))
        tries=int(input("Впишите количество попыток: "))
        entry=(score,name,tries)
        scores.append(entry)
        scores.sort(reverse=True)
        scores=scores[:5] # в списке остается только 5 рекордов
    else:
        print("Извините, в меню нет пункта ", choise)
input("\n\nВведите Enter, чтобы выйти")
