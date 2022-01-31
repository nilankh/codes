def lar_row_sum(li):
    n = len(li)
    m = len(li[0])
    max_sum = -1
    max_row_index = -1

    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
        if sum > max_sum:
            max_row_index = i
            max_sum = sum
    return max_sum, max_row_index

def lar_col_sum(li):
    n = len(li)
    m = len(li[0])
    max_sum = -1
    max_col_index = -1
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += li[i][j]
        if sum  > max_sum:
            max_col_index = j
            max_sum = sum
    return max_sum, max_col_index

s = input().split()
n, m = int(s[0]), int(s[1])
b = input().split()
li = [[int(b[m*i+j])for j in range(m)]for i in range(n)]
r_sum, r_index = lar_row_sum(li)
c_sum, c_index = lar_col_sum(li)

if r_sum > c_sum:
    print('row', r_index, r_sum)
else:
    print('column', c_index, c_sum)










