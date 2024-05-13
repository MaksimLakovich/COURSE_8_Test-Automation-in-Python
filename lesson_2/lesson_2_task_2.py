# Вариант №1:
def is_year_leap(x):
    print("год", x, ": ", end="")
    if (x % 4 == 0):
        print(True)
    else:
        print(False)

is_year_leap(x = int(input("Введите год: ")))


# # Вариант №2:
# def is_year_leap():
#     x = int(input("Type year: "))
#     print("год", x, ": ", end="")
#     if (x % 4 == 0):
#         print(True)
#     else:
#         print(False)

# is_year_leap()