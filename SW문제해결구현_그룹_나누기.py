T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    vote_list = list(map(int, input().split()))

    p = list(range(N+1))

    for m in range(M):
        i, j = vote_list[2*m], vote_list[(2*m)+1]
        
        while True:
            if p[i] == i:
                while True:
                    if (p[j] == j) or (i == j):
                        p[i] = j
                        break
                    else:
                        j = p[j]
                break
            else:
                i = p[i]

    result = 0

    for n in range(1, N+1):
        if p[n] == n:
            result += 1

    print("#{0} {1}".format(t, result))