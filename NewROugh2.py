n = int(input())
i = 2
while(i <= n):
    j = 2
    isPrime = False
    while j < i:
        if i % j == 0:
            isPrime = True
        j = j + 1
    if not isPrime:
        print(i)
    i = i + 1
