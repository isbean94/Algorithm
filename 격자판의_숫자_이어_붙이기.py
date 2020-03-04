for t in range(1,int(input())+1):

    board = [input().split() for _ in range(4)]
    result = set()

    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]

    def seven_num(y,x,arr):

        if len(arr) == 7:
            result.add(tuple(arr))
            return

        for d in range(4):
            if (0 <= y+dy[d] < 4) and (0 <= x+dx[d] < 4):
                seven_num(y+dy[d], x+dx[d], arr+[board[y+dy[d]][x+dx[d]]])

    for i in range(4):
        for j in range(4):
            seven_num(i,j,[board[i][j]])

    print(result)
    print(len(result))