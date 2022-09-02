values = [0, 1]

for X in values:
    for Y in values:
        for Z in values:
            print(f'For X = {X}, Y = {Y}, Z = {Z}')
            print((not (X or Y or Z)) == ((not X) and (not Y) and (not Z)))