x = int(input())
count = 0
n = 1
while(count < x):
    term = 3 * n + 2
    if(term % 4 != 0):
        print(term, end = " ")
        count += 1
    n += 1
