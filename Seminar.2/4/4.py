inputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\4\INPUT.txt','r')
outputFile = open('C:\D\Скачки\GeekBrains\GB.PY\Seminar.2\\4\OUTPUT.txt','w')

inputFile.readline()
row = inputFile.readline().split()
print(row)
newStudHeight = inputFile.readline()
print(newStudHeight)

posInRow = 0
for height in row:
    posInRow += 1
    if height <= newStudHeight:
        row.insert(posInRow-1,newStudHeight)
        #temp = row[posInRow-1]
        #row[posInRow-1] = newStudHeight
        #for i in range(posInRow, len(row)):
        #    if i == len(row) - 1:
        #        temp2 = row[i]
        #        row[i] = temp
        #        row.append(temp2)
        #    temp2 = row[i]
        #    row[i] = temp
        #    temp = temp2
        print(row)
        print(posInRow)
        outputFile.write(f'{posInRow}\n')
        for i in range(0,len(row)-1):
            outputFile.write(f'{row[i]} ')
        outputFile.write(f'{row[len(row)-1]}')
        break

inputFile.close()
outputFile.close()