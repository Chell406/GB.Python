inputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\2\INPUT.txt','r')
N = inputFile.readline()
inputFile.close()
print(f'N = {N}')
summary = 0
for i in range(1, int(N) + 1):
    summary += i
print(f'Summary = {summary}')
outputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\2\OUTPUT.txt','w')
outputFile.write(str(summary))
outputFile.close()