n = int(input('Введите номер числа в последовательности Фибоначчи (0...30): '))

if n <=-1 or n > 30:
    print('Веденно неверное значение. Допустимое значение - 0...30')
    raise SystemExit
if n == 0:
    print(0)
if n == 1:
    print(1)

b = 1
v = 0

#for i in range(0, n+1):
while n-1:
    fibonachi = v + b
    v = b
    b = fibonachi
    n -= 1

print(fibonachi)