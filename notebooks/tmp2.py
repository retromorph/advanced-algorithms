def inv_mod2(lst):
    if len(lst) <= 1:
        return lst, 0

    mid = len(lst) // 2
    left, inv_l = inv_mod2(lst[:mid])
    right, inv_r = inv_mod2(lst[mid:])
    merged, inv = [], inv_l ^ inv_r
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j])
            inv ^= (len(left) - i) & 1
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

def optimal_per(a, n):
    if n < 4:
        return a[:]

    g0 = [a[i] for i in range(0, n, 2)]
    g1 = [a[i] for i in range(1, n, 2)]
    sorted_g0 = sorted(g0)
    sorted_g1 = sorted(g1)
    _, p0 = inv_mod2(g0)
    _, p1 = inv_mod2(g1)

    if p0 == p1:
        final_g0, final_g1 = sorted_g0, sorted_g1
    else:
        if len(g0) > len(g1):
            final_g0 = sorted_g0[:]
            final_g0[-1], final_g0[-2] = final_g0[-2], final_g0[-1]
            final_g1 = sorted_g1
        else:
            final_g1 = sorted_g1[:]
            final_g1[-1], final_g1[-2] = final_g1[-2], final_g1[-1]
            final_g0 = sorted_g0

    res = []
    i0 = i1 = 0
    for i in range(n):
        if i % 2 == 0:
            res.append(final_g0[i0])
            i0 += 1
        else:
            res.append(final_g1[i1])
            i1 += 1
    return res

Q = int(input())

for _ in range(Q):
    n = int(input())
    per = list(map(int, input().split(' ')))
    opt = optimal_per(per, n)
    print(' '.join(map(str, opt)))