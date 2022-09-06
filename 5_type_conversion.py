# какой тип данных мы получаем, когда просим пользователя ввести что-то с клавиатуры?
number = input("Введите число от 1 до 10: ")
# пока предположим, что пользователь действительно вводит то, что мы просим
print(type(number))  # this prints <class 'str'>
# даже если пользователь ввел число, тип данных -  строка
number_as_string = "12"  # это тоже строка

# чтобы превратить строку в число, если функция int()
print(int(number_as_string) + 12)  # this prints 24
print("12" + "12")  # this prints 1212
print(int("12") + int("12"))  # this print 24

# аналогично

print(float("14.45") + float("0.5"))  # this prints 14.95

# и наоборот, можно превратить в строку функцией str()
great_score = 10
print("The highest score is " + str(great_score))
# обратите внимание, что следующая строка вызовет ошибку
# print("The highest score is " + great_score)

# можно также преобразовать float в int, но тогда просто отсечется дробная часть
float_as_int = int(14.9)
print(float_as_int)  # this prints 14

# для округления можно использовать функцию round. try this yourself!
