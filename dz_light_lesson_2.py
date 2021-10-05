# ДЗ 2 Лайт

# 1. Выведем на экран циклом пять пронумерованных строк из нулей
for i in range(5):
    print(i+1, '0')

# 2. Пользователь в цикле вводит 10 цифр. Находим количество введенных пользователем цифр 5.
summ = 0
for i in range(10):
    answer = int(input('Please enter a number: '))
    if answer == 5:
        summ = summ + 1
print('Количество цифр 5, введённых пользователем, равно: ', summ)


# 3. Находим и выводим на экран сумму ряда чисел от 1 до 100.
numbers = 1
summ = 0

while numbers < 101:
    summ += numbers
    numbers += 1
print(summ)

# 4. Находим и выводим на экран произведение ряда чисел от 1 до 10.
prod = 1
for i in range(1, 10):
    prod = prod * i
print(prod)

# 5. Выводим цифры числа на каждой строчке.
int_num = 2021
while int_num > 0:
    print(int_num % 10)
    int_num //= 10