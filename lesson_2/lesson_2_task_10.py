def bank(dep_sum, dep_years, stavka):
    total_income = 0

    for dep_year in range (0, dep_years):
        income = dep_sum * stavka
        dep_sum = dep_sum + income
        total_income = total_income + income
    
    return (dep_sum, total_income)

dep_sum = 0
dep_years = 0
stavka = 0.1

while dep_sum <= 0:
    try:
        dep_sum = round(float(input("Какую сумму Вы хотите внести на вклад? ")), 2)
        if dep_sum <= 0:
            print("Введите любое положительное число, отличное от нуля")
    except ValueError:
        print("Некорректное значение. Допустим только числовой формат")

def valid_dep_years():
    while True:
        try:
            dep_years = int(input("На сколько лет хотите оформить вклад? "))
            if 1 <= dep_years <= 25:
                return dep_years
            else:
                print("Введите любое целое число больше нуля (от 1 до 25)")
        except ValueError:
            print("Некорректное значение. Допустим только числовой формат")
dep_years = valid_dep_years()

fin_sum, final_income = bank (dep_sum, dep_years, stavka)

if dep_years in [1, 21]:
    years_word = "год"
elif dep_years in [2, 3, 4, 22, 23, 24]:
    years_word = "года"    
else:
    years_word = "лет"
print(f"При размещении {dep_sum} руб. на {dep_years} {years_word}, по окончании срока действия вклада Вы получите: {round(fin_sum, 2)} руб. (итоговый доход составит - {round(final_income, 2)} руб.)")