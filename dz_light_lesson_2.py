# ДЗ Лайт, урок 2

# 1
for i in range(5):
    print(i+1, '0')

# 2
summ = 0
for i in range(10):
    answer = int(input('Please enter a number: '))
    summ = summ + 1
print('Пользователь ввёл', summ, 'цифр')

# 3
numbers = 1
summ = 0

while numbers < 101:
    summ += numbers
    numbers += 1
print(summ)

# 4
prod = 1
for i in range(1, 10):
    prod = prod * i
print(prod)

# 5
int_num = 2021
while int_num > 0:
    print(int_num % 10)
    int_num //= 10