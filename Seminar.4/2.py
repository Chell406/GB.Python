N = 666
multipliers = list()
temp = N
while temp>2:
    for i in range(2,int(temp)+1):
        #Проверка на простоту
        simple = 1
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                simple = 0
                break
        #Если число простое, и является множителем
        if simple and temp % i == 0:
            temp /= i
            multipliers.append(i)
            break
multipliers.insert(0,1)
print(multipliers)