# это еще один способ вставлять переменные внутрь текста
# он приятнее и эффективнее, и понадобится нам в будущем
# все равно осознайте, как работает конкатенация строк в предыдущих примерах,
# это тоже важно для понимания

print("Welcome to our coffee shop!")
color = input("What's your favourite color? ")
drink = input("What's your favourite drink? ")
fruit = input("What's your favourite fruit? ")
print(f"Here's your {color} {drink} with some {fruit} ice cream!")

# попробуйте добавить в вывод численные данные. нужно ли их преобразовывать?
# если непонятно, см. следующий файл