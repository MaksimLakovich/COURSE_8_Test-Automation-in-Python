def fizz_buzz():
    n = int(input("Введите число: "))
    for n in range(1, (n+1)):
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif (n % 3 == 0):
            print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)

fizz_buzz()