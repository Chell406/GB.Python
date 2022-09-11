with open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\1\INPUT.txt', 'r') as inputFile:
    N = int(inputFile.readline())
    print(f'Монет всего:{N}')
    orel,reshko = 0, 0

    for line in inputFile:
        if not int(line):
            orel += 1
        else:
            reshko += 1
    inputFile.close()

turns = min(orel, reshko)

print(f'Количество монет, которые нужно перевернуть: {turns}')
with open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\1\OUTPUT.txt', 'w') as outputFile:
    outputFile.write(str(turns))
    outputFile.close()