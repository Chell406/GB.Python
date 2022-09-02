day = int(input('Введите номер дня: '))

print(day)

while day <= 0 or day > 7:
    print('Введено неверное значение')
    day = int(input('Введите номер дня: '))
else:
    if day >=1 or day <= 5:
        print ('Нет')
    else:
        print ('Да')