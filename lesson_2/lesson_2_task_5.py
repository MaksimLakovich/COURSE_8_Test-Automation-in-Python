def month_to_season():
    number_of_month = input("Введите номер месяца: ")
    try:
        number = int(number_of_month)
        if number in range(1, 3) or number == 12:
            print("Зима")
        elif number in range(3, 6):
            print("Весна")
        elif number in range(6, 9):
            print("Лето")
        elif number in range(9, 12):
            print("Осень")
        else:
            print("Несуществующий месяц, необходимо ввести значение от 1 до 12")
    except ValueError:
        print("Некорректное значение. Доступен ввод только целых чисел от 1 до 12")

month_to_season()