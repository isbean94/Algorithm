T = int(input())
for t in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 999999

    def cal(cnt=0, cost=0, check=[]):
        global result

        if len(check) == N:
            result = cost
            return

        for i in range(N):
            if i in check:
                continue
            else:
                ac = cost + board[cnt][i]
                if ac < result:
                    cal(cnt+1, ac, check+[i])

    cal()

    print("#{0} {1}".format(t, result))