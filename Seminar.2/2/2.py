with open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\2\INPUT.txt', 'r') as inputFile:
    N = inputFile.readline()
    inputFile.close()

print(f'N = {N}')
summary = 0
for i in range(1, int(N) + 1):
    summary += i
print(f'Summary = {summary}')

with open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\2\OUTPUT.txt', 'w') as outputFile:
    outputFile.write(str(summary))
    outputFile.close()