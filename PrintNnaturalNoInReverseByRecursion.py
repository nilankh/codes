def print_N_to_1(n):
    if n==0:
        return
    print(n)
    print_N_to_1(n-1)
n=int(input())
print_N_to_1(n)
