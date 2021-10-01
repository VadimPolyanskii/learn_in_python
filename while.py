i = 0

while i < 10:
    print(i)
    i += 1
    if i == 5: break

answer = None

while answer != 'Volvo':
    answer = input('Шведская марка авто?')
print('Верно!')

while i < 10:
    if i == 9: break
    if i < 3: continue
    print(i)
    i += 1