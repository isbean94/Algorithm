for t in range(1,int(input())+1):

    N, M, R, C, L = map(int, input().split())
    hole_map = [list(map(int, input().split())) for _ in range(N)]

    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]

    tunnel_dict = {0: [], 1:[0,1,2,3], 2:[0,1], 3:[2,3], 4:[0,3], 5:[1,3], 6:[1,2], 7:[0,2]}
    move_dic = {0: [1,2,5,6], 1:[1,2,4,7], 2:[1,3,4,5], 3:[1,3,6,7]}

    q1 = [(R,C)]
    q2 = []
    result = {(R,C)}
    time = 1

    while time < L:

        while q1:

            state = q1.pop(0)
            y, x = state[0], state[1]

            for d in tunnel_dict[hole_map[state[0]][state[1]]]:
                
                if (0 <= y+dy[d] < N) and (0 <= x+dx[d] < M) and hole_map[y+dy[d]][x+dx[d]]:
                    
                    if hole_map[y+dy[d]][x+dx[d]] in move_dic[d]:
                        q2.append((y+dy[d],x+dx[d]))
                        result.add((y+dy[d],x+dx[d]))
                        hole_map[state[0]][state[1]] = 0
            
        q1, q2 = q2, []
        time += 1

    print("#{0} {1}".format(t, len(result)))