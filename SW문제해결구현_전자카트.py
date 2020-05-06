T = int(input())
for t in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 999999

    def road(y, k, c, v):
        global result

        if k >= result:
            return

        if c == (N-1):
            k += board[y][0]
            result = k if k < result else result

        for x in range(N):
            if x not in v:
                road(x, k + board[y][x], c + 1, v + [x])

    road(0,0,0,[0])

    print("#{0} {1}".format(t, result))
