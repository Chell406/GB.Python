n = int(input('Введите точность(1-16):'))
pi = int()
for i in range(0,n*10):
    pi = pi + pow(12,0.5) * pow(-1, i) / ((2.0 * i + 1) * pow(3, i))
pi = str(pi)

print(f'Число пи c заданной точностью ({n}) = {pi[0]}',end='')
if n :
    print(pi[1],end='')

    for i in range(2,n+2):
        print(pi[i],end='')
print('\n',end='')
