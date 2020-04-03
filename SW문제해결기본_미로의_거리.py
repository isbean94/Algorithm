T = int(input())
for t in range(1, T+1):

    N = int(input())
    maze = [list(input()) for _ in range(N)]

    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]

    goal = False
    r = 1

    q_a = []
    q_b = []

    for  y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                q_a.append( (y, x) )

    while q_a:
        
        q_b = q_a[:]
        q_a = []

        while q_b:
            
            v = q_b.pop(0)
            y, x = v[0], v[1]

            for i in range(4):
                if (0 <= y+dy[i] < N) and (0 <= x+dx[i] < N):

                    if maze[y+dy[i]][x+dx[i]] == '0':
                        q_a.append( (y+dy[i], x+dx[i]) )
                        maze[y+dy[i]][x+dx[i]] = r
                    
                    elif maze[y+dy[i]][x+dx[i]] == '3':
                        goal = True
                        r -= 1
                        break

            if goal:
                break
        
        if goal:
            break
        else:
            r += 1

    else:
        r = 0

    print("#{0} {1}".format(t, r))
    





    
