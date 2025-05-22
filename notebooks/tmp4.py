Q = int(input())

for _ in range(Q):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    pos = list(map(lambda x: abs(x), arr))
    zero = pos[0]
    pos_sorted = sorted(pos)
    arg_zero = pos_sorted.index(zero)

    if arg_zero <= (n//2):
        print("YES")
    else:
        print("NO")