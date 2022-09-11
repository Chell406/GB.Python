inputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\3\INPUT.txt','r')
outputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\3\OUTPUT.txt','w')

N = int(inputFile.readline())
print(N)

for i in range(2, N):
    if not N%i:
        print(i)
        outputFile.write(str(i))
        break

inputFile.close()
outputFile.close()