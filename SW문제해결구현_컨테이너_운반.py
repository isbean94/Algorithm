T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    S = list(sorted(map(int, input().split())))
    H = list(sorted(map(int, input().split())))

    result = 0

    s = S.pop()
    h = H.pop()

    while S and H:

        if h >= s:
            result += s
            s = S.pop()
            h = H.pop()
        else:
            s = S.pop()

    if h >= s:
        result += s

    print("#{0} {1}".format(t, result))