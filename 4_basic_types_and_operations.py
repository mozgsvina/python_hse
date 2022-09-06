# в начале мы работали со строками. но данные могут быть разных типов
# это важно, потому что с разными типы данных ведут себя по-разному
# целые числа (integer). состоят из цифр. н-р, 0, 1, 33, 254
# числа с дробной частью (floating-point). состоят из цифр и знака точки. н-р, 15.5, 0.666
# с ними можно делать арифметические операции

print(15 + 15)  # this prints 30
print(15 - 5)  # this prints 10
print(3 * 4)  # this prints 12
print(15 / 3)  # this prints 5.0 (!) результат деления всегда float
print(16 / 3)  # this prints 5.333333333333333
print(16 // 3)  # this prints 5. Это целочисленное деление, отбрасывает остаток
print(16 % 3)  # this prints 1. Остаток от деления

# числа также можно хранить в переменных

int_number = 15
float_number = 14.5
new_number = int_number + float_number

print(new_number)  # this prints 29.5
print(int_number + float_number)  # this prints 29.5

# и так можно:
print(f"the sum of {int_number} and {float_number} is {new_number}")

# а так нельзя, потому что мы не можем сложить разные типы (см. тип ошибки при запуске)
# print("The sum is " + new_number)

# уже знакомый тип — строка. все, что находится внутри кавычек (двойных или одинарных).
# пока мы их только складывали (конкатенация), конечно, можно делать еще много чего (потом)

text = "some text"
print(text * 2)  # а это что? :)
print(len(text))  # а эта функиця len() показывает длину строки в символах

# последний важный тип - булевы значения (bool). их всего два: True и False.
# Они очень пригодятся нам потом
bool_value = True

# функция type() позволяет узнать тип переменной (данных).
# Определим тип переменных, которые создали выше

print(type(int_number))
print(type(float_number))
print(type(text))
print(type(bool_value))
