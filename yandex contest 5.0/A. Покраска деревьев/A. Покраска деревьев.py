p, v =  map(int, input().split())
q, m =  map(int, input().split())

all_num = []

p_min, p_max = p - v, p + v
q_min, q_max = q - m, q + m

min = min(p_min, q_min)
max = max(p_max, q_max)

if (p > q and q_max > p_min) or (q > p and p_max > q_min):
    print(max - min + 1)
elif p_max == q_min or q_max == p_min:
    print(max - min + 1)
elif p == q:
    if v > m:
        print(p_max - p_min + 1)
    else:
        print((q_max - q_min + 1))
else:
    print((p_max - p_min) + (q_max - q_min) + 2)

