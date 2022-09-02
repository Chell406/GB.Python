dot = [int(input('Введите X:')), int(input('Введите Y:'))]
if(dot[0] == 0 and dot[1] == 0):
    print(f'dot({dot[0]},{dot[1]}) - недопустимое значение')
elif(dot[0] >= 0 and dot[1] >= 0):
    print(f'dot({dot[0]},{dot[1]}) -> 1')
elif(dot[0] <= 0 and dot[1] >= 0):
    print(f'dot({dot[0]},{dot[1]}) -> 2')
elif(dot[0] <= 0 and dot[1] <= 0):
    print(f'dot({dot[0]},{dot[1]}) -> 3')
else:
    print(f'dot({dot[0]},{dot[1]}) -> 4')