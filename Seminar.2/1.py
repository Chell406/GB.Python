inputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\1.INPUT.txt', 'r')
N = int(inputFile.readline())
print(f'Монет всего:{N}')
turns = 0

for line in inputFile:
    if not int(line):
        turns += 1
inputFile.close()

print(f'Количество монет, которые нужно перевернуть: {turns}')
outputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\1.OUTPUT.txt', 'w')
outputFile.write(str(turns))
outputFile.close()