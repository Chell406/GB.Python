a = [1.1, 1.35, 3.07, 4, 10.6]

minRem, maxRem = 0.99, 0.01

for i in a:
    rem = i % int(i)
    if rem:
        if rem < minRem:
            minRem = rem
        if rem > maxRem:
            maxRem = rem

print(round(maxRem - minRem, 2))