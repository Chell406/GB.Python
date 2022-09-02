values = [True, False]

for X in values:
    for Y in values:
        for Z in values:
            if((not (X and Y and Z)) == ((not X) or (not Y) or (not Z))):
                print(True)
            else:
                print(False)