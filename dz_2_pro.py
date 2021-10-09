# ДЗ 2 Про

# 1. Выведем на экран циклом пять пронумерованных строк из нулей
for i in range(5):
    print(i+1, '0')

# 2. Пользователь в цикле вводит 10 цифр. Находим количество введенных пользователем цифр 5.
summ = 0
for i in range(10):
    answer = int(input('Please enter a number: '))
    if answer == 5:
        summ += 1
print('Количество цифр 5, введённых пользователем, равно: ', summ)

# 3. Находим и выводим на экран сумму ряда чисел от 1 до 100.
summ = 0
for i in range(1, 101):
    summ += i
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

# 6. Находим сумму цифр числа.
def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


print(sum_digits(2021))

# 7. Найти произведение цифр числа.
num = 12345
prod = 1

while num != 0:
    rem = num % 10
    prod = prod * rem
    num = num // 10

print(prod)

# 8. Дать ответ на вопрос: есть ли среди цифр числа 5?
int_num = int(input('Enter the number: '))

while int_num > 0:
    if int_num % 10 == 5:
        print('Yes')
        break
    int_num //= 10
else: print('No')

# 9. Найти максимальную цифру в числе
number_input = input('Enter the number: ')
max_int = 0
for i in number_input:
   list_int = int(i)
   if list_int > max_int:
       max_int = list_int
print(max_int)

# 10. Найти количество цифр 5 в числе
a = 15555
b = 0

while a > 0:
    if a % 10 == 5:
        b += 1
    a //= 10
print( b)
