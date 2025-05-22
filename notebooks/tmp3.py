Q = int(input())

for _ in range(Q):
    n, m, p, q = list(map(int, input().split(' ')))

    if n % p != 0:
        print("YES")
        continue

    if m == (n // p) * q:
        print("YES")
        continue

    print("NO")