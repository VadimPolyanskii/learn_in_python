for i in range(10):     # range(start, stop, step)
    print(i)
    if i == 5: break

for i in range(10):
    answer = input('Какой сегодня месяц?')
    if answer == 'сентябрь':
        print('Это верно!')
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)
