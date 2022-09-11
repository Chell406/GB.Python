N = 6

if N == 0:
    fibonachi = [0]
elif N == 1:
    fibonachi = [1, 0, 1]
else:
    fibonachi = [1, 0, 1]
    for i in range(2, N+1):
        fibonachi.append(fibonachi[i]+fibonachi[i-1])
    for i in range(3, N+N, 2):
        if fibonachi[0] < 0:
            fibonachi.insert(0,fibonachi[i])
        else:
            fibonachi.insert(0,-fibonachi[i])

print(fibonachi)