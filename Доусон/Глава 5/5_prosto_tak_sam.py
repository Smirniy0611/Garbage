scores=[("a","1000"),("b","500"),("c","750")]
choice=None
while choice != "0":
    choice=input("Ваш выбор: ")
    if choice == "0":
        print("До свидания!")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores: 
            name,score =entry
            print(name,"\t", score)
