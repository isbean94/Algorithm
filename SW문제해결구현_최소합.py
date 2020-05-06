T = int(input())
for t in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 999999

    def road(y,x,k):
        global result

        k += board[y][x]

        if k >= result:
            return

        if (y == N-1) and (x == N-1):
            result = k
            return

        for i in [(y,x+1),(y+1,x)]:
            if  (0 <= i[0] < N) and (0 <= i[1] < N):
                road(i[0],i[1],k)

    road(0,0,0)

    print("#{0} {1}".format(t, result))
