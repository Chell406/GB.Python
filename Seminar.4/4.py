from random import randint

factors = list()
N = int(input('Введите степень:'))
for i in range(0,N+1):
    factors.append(randint(0,100))
print(factors)

for i in range(0,N):
    if factors[i]:
        print(f'{factors[i]}x^{N-i}',end=' + ')
print(f'{factors[N]} = 0')