T = int(input())
for t in range(1,T+1):

    N, E = map(int, input().split())

    P = list(range(N+1))
    C = [999999]*(N+1)
    C[0] = 0

    for _ in range(E):
        s, e, c = map(int, input().split())
        r = C[s] + c
        if C[e] >= r:
            P[e] = s
            C[e] = r

    print("#{0} {1}".format(t, C[N]))
