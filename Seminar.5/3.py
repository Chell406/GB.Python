initial = '1e 1e 1 e1e 1e 111www eee3345eeee      rrrr234 1w3d34fff123eee'
initial = list(initial)
output = list()

print(*initial)
i = 0
s = ''
count = 0

# обработка начала
initialSize = len(initial)
while i < initialSize:
    if i == (initialSize - 1):
        output.append(initial[i])
        i += 1
        break
    if initial[i] == ' ':
        output.append(initial[i])
        i += 1
        continue
    if ((ord(initial[i]) >= 46) and (ord(initial[i]) <= 57)):
        output.append(initial[i])
        if ((ord(initial[i+1]) < 46) or (ord(initial[i+1]) > 57)) and (initial[i+1] != ' '):
            output.append(initial[i+1])
            i += 2
            continue 
        else:
            i += 1
            continue
          
    s = initial[i]
    count = 1
    i += 1
    break   

# обработка середины
while i < initialSize - 1:
    
    if initial[i] == s:
        count += 1
        i += 1
        continue
    else:
        if count:
            if count > 1:
                output.append(count)
            output.append(s)

        if initial[i] == ' ':
            output.append(initial[i])
            s = ''
            count = 0
            i += 1
            continue

        if (ord(initial[i]) < 46) or (ord(initial[i]) > 57):
            s = initial[i]
            count = 1
            i += 1
            continue
        else:
            output.append(initial[i])
            s = ''
            count = 0

            if (ord(initial[i+1]) < 46) or (ord(initial[i+1]) > 57):
                output.append(initial[i+1])
                i += 2
                continue
            else:
                i += 1
                continue

# обработка последнего элемента
if i < initialSize:
    if initial[initialSize - 1] == s:
        count += 1
        if count:
            if count > 1:
                output.append(count)
            output.append(s)
    else:
        if count:
            if count > 1:
                output.append(count)
            output.append(s)
        output.append(initial[initialSize - 1])


print(*output)