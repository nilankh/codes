def fact(n):
    n_fact=1
    for i in range(1,n+1):
        n_fact=n_fact*i
    return n_fact
n=int(input())
r=int(input())
n_fact=fact(n)
r_fact=fact(r)
n_r_fact=fact(n-r)
ans=n_fact//(r_fact*n_r_fact)
print(ans)

