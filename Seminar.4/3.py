original = [23, 5 , 4, 4, 2, 10, 3, 3, 3, 4, 5, 17]
resultat = list()

for i in range(0,len(original)):
    unic = True
    for j in range(0,len(resultat)):
        if original[i] == resultat[j]:
            unic = False
            break
    if unic:
        resultat.append(original[i])
        
print(original)
print(resultat)