from random import randint

def Zapros(mound,player):
    while True:
        amount = int(input(f'{player}, сколько конфет берете (1-28): '))
        if amount >= 1 and (amount <= mound and amount <=28):
            return amount
        else:
            print('Введено некорректное значение.')

def GameFor2(playerOne,playerTwo):
    N = 2021
    gameRound = 0
    while N > 0:
        gameRound += 1
        print(f'Раунд {gameRound}')
        print(f'Конфет на столе: {N}')
        N -= Zapros(N,playerOne)
        if N:
            print(f'Конфет на столе: {N}')
            N -= Zapros(N,playerTwo)
        else:
            print(f'Конфет не осталось! Выйграл {playerOne}!')
            break
        if not N:
            print(f'Конфет не осталось! Выйграл {playerTwo}!')
            break

def GameFor1(playerOne,playerTwo):
    N = 2021
    gameRound = 0
    if playerOne == 'Дядя Игорь':
        while N > 0:
            gameRound += 1
            print(f'Раунд {gameRound}')
            print(f'Конфет на столе: {N}')
            maunt = unlogicPC(N)
            print(f'{playerOne} берет {maunt} конфет')
            N -= maunt
            if N:
                print(f'Конфет на столе: {N}')
                N -= Zapros(N,playerTwo)
            else:
                print('Конфет не осталось! Выйграл первый игрок!')
                break
            if not N:
                print('Конфет не осталось! Выйграл второй игрок!')
                break
    else:
        while N > 0:
            gameRound += 1
            print(f'Раунд {gameRound}')
            print(f'Конфет на столе: {N}')
            N -= Zapros(N,playerOne)           
            if N:
                print(f'Конфет на столе: {N}')
                maunt = logicPC(N)
                print(f'{playerTwo} берет {maunt} конфет')
                N -= maunt    
            else:
                print('Конфет не осталось! Выйграл первый игрок!')
                break
            if not N:
                print('Конфет не осталось! Выйграл второй игрок!')
                break

def logicPC(mound):
    if mound%28:
        return mound - int(mound/28)*28
    else:
        return 28

def unlogicPC(mound):
    if mound >= 28:
        return randint(1,28)
    else:
        return randint(1,mound)

def jrebij():
    return randint(1,100)%2


gameMod = None
while True:
        gameMod = int(input(f'Выберите режим (1-один игрок,2-два игрока): '))
        if gameMod >= 1 and gameMod <=2:
            break
        else:
            print('Введено некорректное значение.')
if gameMod-1:
    print('Игра на двоих!')
    if jrebij():
        print('Первым ходит первый игрок')
        GameFor2('Первый','Второй')
    else:
        print('Первым ходит второй игрок')
        GameFor2('Второй','Первый')
else:
    print('Игра на одного!')
    if jrebij():
        print('Первым ходит Дядя Игорь')
        GameFor1('Дядя Игорь','Игрок')
    else:
        print('Первым ходит игрок')
        GameFor1('Игрок','Дядя игорь')