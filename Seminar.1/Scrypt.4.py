quarter = int(input('Номер четверти: '))

if quarter <= 1 or quarter >= 4:
    print('Невозможно определить. Проверьте вводимое значение (от 1 до 4).')
elif quarter == 1:
    print('x: 0...n, y: 0...n')
elif quarter == 2:
    print('x: -n...0, y: 0...n')
elif quarter == 3:
    print('x: -n...0, y: -n...0')
elif quarter == 4:
    print('x: 0...n, y: -n...0')