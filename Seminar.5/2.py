from random import randint

def fieldDrow(field):
    for i in range(0,3):
        print(*field[i])

def jrebij():
    return randint(1,100)%2

def Hod(player, simbol, field):
    while True:
        pos = input(f'{player}, куда поставить {simbol} (строка столбец)(пример: 1 1): ').split()
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        if 3 >= pos[0] >= 1  and 3 >= pos[1] >= 1 and field[pos[0]-1][pos[1]-1] == '*':
            field[pos[0]-1][pos[1]-1] = simbol
            print(pos)
            return
        else:
            print('Введено некорректное значение.')

def winMeter(field,simbol):
    i=0
    j = 0
    while i < 3:
        while j < 3:
            if field[i][j] == simbol:
                j+=1
            else:
                j = 0
                break
            if j == 3:
                return 0
        i+=1

    i=0
    j = 0
    while i < 3:
        while j < 3:
            if field[j][i] == simbol:
                j+=1
            else:
                j = 0
                break
            if j == 3:
                return 0
        i+=1

    i = 0
    j = 0

    while j < 3 and i < 3:
        if field[i][j] == simbol:
            j+=1
            i+=1
        else:
            break
        if j == 3 and i == 3:
            return 0
    i = 2
    j = 0

    while j < 3 and i >-1:
        if field[i][j] == simbol:
            j+=1
            i-=1
        else:
            break
        if j == 3 and i == -1:
            return 0

    for l in field:
        for s in l:
            if s == '*':
                return 1

    return 2

def GameFor2(playerOne,playerTwo):
    gameFlag = True
    gameField = [['*','*','*'],['*','*','*'],['*','*','*']]
    while True:
        fieldDrow(gameField)
        Hod(playerOne, 'x', gameField)
        gameFlag = winMeter(gameField,'x')
        if gameFlag == 2:
            print('Свободных клеток не осталось! Ничья!')
            fieldDrow(gameField)
            break
        if gameFlag:
            fieldDrow(gameField)
            Hod(playerTwo, 'o', gameField)
            gameFlag = winMeter(gameField,'o')
        else:
            print(f'Выйграл {playerOne}!')
            fieldDrow(gameField)
            break
        if gameFlag == 2:
            print('Свободных клеток не осталось! Ничья!')
            fieldDrow(gameField)
            break
        if not gameFlag:
            print(f'Выйграл {playerTwo}!')
            fieldDrow(gameField)
            break

if jrebij():
    print('Первым ходит первый игрок')
    GameFor2('Первый','Второй')
else:
    print('Первым ходит второй игрок')
    GameFor2('Второй','Первый')