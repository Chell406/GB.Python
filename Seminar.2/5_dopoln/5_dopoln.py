inputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\5_dopoln\INPUT.txt','r')
outputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\5_dopoln\OUTPUT.txt','w')

N = int(inputFile.readline())
print(N)

shrubs = [int(i) for i in inputFile.readline().split()]
print(shrubs)

maxSumOf3 = 0
for i in range(0,len(shrubs)):
    sumOf3 = shrubs[i-2]+shrubs[i-1]+shrubs[i] #Если использовать индекс i+1, то IndexError: list index out of range
    if maxSumOf3 < sumOf3:
        maxSumOf3 = sumOf3
print(maxSumOf3)
outputFile.write(str(maxSumOf3))

inputFile.close()
outputFile.close()