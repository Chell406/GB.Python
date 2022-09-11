a = [2, 3, 4, 5, 6, 2, 9]
mid = int(len(a)/2)

mult = 0
for i in range(0,mid):
    mult += a[i]*a[len(a)-1-i]
if len(a)%2:
    mult += a[mid]**2
print(mult)