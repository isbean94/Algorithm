for t in range(1,int(input())+1):

    N = int(input())
    square = [list(map(int,input().split())) for _ in range(N)]

    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]

    result = 1
    result_idx = (1,1)

    def move(y,x,cnt=1):

        for d in range(4):
            if (0 <= (y+dy[d]) < N) and (0 <= (x+dx[d]) < N) and (square[y+dy[d]][x+dx[d]] == square[y][x]+1):
                re_cnt = move(y+dy[d],x+dx[d],cnt+1)
                cnt = re_cnt if re_cnt > cnt else cnt

        return cnt
                
    for i in range(N):
        for j in range(N):
            move_cnt = move(i,j)
            if result < move_cnt:
                result = move_cnt
                result_idx = (i,j)
            if result == move_cnt:
                if square[i][j] < square[result_idx[0]][result_idx[1]]:
                    result_idx = (i,j)

    print("#{0} {1} {2}".format(t, square[result_idx[0]][result_idx[1]], result))