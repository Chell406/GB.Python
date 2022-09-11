N = 8

def to_2(number):
    ostatok = number % 2
    resultat = (number - ostatok) / 2
    if resultat < 2:
        print(int(resultat),end='')
    else:
        to_2(resultat)
    print(int(ostatok),end='')

to_2(N)
print() #Для вывода с новой строкой при следующем выводе
