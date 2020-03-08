N, W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [ 0, 0,-1, 1]
dy = [-1, 1, 0, 0]

for start in range(H):
    if board[start][N-1]:
        break

q = [(start,N-1)]

while q:
    v = q.pop()
    y, x = v[0], v[1]
    boom, board[y][x] = board[y][x]-1, 0

    for r in range(1,boom):
        for d in range(4):
            if 0 <= y+(dy[d]*r) < H and 0 <= x+(dx[d]*r) < W and board[y+(dy[d]*r)][x+(dx[d]*r)]:
                q.append((y+(dy[d]*r), x+(dx[d]*r)))

for i in range(H):
    print(board[i])
