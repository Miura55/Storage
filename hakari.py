n, r = map(int, raw_input().split())
l = 2 * r
for num in range(1, n + 1):
    h, w, d = map(int, raw_input().split())
    if h >= l and w >= l and d >= l:
        print num
